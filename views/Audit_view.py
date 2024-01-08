from web.pages.Audit import Audit_func

def Audit_view_func(namespace: str, pod_name: str):
    print(".......................................Auditing............................")
    return Audit_func(namespace=namespace,pod_name=pod_name)