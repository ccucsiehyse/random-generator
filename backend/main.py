from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import random

app = FastAPI()

'''
# 允許所有來源，開發階段使用
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:8000"],  # 允許特定的前端來源
    allow_credentials=True,
    allow_methods=["*"],  # 允許所有 HTTP 方法（GET, POST, etc.）
    allow_headers=["*"],  # 允許所有標頭
)
'''

@app.get("/api/random")
async def generate_random():
    number = random.randint(0, 100)
    return {"randomNumber": number}


