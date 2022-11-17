import requests 


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

def get_export_exclusions_outputs(exclusions):
    for exclude in exclusions:
        entry = {
            'CSV_Data': exclude
        }
        #remove_nulls_from_dictionary(entry)
        yield entry


urlGet = ''
access_token = BearerAuth('')
resp = requests.get(urlGet, auth=access_token)
#rint(resp)


r_json={}
print(type(r_json))
r_json = resp.json()
print(type(r_json))
#r_json = r_json.get('data')
#print(r_json)

exlusions_report = r_json