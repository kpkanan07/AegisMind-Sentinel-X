from fastapi import APIRouter

from backend.ai_engine import analyze_threat


router = APIRouter()



@router.get("/")
def home():

    return {

        "message":
        "AegisMind Sentinel API Running"

    }



@router.post("/analyze-threat")
def analyze(data:dict):


    result = analyze_threat(data)


    return result