from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from typing import List
import json

app = FastAPI()

# Enable CORS for all domains
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Load dummy data (100 students)
with open("marks.json", "r") as f:
    student_marks = json.load(f)

@app.get("/api")
def get_marks(name: List[str] = []):
    results = [student_marks.get(n, None) for n in name]
    return {"marks": results}
