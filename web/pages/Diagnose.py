
from kube_copilot.chains import ReActLLM
from kube_copilot.prompts import get_diagnose_prompt
from kube_copilot.labeler import CustomLLMThoughtLabeler

def Diagnose_func(namespace:str,pod_name:str,model_name="K8-Copliot-POC"):
    try :

        if not namespace or not pod_name:
            return "Please add your namespace and pod to continue."
    
        prompt = get_diagnose_prompt(namespace, pod_name)
        print("..................Prompt ().................",namespace,pod_name)
        chain = ReActLLM(model=model_name,
                     verbose=True,
                     enable_python=True,
                     auto_approve=True) 
    
        response = chain.run(prompt, callbacks=[CustomLLMThoughtLabeler()]) 

        return response
    except Exception as e:
        return "An Error Occured : "+str(e)








