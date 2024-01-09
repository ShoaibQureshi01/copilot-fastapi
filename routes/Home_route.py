from fastapi import  APIRouter,Query
from views.Home_view import process_message

Home_router = APIRouter()

@Home_router.post("/Kubernetese_prompt")
def Home_route_func(
    prompt: str = Query(..., alias="prompt")
    ):
    return process_message(message=prompt)