from fastapi import FastAPI

app = FastAPI()

@app.get("/ask")
async def ask():
    return {"message": "Hello World"}

