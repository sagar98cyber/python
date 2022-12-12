import requests

#to handle the various status codes responses
def statusCodeHandlerFunction(resCode):
    pass
    if resCode < 300:
        print(f"The response code is: {resCode}")
    elif resCode == 403:
        print(f"Forbidden Final Response: {resCode}")
    elif resCode == 404:
        print(f"Not Found Final Response: {resCode}")
    elif resCode == 400:
        print(f"Response is Bad Request: {resCode}")
    else:
        print("No MAtches final catch condition")
        print("Something went wrong!")
   

def requestAPICall():
    APIKey = "<API-Key>"
    command = "<commit-all><shared-policy><device-group><entry name=\"Device_Group_Name\"></entry></device-group><include-template>yes/no</include-template><merge-with-candidate-cfg>yes/no</merge-with-candidate-cfg><force-template-values>yes/no</force-template-values><validate-only>no</validate-only></shared-policy></commit-all>"
    url = "https://<firewall-domain>/api/?type=commit&action=all&cmd="+command+"&key="+APIKey
    print(f'\n\n{url}\n\n')
    requesResp = requests.post(url=url,verify=False)
    #r = requests.head("https://www.miniclip.com/games/en/")
    #r = requests.head("https://stackoverflow.com")
    #r = requests.head("https://r18.com")
   # print(f"This is the new line \n\n {type(r)}")
    print(requesResp)
    return url
    """if r.status_code >= 300:
        return (False,r.status_code)
    else:
        return (True,r.status_code)"""

try:
    #retry = 0
    r = requestAPICall()
    # prints the int of the status code. Find more at httpstatusrappers.com :)
except requests.ConnectionError:
    print("failed to connect")