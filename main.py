
from fastapi import FastAPI


from kube_copilot.kubeconfig import setup_kubeconfig
# from kube_copilot.labeler import CustomLLMThoughtLabeler


from routes.Analyze_route import Analyze_router
from routes.Audit_route import Audit_router
from routes.Diagnose_route import Diagnose_router
from routes.Generate_route import Generate_router
from routes.Home_route import Home_router


app = FastAPI()

app.include_router(Analyze_router, prefix="/api", tags=["Analyze"])
app.include_router(Audit_router, prefix="/api", tags=["Audit"])
app.include_router(Diagnose_router, prefix="/api", tags=["Diagnose"])
app.include_router(Generate_router, prefix="/api", tags=["Generate"])
app.include_router(Home_router, prefix="/api", tags=["Home"])

# Set up kubeconfig when running inside Pod
setup_kubeconfig()



if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)