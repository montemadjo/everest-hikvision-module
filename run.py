import requests
from requests.auth import HTTPDigestAuth
url = 'http://192.168.1.33/ISAPI/System/IO/outputs/1/trigger'
# url = 'http://192.168.1.33/ISAPI/System/IO/capabilities'
raw = '<IOPortData version="2.0" xmlns="http://www.isapi.org/ver20/XMLSchema"><outputState>low</outputState></IOPortData>'
response = requests.put(url, data=raw, auth=HTTPDigestAuth('admin', 'Admin123'))
print(response.status_code)