import os
from azure.ai.inference import ChatCompletionsClient
from azure.ai.inference.models import SystemMessage, UserMessage
from azure.core.credentials import AzureKeyCredential

# Hardcoded credentials provided by you
ENDPOINT = "https://models.inference.ai.azure.com"
MODEL_NAME = "gpt-4o"
GITHUB_TOKEN = "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"

def summarize_text(text: str, temperature: float = 0.7, max_tokens: int = 1500) -> str:
    """
    Summarizes academic paper text using Azure AI Inference.
    """
    client = ChatCompletionsClient(
        endpoint=ENDPOINT,
        credential=AzureKeyCredential(GITHUB_TOKEN)
    )
    
    prompt_intro = (
        "You are an expert academic summarizer and explainer. "
        "Summarize the following academic paper text, highlighting key concepts, defining technical terms, "
        "and suggesting simple diagrams or flowcharts if applicable. "
        "Provide a concise, clear summary that would help a student quickly grasp the content.\n\n"
    )
    
    messages = [
        SystemMessage("You are a helpful assistant for academic paper summarization."),
        UserMessage(prompt_intro + text)
    ]
    
    response = client.complete(
        messages=messages,
        temperature=temperature,
        max_tokens=max_tokens,
        model=MODEL_NAME
    )
    
    summary = response.choices[0].message.content
    client.close()
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
