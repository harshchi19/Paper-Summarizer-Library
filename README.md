# Paper Summarizer & Explainer

# Pypi Link = https://pypi.org/project/paper-academic-summarizer/
**Paper Summarizer & Explainer** is a Python library designed to help students and researchers quickly digest complex academic papers. The library extracts text from PDFs or accepts raw text and uses Azure AI Inference (leveraging GitHub models) to generate concise summaries that highlight key concepts and define technical terms. Additionally, it provides an optional feature to generate simple diagrams or flowcharts from the summary.

## Features

- **PDF Text Extraction:** Easily extract text from academic papers in PDF format using [PyPDF2](https://pypi.org/project/PyPDF2/).
- **Automated Summarization:** Leverage Groq and pre-trained NLP models to create clear, concise summaries of academic papers.
- **Diagram Generation:** Generate simple diagrams or flowcharts from summary points using [Graphviz](https://pypi.org/project/graphviz/).
- **Modular Design:** Start with core summarization and gradually expand functionality to include additional explanations or visual aids.

## Installation

### Prerequisites

- Python 3.8 or higher

### Install Dependencies

```bash
<<<<<<< HEAD
pip install Groq PyPDF2 graphviz
```

## Example Usage
import os
import re
from paper_academic_summarizer import summarize_paper, generate_diagram

def shorten_summary(summary: str, max_words: int = 30) -> str:
    """
    Truncates the summary to a specified number of words.
    Appends '...' if the original summary exceeds max_words.
    """
    words = summary.split()
    if len(words) <= max_words:
        return summary
    return " ".join(words[:max_words]) + " ..."

def main():
    # Sample academic paper text with detailed model references
    sample_text = """
    In this study, we present a comprehensive evaluation of several state-of-the-art deep learning architectures
    for image classification and object detection. Our focus includes ResNet50, which uses residual connections
    to mitigate the vanishing gradient problem, Inception-v3 for multi-scale processing, and EfficientNet-B7
    leveraging compound scaling. We also analyze transformer-based models such as the Vision Transformer (ViT)
    and DeiT, discussing their performance trade-offs in terms of accuracy, computational cost, and scalability.
    Overall, these findings provide guidance for selecting and optimizing deep learning architectures in
    real-world applications, where balancing efficiency and accuracy is crucial.
    """

    # Generate the full summary using your library function
    full_summary = summarize_paper(sample_text, is_pdf=False)
    print("Full Summary:\n")
    print(full_summary)

    # Shorten the summary to ensure it's very concise
    short_summary = shorten_summary(full_summary, max_words=30)
    print("\nShort Summary:\n")
    print(short_summary)

    # Generate a diagram from the shortened summary
    output_file = "diagram_short"
    try:
        generate_diagram(short_summary, output_file=output_file)
        print(f"\nShort diagram generated successfully: {output_file}.png")
    except Exception as e:
        print("Error generating diagram:", e)

if __name__ == "__main__":
    main()


## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any enhancements or bug fixes.

## License

This project is licensed under the MIT License.

## Acknowledgments

- [PyPDF2](https://pypi.org/project/PyPDF2/)
- [Graphviz](https://pypi.org/project/graphviz/)
- [Azure AI Inference](https://learn.microsoft.com/en-us/azure/cognitive-services/openai/overview)
- [GitHub Models](https://github.com/microsoft/guidance)

## Contact

For any questions or inquiries, please contact [harshchitaliya193@gmail.com](mailto:harshchitaliya193@gmail.com).


