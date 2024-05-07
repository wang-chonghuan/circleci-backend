from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # allow all origins
    allow_credentials=True,
    allow_methods=["*"],  # allow all methods
    allow_headers=["*"],  # allow all headers
)

@app.get("/test")
async def root():
    return {"message": "Hello from CircleCI Backend"}

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=9001, reload=True)
