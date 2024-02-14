import uvicorn
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def hello_world():
    return {"message": f"OK"}

if __name__ == '__main__':
    import os
    port = os.environ.get('PORT') if os.environ.get('PORT') else 5000
    uvicorn.run("main:app", host="0.0.0.0", port=int(port))
