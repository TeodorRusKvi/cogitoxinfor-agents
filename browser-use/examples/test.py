import gradio as gr

def greet(name):
    return f"Hello, {name}!"

with gr.Blocks() as demo:
    name_input = gr.Textbox(label="Your Name")
    greet_button = gr.Button("Greet")
    output = gr.Textbox(label="Output")

    greet_button.click(greet, inputs=name_input, outputs=output)

demo.launch()
