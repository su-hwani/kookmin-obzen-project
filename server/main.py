from routes import chats, chatAnswer, chatQuestion, chatRoom, session, search
from db import model_chat, model_chatAnswer, model_chatQuestion, model_chatRoom
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from db.db import engine
from db.model_session import Session  # Import your models

app = FastAPI()

origins = ["https://deploy-preview-31--dainty-cendol-bf34a5.netlify.app"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Define your database models and associate them with the metadata

model_chat.Chat.metadata.create_all(bind=engine)
model_chatAnswer.ChatAnswer.metadata.create_all(bind=engine)
model_chatQuestion.ChatQuestion.metadata.create_all(bind=engine)
model_chatRoom.ChatRoom.metadata.create_all(bind=engine)
Session.metadata.create_all(bind=engine)

# Define your routes

app.include_router(chats.router, prefix="/chats")
app.include_router(chatRoom.router, prefix="/chatRoom")
app.include_router(chatAnswer.router, prefix="/chatAnswer")
app.include_router(chatQuestion.router, prefix="/chatQuestion")
app.include_router(session.router, prefix="/session")
app.include_router(search.router, prefix="/search")
# Define your main route


@app.get('/')
async def home():
    return {'msg': 'main.py'}

