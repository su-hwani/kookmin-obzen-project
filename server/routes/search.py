
from fastapi import FastAPI, Depends, HTTPException, APIRouter
import httpx
from db.model_chat import *
from sqlalchemy import text
import openai

app = FastAPI()

# 라우터 생성
router = APIRouter()

@router.get("/")
async def get_search():
    return 'hello'

@router.get("/query/")
async def read_item(q: str, db: db_dependency):
    target_url = f"http://43.201.72.216:8000/{q}"
    
    try: 
        response = httpx.get(target_url, timeout=30.0)  # 30 seconds timeout
    
    # 타임 아웃 시 에러 처리
    except httpx.TimeoutException as e:
        error_msg = "HTTP 요청이 타임 아웃되었습니다."
        return {'query': None, 'q': q, 'answer': error_msg}
    
    try:
        returned_query = response.text.strip("\"\\")

        fake_db = FakeSessionLocal()
        
        result = fake_db.execute(text(returned_query))
        data = result.fetchall()
        
    # 데이터가 비었을 때 에러 처리
        if not data: 
            error_msg = "데이터 수집에 실패하였습니다."
            return {'query': returned_query, 'q': q, 'answer': error_msg}
    
    # 쿼리 실행 시 에러 처리
    except Exception as e:
        error_msg = f"쿼리 실행 중 오류가 발생했습니다. msg: {e}"
        return {'query': returned_query, 'q': q, 'answer': error_msg}
        
    finally: 
        fake_db.close() 
        
    # API KEY 삭제
    openai.api_key = "YOUR API KEY"
    messages = [
        {"role": "system", "content": "I'll provide you with three pieces of information. The first one is the user's question, the second is the SQL query required to obtain the answer to that question, and the third is the value received after executing the query in the database. "},
        {"role": "user", "content": f"1. user's question: {q} 2. SQL query: {returned_query} 3. received value: {data} Now, organize the appropriate answers in natural language You can say it in one sentence in Korean"},
    ]
    
    # 필요한 토큰 수 계산
    total_tokens = sum(len(message["content"].split()) for message in messages)
    # 사용 가능한 토큰 수 
    usable_tokens = 1000 
    
    # 토큰이 모자를 때 에러 처리 
    if total_tokens > usable_tokens:
        error_msg = "토큰이 모자릅니다."
        return {'query': returned_query, 'q': q, 'answer': error_msg}
    
    try:
        completion = openai.ChatCompletion.create(
            model="gpt-3.5-turbo", messages=messages)
        final_answer = completion.choices[0].message["content"].strip()
    
    # OpenAI API 에러 처리 
    except openai.error.OpenAIError as e:
        error_msg = "OpenAI API 사용 중 에러가 발생했습니다."
        return {'query': returned_query, 'q': q, 'answer': error_msg}
    # 그 외 에러 처리
    except Exception as e:
        error_msg = f"에러 발생: {e}"
        return {'query': returned_query, 'q': q, 'answer': error_msg}

    nla = {
        'answer': str(final_answer),
        'query': returned_query,
        'q':  q,
    }
    return nla