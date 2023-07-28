from fastapi import APIRouter, Request
from src.services import spotify_service

router = APIRouter()


@router.post("/predict", status_code=200)
async def predict(request: Request):
    json_ = await request.json()
    prediction = spotify_service.recommend_songs(json_)
    return {"prediction": list(prediction)}
