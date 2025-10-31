from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import os
import aiml
from autocorrect import spell
import uvicorn

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
BRAIN_FILE = "./pretrained_model/aiml_pretrained_model.dump"
k = aiml.Kernel()

if os.path.exists(BRAIN_FILE):
    print("Loading from brain file: " + BRAIN_FILE)
    k.loadBrain(BRAIN_FILE)
else:
    print("Parsing aiml files")
    k.bootstrap(learnFiles="./pretrained_model/learningFileList.aiml", commands="load aiml")
    print("Saving brain file: " + BRAIN_FILE)
    k.saveBrain(BRAIN_FILE)

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
        query = [spell(w) for w in chat_message.message.split()]
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