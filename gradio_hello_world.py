import gradio as gr

def greet(name, age):
    return "Hello " + name + "! Your age is "+str(age)+".

demo = gr.Interface(
    fn=greet, 
    inputs=["text", "text"], 
    outputs="text"
)
demo.launch()