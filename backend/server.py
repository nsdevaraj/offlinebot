from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import os
import aiml
from autocorrect import Speller
import uvicorn
import time

# Fix for Python 3.8+ compatibility with AIML library
if not hasattr(time, 'clock'):
    time.clock = time.perf_counter

app = FastAPI()

# CORS Configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Initialize AIML Kernel
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BRAIN_FILE = os.path.join(BASE_DIR, "pretrained_model", "aiml_pretrained_model.dump")
LEARNING_FILE = os.path.join(BASE_DIR, "pretrained_model", "learningFileList.aiml")

k = aiml.Kernel()

if os.path.exists(BRAIN_FILE):
    print("Loading from brain file: " + BRAIN_FILE)
    k.loadBrain(BRAIN_FILE)
else:
    print("Parsing aiml files")
    k.bootstrap(learnFiles=LEARNING_FILE, commands="load aiml")
    print("Saving brain file: " + BRAIN_FILE)
    try:
        k.saveBrain(BRAIN_FILE)
        print("Brain file saved successfully!")
    except Exception as e:
        print(f"Warning: Could not save brain file: {e}")
        print("Continuing without brain file (will parse AIML on each startup)")

print("✅ AIML Chatbot ready!")

# Request Model
class ChatMessage(BaseModel):
    message: str

@app.get("/api/health")
async def health_check():
    return {"status": "healthy", "service": "AIML Chatbot API"}

@app.post("/api/chat")
async def chat(chat_message: ChatMessage):
    try:
        # Autocorrect the message
        speller = Speller(lang='en')
        query = [speller(w) for w in chat_message.message.split()]
        question = " ".join(query)
        
        # Get bot response
        response = k.respond(question)
        
        if response:
            return {"response": str(response), "status": "success"}
        else:
            return {"response": "I'm not sure how to respond to that. Can you try asking differently?", "status": "success"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error processing message: {str(e)}")

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8001)
