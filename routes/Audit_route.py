from fastapi import  APIRouter
from fastapi import Query
from views.Audit_view import Audit_view_func

Audit_router = APIRouter()


@Audit_router.post("/Audit")
def Anaylze_route_func(
    namespace: str = Query(..., alias="namespace"),
    pod_name: str = Query(..., alias="podname")
    ):
    try:
        Func_Response = Audit_view_func(namespace=namespace,pod_name=pod_name)
        return Func_Response
    except Exception as e:
        return "error occured : "+str(e)