import requests
import os
import pandas
import requests
import pandas as pd
class BearerAuth(requests.auth.AuthBase):
    def __init__(self, token):
        #print(f"Token: {token}")
        self.token = token
    def __call__(self, r):
        #print(f"R: {r}")
        r.headers["authorization"] = "ApiToken " + self.token
        r.headers["Accept"]="application/json"
        #print(f"R: {r}")
        return r

def output(resp):
    df = pd.DataFrame.from_dict(resp)
    df.to_csv(sep=',', header=True, index=True, index_label='Index', mode='w')
    print(type(df))
    return df


#taking an argument of list of dictionaries returning a list of dictionaries
def normalizeActions(resp):
    #print(resp[0])
    for i in resp:
        result = i.get('actions')
        #print(f'Value of I in loop {result}')
        if result == None:
            i['actions_upload'] = False
            i['actions_detect'] = False
        else:
            i['actions'] = '-'.join(result)
            if 'upload' in result:
                i['actions_upload'] = True
            if 'detect' in result:
                i['actions_detect'] = True
    #print(resp)
    ####I can drop the key 'Actions' but I ain't dropping it
    return resp

#taking an argument of list of dictionaries returning a list of dictionaries
def normalizeScopes(resp):
    #print('\n\nScope')
    #print(resp[0])
    for i in resp:
        result = i.get('scope')
        if result == None:
            i['scope_siteIds'] = None
            i['scope_tenant'] = None
        else:
            if result.get('siteIds') != None:
                siteIds = result.get('siteIds')
                siteIds = ','.join(siteIds)
                i['scope_siteIds'] = siteIds
     #           print(f'SiteIds: {siteIds}')
            else:
                i['scope_siteIds']=None
            if result.get('tenant') != None:
                siteIds = result.get('tenant')
                i['scope_tenant'] = True
                #print(f'Tenant: {siteIds}')
            else:
                #print(f'Tenant: False')
                i['scope_tenant'] = False
    ####As per Sai Teja Dropping off the 'Scopes Column'
        i.pop('scope')
    #for i in resp:
        #print(f'After Normalizing Scope:{i}\n\n')
    return resp

def convertTheDataToHtml(resp):
    #html = resp.to_html(index=False, classes="ui compact table celled regular-table stackable striped", escape=False, justify="left")
    htmlBody = f'''
    {resp}
    '''
    return htmlBody

urlGet = ''
access_token = BearerAuth('')
resp = requests.get(urlGet, auth=access_token)
#resp = requests.get(url=f"{urlGet}",headers={"Accept":"application/x-www-form-urlencoded","Authorization":f"Bearer {access_token}"})
#print(type(resp))
#result = resp
#print(type(result))
resp = resp.json()
#print(type(resp))
resp = resp['data']
#print(type(resp))
#print(resp)
resp = normalizeActions(resp)
#print(f'Returned Resp after normalizing Actions: {type(resp)}  -- {resp}\n\n')
resp = normalizeScopes(resp)
#resp = normalizingActions(resp)
#print(f'Output() -- {resp}')
resp=output(resp)
#print(f'Output() -- {resp}')
htmlBody = convertTheDataToHtml(resp)
#print(f'HTML BODY -- {htmlBody}  ---  {type(htmlBody)}')

resp =demisto.executeCommand("send-mail", {"to":"", "htmlBody":htmlBody,"subject":"Topic of the day", "replyTo":"", "subject":"This is Sagar Shah CSV"})
#resp =demisto.executeCommand("send-mail", {"to":"", "htmlBody":htmlBody,"subject":"Topic of the day", "replyTo":"", "subject":"This is Sagar Shah CSV"})
##resp = demisto.executeCommand("send-mail", {"htmlBody":htmlBody,"subject":"Sagar Shah","using":"noreply", "subject":"Exclusions CSV Data","to":""})
demisto.log(resp)
