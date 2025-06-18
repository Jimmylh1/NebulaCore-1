from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"message": "NebulaCore-1 Render deployment is live!"}
