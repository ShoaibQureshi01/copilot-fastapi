from fastapi import  APIRouter
from fastapi import Query
from views.Analyze_view import Anaylze_view_func

Analyze_router = APIRouter()


@Analyze_router.post("/Analyze")
def Anaylze_route_func(
    namespace: str = Query(..., alias="namespace"),
    resource_type: str = Query(..., alias="resource_type"),
    resource_name: str = Query(..., alias="resource_name")
    ):
    try:
        Func_Response = Anaylze_view_func(namespace=namespace,resource_type=resource_type,resource_name=resource_name)
        return Func_Response
    except Exception as e:
        return "error occured : "+str(e)