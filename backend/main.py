from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware




app = FastAPI()


#CORS CONFIG
origins = [
   
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

print('It worked')
@app.get("/")
def root():
    content = {"Server_Status": "Online"}
    print('It worked')
    return content
