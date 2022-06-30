from fastapi import FastAPI, Request, File, Form, UploadFile

app = FastAPI()
userfullpath = "{}" + "@asahiindia.com"
password = "tasty@lemon09"


@app.post("/")
async def root():
    return "Hello World"


@app.post("/authenticate/")
async def authenticate(request: Request, username: str = Form(), password: str = Form()):
    response_body = {}
    if username and password:
        try:
            dn = userfullpath.format(username)
            ad_response = authenticate_ad_user_test(
                "80.0.0.108", dn, password)
            response_body["msg"] = ad_response
            return response_body
        except:
            response_body["msg"] = ad_response
            return response_body
        finally:
            return response_body


def authenticate_ad_user_test(address, username, password):
    print(username)
    userid = "13666"
    pwd = "12345"
    if userid == username and password == pwd:
        return "user authenticate"
    else:
        return "Invalid LDAP Credentials"
