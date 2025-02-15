from groq import Groq

# Directly set the Groq API key and model name
GROQ_API_KEY = "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"
MODEL_NAME = "llama-3.3-70b-versatile"

def summarize_text(text: str, temperature: float = 0.7, max_tokens: int = 1500) -> str:
    """
    Summarizes academic paper text using the Groq API.
    """
    client = Groq(api_key=GROQ_API_KEY)
    
    prompt_intro = (
        "You are an expert academic summarizer and explainer. "
        "Summarize the following academic paper text, highlighting key concepts, defining technical terms, "
        "and suggesting simple diagrams or flowcharts if applicable. "
        "Provide a concise, clear summary that would help a student quickly grasp the content.\n\n"
    )
    
    messages = [
        {"role": "system", "content": "You are a helpful assistant for academic paper summarization."},
        {"role": "user", "content": prompt_intro + text}
    ]
    
    chat_completion = client.chat.completions.create(
        messages=messages,
        model=MODEL_NAME,
    )
    
    summary = chat_completion.choices[0].message.content
    return summary

def summarize_paper(input_data: str, is_pdf: bool = False) -> str:
    """
    Summarizes an academic paper provided as raw text or a PDF file path.
    """
    if is_pdf:
        from .pdf_extractor import extract_text_from_pdf
        paper_text = extract_text_from_pdf(input_data)
    else:
        paper_text = input_data
    
    return summarize_text(paper_text)
