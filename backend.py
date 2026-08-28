from fastapi import FastAPI, UploadFile, File
import uvicorn


app = FastAPI()



def start_api():
    uvicorn.run("main:app",host="0.0.0.0",reload=True)

