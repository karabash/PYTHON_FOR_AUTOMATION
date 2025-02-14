import requests

url = requests.get('https://services.nvd.nist.gov/rest/json/cves/2.0')
print(url.status_code)
print(url.text)
 

