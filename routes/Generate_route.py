from fastapi import  APIRouter
from fastapi import Query
from views.Generate_view import generate_view_func,generate_apply_view_func

Generate_router = APIRouter()

@Generate_router.post("/Generate")
def Genarate_route_func(
    prompt: str = Query(..., alias="prompt"),
    ):
    try:
        Func_Response = generate_view_func(prompt=prompt)
        return Func_Response
    except Exception as e:
        return "error occured : "+str(e)
    
@Generate_router.post("/ApplyGenerate")
def ApplyGenerate_route_func():
    try:
        Func_Response = generate_apply_view_func()
        return Func_Response
    except Exception as e:
        return "error occured : "+str(e)