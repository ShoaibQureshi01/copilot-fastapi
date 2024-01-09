from kube_copilot.chains import ReActLLM
from kube_copilot.prompts import get_analyze_prompt
from kube_copilot.labeler import CustomLLMThoughtLabeler

def Analyze_func(namespace: str, resource_type: str, resource_name: str, model_name="K8-Copliot-POC"):
    try:
        if not namespace or not resource_type or not resource_name:
            return "Please add your namespace, resource_type, and resource_name to continue."
 
        prompt = get_analyze_prompt(namespace, resource_type, resource_name)
 
        chain = ReActLLM(model=model_name, verbose=True, enable_python=True, auto_approve=True)
        print("..................Response (chain has been build).................",chain)
        response = chain.run(prompt, callbacks=[CustomLLMThoughtLabeler()])
        return response
 
    except Exception as e:
        return "An Error Occurred: " + str(e)