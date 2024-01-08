from fastapi import  APIRouter
from fastapi import Query
from views.Diagnose_view import Diagnose_view_func

Diagnose_router = APIRouter()


@Diagnose_router.post("/Diagnose")
def Diagnose_route_func(
    namespace: str = Query(..., alias="namespace"),
    pod_name: str = Query(..., alias="podname")
    ):
    try:
        Func_Response = Diagnose_view_func(namespace=namespace,pod_name=pod_name)
        return Func_Response
    except Exception as e:
        return "error occured : "+str(e)