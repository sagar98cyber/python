import requests
import Get_Token as g

def requestAPICall():
    APIKey = g.get_token()
    command = "<commit><partial><admin><member>member-userId</member></admin><device-group><member>Member_Device_Group</member></device-group><no-template/><no-template-stack/><no-log-collector-group/><no-log-collector/><no-wildfire-appliance-cluster/><no-wildfire-appliance/><device-and-network>excluded</device-and-network><shared-object>excluded</shared-object></partial></commit>"
    url = "https://<your-FQDN>/api/?type=commit&action=partial&cmd="+command+"&key="+APIKey
    print(f'\n\n{url}\n\n')
    requesResp = requests.post(url=url,verify=False)
    print(requesResp.content)
    return url

try:
    r = requestAPICall()
    # prints the int of the status code. Find more at httpstatusrappers.com :)
except requests.ConnectionError:
    print("failed to connect")