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
    r = requests.head("https://www.miniclip.com/games/en/")
    r = requests.head("https://stackoverflow.com")
    #r = requests.head("https://r18.com")
   # print(f"This is the new line \n\n {type(r)}")
    return r
    """if r.status_code >= 300:
        return (False,r.status_code)
    else:
        return (True,r.status_code)"""

try:
    #retry = 0
    r = requestAPICall()
    if r.status_code < 300:
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

    # prints the int of the status code. Find more at httpstatusrappers.com :)
except requests.ConnectionError:
    print("failed to connect")