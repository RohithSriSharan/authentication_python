from fastapi import FastAPI

app = FastAPI()



@app.get("/")
def root():
    content = {"Server_Status": "Online"}
    return content
