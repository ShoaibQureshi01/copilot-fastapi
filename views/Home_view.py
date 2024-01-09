from kube_copilot.chains import ReActLLM
from kube_copilot.prompts import get_prompt
from kube_copilot.kubeconfig import setup_kubeconfig

def process_message(message):

    prompt = message
    print(".......................................Kubernetes prompts 1............................",prompt)

    chain = ReActLLM(model="K8-Copliot-POC",  # default to gpt-4 if no other model specified
                     verbose=True,
                     enable_python=True,
                     auto_approve=True)
   
    # Assuming you have a function to generate response from the chain
    response = generate_response(chain, prompt)
    print(".......................................Kubernetes prompts 2............................")
   
    return {"role": "assistant", "content": response}
 
def generate_response(chain, prompt):
    st_cb = ...  # Initialize your StreamlitCallbackHandler if needed
    response = chain.run(get_prompt(prompt), callbacks=[st_cb])
    return response