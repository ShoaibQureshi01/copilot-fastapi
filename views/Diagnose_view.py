from web.pages.Diagnose import Diagnose_func

def Diagnose_view_func(namespace: str, pod_name:str):
    print(".......................................Diagnoseing............................")
    return Diagnose_func(namespace=namespace,pod_name=pod_name)