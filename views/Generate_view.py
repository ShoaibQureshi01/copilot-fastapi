from web.pages.Generate import generate_func

def generate_view_func(prompt: str):
    print(".......................................Generating............................")
    return generate_func(prompt=prompt)



def generate_apply_view_func():
    print(".......................................APplying generates...........................")
    return generate_func(prompt="")