from fastapi import FastAPI
from pydantic import BaseModel
from query_engine import ask_question
from anomaly import detect_anomalies

app = FastAPI()

class QueryRequest(BaseModel):
    question: str

@app.get("/health")
def health():
    return {"status": "running"}

@app.post("/query")
def query(data: QueryRequest):
    return {"answer": ask_question(data.question)}

@app.get("/anomalies")
def anomalies():
    return {"anomalies": detect_anomalies()}
