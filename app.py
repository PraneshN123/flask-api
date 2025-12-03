from flask import Flask, request, jsonify
import requests
import json

app = Flask(__name__)

@app.route("/run", methods=["POST"])
def run_script():
    try:
        api_parameters = {
            "max_records": "200"
        }

        # Motor Dataset record fetching
        api_headers = {
            "Authorization": "Zoho-oauthtoken 1000.dcd94aaf6e99306fb2debe66fc2c1b54.f0aca6b6172966aea6a4c635c0f1dc96"
        }

        report_response = requests.get(
            "https://www.zohoapis.in/creator/v2.1/data/rcidigitalsolutions387/pranesh-application/report/motor_dataset_500_Report",
            params=api_parameters,
            headers=api_headers
        )

        var = report_response.json()
        data1 = []

        if "data" in var:
            fixed_attributes = "Type, Speed, Manufacturer, Model, Power"
            for record in var["data"]:
                # FIX: "ID" does not exist; "ID1" does
                id = record.get("ID1")
                desc = record.get("Description")
                if id is not None and desc is not None:
                    alldata = str(id) + "," + str(desc)
                    data1.append(alldata)

        print(data1)

        # Attribute record fetching
        api_headers2 = {
            "Authorization": "Zoho-oauthtoken 1000.dcd94aaf6e99306fb2debe66fc2c1b54.f0aca6b6172966aea6a4c635c0f1dc96"
        }

        report_response1 = requests.get(
            "https://www.zohoapis.in/creator/v2.1/data/rcidigitalsolutions387/pranesh-application/report/All_Attributes",
            params=api_parameters,
            headers=api_headers2
        )

        var1 = report_response1.json()
        lst = []

        if "data" in var1:
            for record1 in var1["data"]:
                att = record1.get("Attributes")
                if att is not None:
                    lst.append(str(att))

        # Convert attribute list to clean comma string
        lst_str = ", ".join(lst)

        collect = "Data Fetched"
        print(collect)

        if collect == "Data Fetched":
            URL = "https://ollama.com/api/chat"
            headers = {
                "Authorization": "Bearer e79a036b75eb4053b879c24ab2fd437b.1JBJ2GtpVEOuW-Gw_uZibf2I"
            }

            content_prompt = (
                "You must not modify, remove, reorder, or alter any part of the user-provided input. "
                "The input is a repeating CSV-like pattern: ID,Description. Your task is to analyze ONLY the Description values "
                "and assign an Attribute to each one using ONLY the attribute list provided by the user: " + lst_str +
                ". You must not use any attribute that is not explicitly present in " + lst_str +
                ". For each Description, assign exactly ONE Attribute from the provided list or '-' if none apply. "
                "Attribute assignment rules (MANDATORY and STRICT): 'MOTOR' → the exact token from " + lst_str +
                " that represents Type; known manufacturers (ABB, BALDOR, SIEMENS, JOHNSON, CGL, KEC, ANSONS, TAIWAN, "
                "LEROY-SOMER, etc.) → the exact Manufacturer token from " + lst_str +
                "; values ending with 'RPM' → the Speed attribute token from " + lst_str +
                "; model-like codes (FR:, CB, ND, KH, Y100, W300, R370, etc.) → the Model attribute token from " + lst_str +
                "; numeric values containing 'KW' → assign '-' unless the exact attribute 'Power' exists inside " + lst_str +
                "; anything that does not match any rule must be '-' with no exceptions. You MUST preserve every Description exactly "
                "as provided, including casing and special characters. The output MUST be a single raw JSON object strictly in this format "
                "and nothing else: {\"data\":[{\"SNo\":\"1\",\"ID\":\"xxxx\",\"Description\":\"xxxx\",\"Attribute\":\"xxxx\"}]} "
                "with keys ONLY in this exact order: SNo,ID,Description,Attribute. SNo must start at '1' and increment by 1 for each "
                "Description in the input with no gaps. DO NOT wrap the JSON in code fences. DO NOT output explanation, comments, or notes. "
                "DO NOT output anything before or after the JSON. The input is: " + str(data1) + " and the Attributes are: " + lst_str +
                " — produce the JSON now."
            )

            data = {
                "model": "gpt-oss:120b",
                "messages": [
                    {"role": "user", "content": content_prompt}
                ],
                "stream": False
            }

            response = requests.post(URL, headers=headers, json=data)
            res = response.json()

            result = res.get("message", {}).get("content", "{}")
            jsn = json.loads(result)
            if "data" in jsn:
                for op in jsn["data"]:
                    sno = op.get("SNo")
                    mid = op.get("ID")
                    desc = op.get("Description")
                    attr = op.get("Attribute")

                    payload = {
                        "data": [
                            {
                                "Number": int(sno),
                                "ID1": mid,
                                "Discription": desc,
                                "Attribute": attr
                            }
                        ]
                    }

                    api_headers1 = {
                        "Authorization": "Zoho-oauthtoken 1000.6f9316ce93aff9ee2faac607d034fd7c.c5940754701f67d21e98a72b30c06c6d"
                    }

                    try:
                        requests.post(
                            "https://www.zohoapis.in/creator/v2.1/data/rcidigitalsolutions387/pranesh-application/form/Template",
                            headers=api_headers1,
                            data=str(payload)
                        )
                    except:
                        print("Exception while making the API request.")

            return jsonify({"status": "success", "result": jsn})

    except Exception as e:
        return jsonify({"status": "error", "message": str(e)})


@app.route("/", methods=["GET"])
def home():
    return jsonify({"status": "ok", "message": "API is running"})
