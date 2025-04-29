from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
import openai
import os
from dotenv import load_dotenv

load_dotenv()

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def root():
    return {"message": "Bienvenido a JurisMind Abogados"}

@app.post("/consulta")
async def consulta_legal(request: Request):
    data = await request.json()
    pregunta = data.get("pregunta", "")

    if not pregunta:
        return {"error": "No se recibió ninguna pregunta"}

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": pregunta}]
    )

    return {"respuesta": response['choices'][0]['message']['content']}

