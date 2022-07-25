from fastapi import *
from fastapi.security import *
from fastapi.middleware.cors import CORSMiddleware
from typing import Union
import pyrebase

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get('/')
async def get():
    return "Hola Mundo"

firebaseConfig = {
    'apiKey': "AIzaSyC8TQdK06K-Gfcuv7TkEZpPrhHemdfexDc",
    'authDomain': "fir-course-69128.firebaseapp.com",
    'databaseURL': "https://fir-course-69128-default-rtdb.firebaseio.com/",
    'projectId': "fir-course-69128",
    'storageBucket': "fir-course-69128.appspot.com",
    'messagingSenderId': "1088238020096",
    'appId': "1:1088238020096:web:345714eb00257621461ae5",
    'measurementId': "G-XR168CFEC8"
}

firebase = pyrebase.initialize_app(firebaseConfig)

securityBasic = HTTPBasic()
securityBearer = HTTPBearer()


@app.get("/user/token/",
         status_code=status.HTTP_202_ACCEPTED,
         summary="Get a token for user",
         description="Get token for user",
         tags=["auth"])
def get_token(credentials: HTTPBasicCredentials = Depends(securityBasic)):
    try:
        email = credentials.username
        password = credentials.password
        auth = firebase.auth()
        user = auth.sign_in_with_email_and_password(email, password)
        response = {
            "token": user["idToken"]
        }
        return response
    except Exception as error:
        print(f"Error : {error}")
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)


@app.get("/users/",
         status_code=status.HTTP_202_ACCEPTED,
         summary="Get a user",
         description="Get a user",
         tags=["auth"])
async def get_user(credentials: HTTPAuthorizationCredentials = Depends(securityBearer)):
    try:
        auth = firebase.auth()
        user = auth.get_account_info(credentials.credentials)
        uid = user['users'][0]['localId']

        db = firebase.database()
        user_data = db.child("users").child(uid).get().val()

        response = {
            'user_data': user_data
        }
        return response
    except Exception as error:
        print(f"Error: {error}")
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)


@app.post("/registro/{email}/{password}/{confirmacion}",
          status_code=status.HTTP_202_ACCEPTED,
          summary="Get a user",
          description="Get a user",
          tags=["auth"])
def new_user(email: str, password: str, confirmacion: str):
    if password == confirmacion:
        auth = firebase.auth()
        auth.create_user_with_email_and_password(email, password)
        return {"Exito": "regisstro completo"}
    else:
        return "Error de registro"
