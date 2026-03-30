import gradio as gr
from agent_builder import AgentBuilder

def run_agent(prompt_text, history):
    builder = AgentBuilder()
    builder.add_node("llm", {"name": "assistant"})
    result = builder.execute(prompt_text)
    history.append((prompt_text, result))
    return "", history

with gr.Blocks(title="🤖 AI Agent Builder") as demo:
    gr.Markdown("# 🤖 AI Agent Builder\n### Build AI agents with tools")
    chatbot = gr.Chatbot(height=450)
    prompt = gr.Textbox(label="Task", placeholder="What can you do?")
    run_btn = gr.Button("🚀 Run Agent", variant="primary")
    
    prompt.submit(lambda p, h: run_agent(p, h), [prompt, chatbot], [prompt, chatbot])
    run_btn.click(lambda p, h: run_agent(p, h), [prompt, chatbot], [prompt, chatbot])

demo.launch(server_name="0.0.0.0", server_port=7861)
