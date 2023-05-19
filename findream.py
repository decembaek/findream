# Created on iPad.
import requests
import json 

# Your API Key
key = "eae3487f0918a868b08171e7cad209b7"




base_url = "https://www.career.go.kr/cnet/openapi/getOpenApi.json?"

params = {
    'apiKey': key,
    'svcType': 'api',
    'svcCode': 'JOB',
    'contentType': 'json',
    'gubun': 'job_dic_list',
    # Optional parameters. Adjust as needed.
    # 'thisPage': '1',
    # 'perPage': '10',
    # 'searchJobNm': 'programmer',
    # 'jobdicSeq': '123',
}

response = requests.get(base_url, params=params)


if response.status_code == 200:
    data = response.json()
    print("총 길이", len(data))
    print(data)
    with open('job_data.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)
    print("Job data saved to 'job_data.json'")
else:
    print(f"Error: {response.status_code}")
