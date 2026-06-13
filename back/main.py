from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app = FastAPI(title="전공 과목 기반 자격증 추천 API")

class SubjectRequest(BaseModel):
    subjects: List[str]

CERTIFICATE_DB = {
    "빅데이터프로그래밍": ["빅데이터분석기사"],
    "이산수학": ["COS Pro 1급"],
    "그래픽디자인": ["컴퓨터그래픽스운용기능사"],
    "AI수학": ["ADsP (데이터분석 준전문가)"],
    "객체지향프로그래밍": ["정보처리기사"],
    "오픈소프트웨어실습": ["리눅스마스터 2급"],
    "기계학습": ["AICE Professional"],
    "데이터베이스": ["SQLD (SQL 개발자)"],
    "빅데이터알고리즘": ["COS Pro 1급"],
    "ICT융합전략": ["AWS Certified Cloud Practitioner"],
    "데이터시각화": ["Tableau Desktop Specialist"],
    "네트워크데이터분석": ["네트워크관리사 2급"]
}

@app.post("/recommend")
def recommend_certificates(data: SubjectRequest):
    recommended_certs = set()
    match_details = {} 
    
    for subject in data.subjects:
        if subject in CERTIFICATE_DB:
            certs = CERTIFICATE_DB[subject]
            match_details[subject] = certs 
            for cert in certs:
                recommended_certs.add(cert)
                
    result_list = list(recommended_certs)
    
    if not result_list:
        result_list = ["정보처리기사 (전공자 필수 자격증)"]
        match_details["기본 추천"] = ["정보처리기사"]
        
    return {
        "recommendations": result_list,
        "count": len(result_list),
        "match_details": match_details 
    }