
import yaml
from kube_copilot.chains import ReActLLM
from kube_copilot.prompts import get_generate_prompt
from kube_copilot.shell import KubeProcess
from kube_copilot.labeler import CustomLLMThoughtLabeler

def generate_func(prompt:str,model_name="gpt-4"):
    try:
        if not prompt:
            return "Please add your prompt to continue."
        
        print("..................Prompt ().................",prompt)
        chain = ReActLLM(model=model_name,
                     verbose=True,
                     enable_python=True,
                     auto_approve=True)

        response = chain.run(get_generate_prompt(prompt), callbacks="")

        if response != "":
            manifests = response.removeprefix('```').removeprefix('yaml').removesuffix('```').strip()
            try:
                yamls = yaml.safe_load_all(manifests)
            except:
                return "The generated manifests are not valid YAML."
        yield response

        if manifests != "":
            result = KubeProcess(command="kubectl").run('kubectl apply -f -', input=bytes(manifests, 'utf-8'))
            return result
    except Exception as e:
        return "An Error Occured at generate_func"+str(e)

