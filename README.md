# Paper Summarizer & Explainer
# Pypi Link = https://pypi.org/project/paper-summarizer/
**Paper Summarizer & Explainer** is a Python library designed to help students and researchers quickly digest complex academic papers. The library extracts text from PDFs or accepts raw text and uses Azure AI Inference (leveraging GitHub models) to generate concise summaries that highlight key concepts and define technical terms. Additionally, it provides an optional feature to generate simple diagrams or flowcharts from the summary.

## Features

- **PDF Text Extraction:** Easily extract text from academic papers in PDF format using [PyPDF2](https://pypi.org/project/PyPDF2/).
- **Automated Summarization:** Leverage Azure AI Inference and pre-trained NLP models to create clear, concise summaries of academic papers.
- **Diagram Generation:** Generate simple diagrams or flowcharts from summary points using [Graphviz](https://pypi.org/project/graphviz/).
- **Modular Design:** Start with core summarization and gradually expand functionality to include additional explanations or visual aids.

## Installation

### Prerequisites

- Python 3.8 or higher

### Install Dependencies

```bash
pip install azure-ai-inference PyPDF2 graphviz


