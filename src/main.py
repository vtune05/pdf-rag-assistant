from fastapi import FastAPI
from google import genai
from dotenv import load_dotenv
from pydantic import BaseModel

app = FastAPI()

load_dotenv()
client = genai.Client()

class Question(BaseModel):
    text: str

@app.get("/")
def home():
    return {"Status": "Server is working"}

@app.post("/ask")
def ask(question : Question):
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=question.text,
    )
    return {"answer": response.text}