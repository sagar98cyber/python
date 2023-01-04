import requests
import xml.dom.minidom as minidom

def get_token():
    params = {
    "user":"<User-Id>",
    "password":"<Password>"}
    
    url = "https://<Your-FQDN>/api/?type=keygen"
    try:
        response = requests.get(url, verify = False,  params = params)
        xmlparse = minidom.parseString(response.text)
        result = xmlparse.getElementsByTagName('key')
        token = result[0].firstChild.nodeValue
        return(str(token))
    except:
        print("Auth Unsuccesful")
