

import os
from kube_copilot.chains import ReActLLM
from kube_copilot.prompts import get_audit_prompt
from kube_copilot.labeler import CustomLLMThoughtLabeler

 
def Audit_func(namespace: str, pod_name: str, model_name="K8-Copliot-POC"):
    try:

        if not namespace or not pod_name:
            return "Please add your namespace and pod to continue."
   
        prompt = get_audit_prompt(namespace, pod_name)
        print("..................Prompt ().................",namespace,pod_name)

        # Initialize ReActLLM for the audit process
        chain = ReActLLM(model=model_name, verbose=True, enable_python=False, auto_approve=True)
 
        # Run the audit chain with the generated prompt
        response = chain.run(prompt, callbacks=[CustomLLMThoughtLabeler()])
        print(".........................................response..................................",response)
        return response
 
    except Exception as e:
        return "An Error Occurred: " + str(e)