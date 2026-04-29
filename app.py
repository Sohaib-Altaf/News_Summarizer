import gradio as gr
from summarizer import get_news_summary, NEWS_SOURCES

# =============================================
# Gradio Web App — Pakistani News Summarizer
# Run: python app.py
# Opens in browser: http://localhost:7860
# =============================================

def run_summarizer(source_key: str, num_articles: int):
    """Called when user clicks the button in UI"""
    try:
        results = get_news_summary(source_key=source_key, max_articles=num_articles)

        output_text = ""
        for i, article in enumerate(results, 1):
            output_text += f"━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n"
            output_text += f"📰 Article {i}\n"
            output_text += f"━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n"
            output_text += f"🔖 Title  : {article['title']}\n"
            output_text += f"📡 Source : {article['source']}\n"
            output_text += f"🔗 Link   : {article['link']}\n\n"
            output_text += f"📝 Summary:\n{article['summary']}\n\n"

        return output_text if output_text else "No articles found. Try another source."

    except Exception as e:
        return f"Error: {str(e)}"


# Source options for dropdown
source_options = {v["name"]: k for k, v in NEWS_SOURCES.items()}

with gr.Blocks(
    title="Pakistani News Summarizer",
    theme=gr.themes.Soft(),
) as demo:

    gr.Markdown("""
    # 📰 Pakistani News Summarizer
    **Automatically fetch and summarize latest news from Dawn, Geo, and ARY News**
    """)

    with gr.Row():
        source_dropdown = gr.Dropdown(
            choices=list(source_options.keys()),
            value="Dawn News",
            label="Select News Source",
        )
        num_slider = gr.Slider(
            minimum=1,
            maximum=10,
            value=5,
            step=1,
            label="Number of Articles",
        )

    summarize_btn = gr.Button("🔍 Fetch & Summarize", variant="primary")

    output_box = gr.Textbox(
        label="Summaries",
        lines=25,
        placeholder="Click 'Fetch & Summarize' to get started...",
    )

    summarize_btn.click(
        fn=lambda name, n: run_summarizer(source_options[name], int(n)),
        inputs=[source_dropdown, num_slider],
        outputs=output_box,
    )

    gr.Markdown("""
    ---
    💡 **Tip:** Results are summarized using Facebook's BART model (AI-powered)
    """)

if __name__ == "__main__":
    demo.launch(share=False)
