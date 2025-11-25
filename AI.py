import requests
api_parameters = {
    "max_records": "200"
    }
try:
    api_headers = {
        "Authorization": "Zoho-oauthtoken 1000.293e0fd16100f06e6f19c4b8648e8bf4.19119cb252881a03a3df34118003296c"
    }
    report_response = requests.get(
        "https://www.zohoapis.in/creator/v2.1/data/rcidigitalsolutions387/pranesh-application/report/motor_dataset_500_Report",params=api_parameters,
        headers=api_headers
    )
    var = report_response.json()
    data1 = list()
    if "data" in var:
        # lst = "Type, Speed, Manufacturer, Model, Power"
        for record in var["data"]:
            if "ID" in record:
                id = record.get("ID1")
                desc = record.get("Description")
                alldata = str(id) + "," + str(desc)
                data1.append(alldata)
    # print(data1)
                # Sno = record.get("SNO1")
                # data1.append(Sno)
    print(data1)
    # collect = "Data Fetched"
    # print(collect)
    # if collect == "Data Fetched":
    #     URL = "https://ollama.com/api/chat"
    #     headers = {
    #     "Authorization": "Bearer e79a036b75eb4053b879c24ab2fd437b.1JBJ2GtpVEOuW-Gw_uZibf2I"
    #     }
    #     data = {
    #     "model": "gpt-oss:120b",
    #     "messages": [
    #         {
    #             "role": "user",
    #             "content":
    #                 "You must not modify, remove, reorder, or alter any part of the user-provided input. "
    #                 "The input is a repeating CSV-like pattern: ID,Description. Your task is to analyze ONLY the Description values "
    #                 "and assign an Attribute to each one using ONLY the attribute list provided by the user: " + lst +
    #                 ". You must not use any attribute that is not explicitly present in " + lst +
    #                 ". For each Description, assign exactly ONE Attribute from the provided list or '-' if none apply. "
    #                 "Attribute assignment rules (MANDATORY and STRICT): 'MOTOR' → the exact token from " + lst +
    #                 " that represents Type; known manufacturers (ABB, BALDOR, SIEMENS, JOHNSON, CGL, KEC, ANSONS, TAIWAN, "
    #                 "LEROY-SOMER, etc.) → the exact Manufacturer token from " + lst +
    #                 "; values ending with 'RPM' → the Speed attribute token from " + lst +
    #                 "; model-like codes (FR:, CB, ND, KH, Y100, W300, R370, etc.) → the Model attribute token from " + lst +
    #                 "; numeric values containing 'KW' → assign '-' unless the exact attribute 'Power' exists inside " + lst +
    #                 "; anything that does not match any rule must be '-' with no exceptions. You MUST preserve every Description exactly "
    #                 "as provided, including casing and special characters. The output MUST be a single raw JSON object strictly in this format "
    #                 "and nothing else: {\"data\":[{\"SNo\":\"1\",\"ID\":\"xxxx\",\"Description\":\"xxxx\",\"Attribute\":\"xxxx\"},...]} "
    #                 "with keys ONLY in this exact order: SNo,ID,Description,Attribute. SNo must start at '1' and increment by 1 for each "
    #                 "Description in the input with no gaps. DO NOT wrap the JSON in code fences. DO NOT output explanation, comments, or notes. "
    #                 "DO NOT output anything before or after the JSON. The input is: " + str(data1) + " and the Attributes are: " + lst +
    #                 " — produce the JSON now."
    #         }
    #     ],
    #     "stream": False
    # }
    # response = requests.post(URL, headers=headers, json=data)
    # res = response.json()
    # result = res.get("message").get("content")
    # print(result)
    # Ai = "Excecuted"
    # if Ai == "Excecuted":
    #     if "data" in result:
    #         for op in result["data"]:
    #             sno = op.get("SNo")
    #             mid = op.get("ID")
    #             desc = op.get("Description")
    #             attr = op.get("Attribute")
    #         print(f"SNo: {sno}, ID: {mid}, Description: {desc}, Attribute: {attr}")
            #     SNO = record.get("SNO")
            #     id1 = record.get("ID")
            #     Discription = record.get("Discription")
            #     Attribute = record.get("Attribute")
            # print(f"SNO: {SNO}, ID: {id1}, Discription: {Discription}, Attribute: {Attribute}")
except:
  print("Exception while making the API request.")
