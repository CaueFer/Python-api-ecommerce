from fastapi import FastAPI
from dotenv import load_dotenv
from app.routes import router  
from app.db import init_db, close_db  

load_dotenv()

app = FastAPI()

app.include_router(router)

async def lifespan(app: FastAPI):
    await init_db()
    yield 
    await close_db()

app = FastAPI(lifespan=lifespan)

app.include_router(router)

@app.get("/")
async def read_root():
    return {"message": "API is working!"}