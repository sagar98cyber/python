import requests
import Get_Token as g

def createCommandForCommitAllAdmins(admins):
    commandReturn =''
    for each in admins:
        if each != '':
            commandReturn += f'<member>{each}</member>'
    commandReturn = commandReturn + '<member>FirstUserNameShouldComeHere</member>'
    #print('Printing Command Return')
    #print(commandReturn)
    return commandReturn

def callCommitAllFunctionForAllTheAdmins(command):
    #print("Calling ---------- def callCommitAllFunctionForAllTheAdmins")
    command = command
    headers = {
        "X-PAN-KEY":g.get_token(),
        "Accept":"application/json"
    }
    url = "https://<your-FQDN>/api/?type=commit&action=partial&cmd="+command
    #print(f'\n\n{url}\n\n')
    requesResp = requests.post(url=url,verify=False,headers=headers)
    #print(requesResp.content)
    return requesResp

def gainTheOutputFromResponseFor13(response):
    #print(f'Flag1: {response} ------- {type(response)}')
    response = response.split("<line>")
    response = response[1].split("</line>")
    response = response[0]
    #print(f'FLAG 1: --------- {response} ----- {type(response)}')
    #print(response)
    return response

def responseCodeHandler(resCode,output):
    if resCode == "19":
        print("Success")
        return '19'
    elif resCode == "13":
        return gainTheOutputFromResponseFor13(output),'13'
    else:
        print(resCode)

def findResponseCodeInOutput(output):
    temp = output.split("code=\"")
    temp = temp[1].split('\"')
    #print(temp[0])
    return temp[0]

def requestAPICall():
    APIKey = g.get_token()
    command = "<commit><partial><admin><member>FirstUserNameShouldComeHere</member></admin><device-group><member>Mobile_User_Device_Group</member></device-group><no-template/><no-template-stack/><no-log-collector-group/><no-log-collector/><no-wildfire-appliance-cluster/><no-wildfire-appliance/><device-and-network>excluded</device-and-network><shared-object>excluded</shared-object></partial></commit>"
    url = "https://<your-FQDN>/api/?type=commit&action=partial&cmd="+command+"&key="+APIKey
    print(f'\n\n{url}\n\n')
    requesResp = requests.post(url=url,verify=False)
    return requesResp

def getAdminFromEachPending(eachPending):
    each=eachPending.split('modified by ')
    if len(each) >1:
        each = each[1]
    else:
        return ''
    each = each.split(' in device-group')
    each = each[0]
    #print(each)
    return each

def getAllTheAdminsOfPendingCommits(response):
    #print(f'In the getAllTheAdminsOfPendingCommits(response) {response}')
    admins = response.split(' security rules')
    collectedAdmins = []
    for each in admins:
        collectedAdmins.append(getAdminFromEachPending(eachPending=each))
    #print('Collected Admins')
    #print(collectedAdmins)
    return collectedAdmins

def getResponseFromSuccess(responseInit):
    response = responseInit.split('<line>')
    response = response[1].split('</line>')
    response = response[0]
    return response

def commitForMultipleAdminsMain(response):
    ####Use the below function to get all the users-admins of pending commits
    ##Also after removing the duplicates
    admins = list(set(getAllTheAdminsOfPendingCommits(response)))
    #print(f'LISTSSS ADMINSS: {admins}')
    ####creating the command to be passed as an API call
    command = f'<commit><partial><admin>{createCommandForCommitAllAdmins(admins)}</admin><device-group><member>Mobile_User_Device_Group</member></device-group><no-template/><no-template-stack/><no-log-collector-group/><no-log-collector/><no-wildfire-appliance-cluster/><no-wildfire-appliance/><device-and-network>excluded</device-and-network><shared-object>excluded</shared-object></partial></commit>'
    #print('PRINTING THE COMMAND')
    #print(command)
    ####Use the Below COMMITALL Function to commit all the changes that have been made """""callCommitAllFunctionForAllTheAdmins()""""
    ####if response code is "13":
    respOfCommitAllAdmins=callCommitAllFunctionForAllTheAdmins(command=command)
    #print('AFTER ALL COMPLETED:')
    print(respOfCommitAllAdmins.content)

try:
    r = requestAPICall()
    responseInit = r.content.decode()
    #print(f'INITIAL RESPONSE CODE: \n{responseInit}')
    if 'The result of this commit would be the same as the previous commit queued/processed' in responseInit:
        ###########CHECK WITH JONATHAN
        print('NO COMMITS IN THE FirstUserNameShouldComeHere user HAS BEEN MADE, however there may be changes in other users')
    else:
        resCode = findResponseCodeInOutput(responseInit)
        response = responseCodeHandler(resCode=resCode,output=responseInit)
        #print(f'\n\n\n{response}---------- {type(response)} ---------------  {resCode} - {type(resCode)}\n\n')
        if '\n' in response:
            response=response.replace('\n','')
        if response == '19':
            print(getResponseFromSuccess(responseInit))
        elif response != []:
            #print('CHECKING FOR RETURN OF "13"')
            #print(response)
            #print(type(response))
            if response[1]=='13':
                commitForMultipleAdminsMain(response=response[0])
        else:
            print('Add an appropriate handler for these response')
            print(response)
except requests.ConnectionError:
    print("failed to connect")