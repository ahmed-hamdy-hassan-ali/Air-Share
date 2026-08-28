from fastapi import FastAPI, UploadFile, File
import uvicorn
import socket

app = FastAPI()

def get_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        s.connect(("8.8.8.8", 80))
        return s.getsockname()[0]
    finally:
        s.close()

def start_api():
    uvicorn.run("main:app",host="0.0.0.0",reload=True)

