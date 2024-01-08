from web.pages.Analyze import Analyze_func

def Anaylze_view_func(namespace: str, resource_type: str, resource_name: str):
    print(".......................................Analyzing............................")
    return Analyze_func(namespace=namespace,resource_type=resource_type,resource_name=resource_name)