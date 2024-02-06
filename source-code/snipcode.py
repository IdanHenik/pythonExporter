import requests
import os
api_url = os.environ.get('API_URL', 'https://example.com/api/v2/')
token = os.environ.get('API_TOKEN', 'your_default_token')
headers = {'Authorization': 'Bearer ' + token}
api_endpoint = 'jobs'
url = f'{api_url}' + f'/{api_endpoint}' + '/'
payload = {}

    # makes request to controller user endpoint
response = requests.request('GET', url, headers=headers, data=payload, allow_redirects=False, verify=False)
print(response)
response.raise_for_status()  # raises exception when not a 2xx response
