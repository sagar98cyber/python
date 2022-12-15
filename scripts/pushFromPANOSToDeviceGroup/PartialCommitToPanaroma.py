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
    #url =f"https://us1-pamgt-lab.micron.com/api/?type=op&cmd=<commit-all><shared-policy><device-group>Mobile_User_Device_Group</device-group><include-template>yes</include-template><merge-with-candidate-cfg>no</merge-with-candidate-cfg><force-template-values>no</force-template-values><validate-only>no</validate-only></shared-policy></commit-all>&key="+APIKey
    #url =f"https://us1-pamgt-lab.micron.com/api/?type=op&cmd=<commit-all><shared-policy><device-group></device-group></shared-policy></commit-all>&key="+APIKey
    command = "<commit><partial><admin><member>member-userId</member></admin><device-group><member>Member_Device_Group</member></device-group><no-template/><no-template-stack/><no-log-collector-group/><no-log-collector/><no-wildfire-appliance-cluster/><no-wildfire-appliance/><device-and-network>excluded</device-and-network><shared-object>excluded</shared-object></partial></commit>"
    url = "https://<your-FQDN>/api/?type=commit&action=partial&cmd="+command+"&key="+APIKey
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
    temp =''' if r.status_code < 300:
        print("Success")
        print(f"Status Code{r.status_code}")
    else:
        print("Retrying Once...")
        r = requestAPICall()
        if r.status_code < 300:
            print("Success")
            print(f"Status Code{r.status_code}")
        else:
            print("Retrying Twice...")
            r = requestAPICall()
            if r.status_code < 300:
                print("Success")
                print(f"Status Code{r.status_code}")
            else:
                print("Retrying Thrice...")
                r = requestAPICall()
                if r.status_code < 300:
                    print("Success")
                    print(f"Status Code{r.status_code}")
                else:
                    print("Sorry Failed")
    '''
    # prints the int of the status code. Find more at httpstatusrappers.com :)
except requests.ConnectionError:
    print("failed to connect")