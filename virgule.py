import os
import requests
import logging
from fastapi import FastAPI, UploadFile, File
from transformers import pipeline
from dotenv import load_dotenv

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("Virgule")

app = FastAPI()

load_dotenv()

summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

@app.post("/summarize")
async def summarize_transcript(file: UploadFile = File(...)):
    try:
        content = await file.read()
        text = content.decode('utf-8')

        logger.info("Transcription reçue pour résumé.")
        summary = summarizer(text, max_length=150, min_length=50, do_sample=False)[0]['summary_text']

        logger.info("Résumé réussi.")
        return {"summary": summary}
    except Exception as e:
        logger.error(f"Erreur lors du résumé: {e}")
        return {"error": "Échec du résumé de la transcription"}
