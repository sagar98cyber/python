import requests
import Get_Token as g

def requestAPICall():
    APIKey = g.get_token()
    command = "<commit-all><shared-policy><device-group><entry name=\"Mobile_User_Device_Group\"></entry></device-group><include-template>no</include-template><merge-with-candidate-cfg>no</merge-with-candidate-cfg><force-template-values>no</force-template-values><validate-only>no</validate-only></shared-policy></commit-all>"
    url = "https://<your-FQDN>/api/?type=commit&action=all&cmd="+command+"&key="+APIKey
    print(f'\n\n{url}\n\n')
    requesResp = requests.post(url=url,verify=False)
    print(requesResp.content)
    return url

try:
    #retry = 0
    r = requestAPICall()
    # prints the int of the status code. Find more at httpstatusrappers.com :)
except requests.ConnectionError:
    print("failed to connect")