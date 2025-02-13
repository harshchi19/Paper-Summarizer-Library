# import os
# from paper_summarizer import summarize_paper

# def main():
#     # Optionally, you can load environment variables from a .env file:
#     # from dotenv import load_dotenv
#     # load_dotenv()

#     # Specify the absolute path to your research paper PDF.
#     # Update the file_path to point to your PDF file.
#     file_path = r"E:\Python Library\paper_summarizer\examples\Experiment no3.pdf"
    
#     # Print the current working directory (for debugging purposes)
#     print("Current Working Directory:", os.getcwd())
    
#     # Check if the file exists
#     if not os.path.exists(file_path):
#         print(f"File not found: {file_path}")
#         return

#     # Determine if the input is a PDF based on its extension
#     is_pdf = file_path.lower().endswith(".pdf")
    
#     # Generate summary using the provided research paper.
#     summary = summarize_paper(file_path, is_pdf=is_pdf)
#     print("Generated Summary:\n")
#     print(summary)
    
# if __name__ == "__main__":
#     main()

import os
from paper_summarizer import summarize_paper
from graphviz import Digraph

def generate_short_colorful_diagram(summary: str, output_file: str = "short_diagram"):
    """
    Generates a short, colorful diagram from the summarized text using Graphviz.
    - Limits the diagram to a fixed number of lines.
    - Applies color styling to nodes.
    """
    # Split summary into lines, filtering out any empty ones
    lines = [line.strip() for line in summary.strip().split("\n") if line.strip()]

    # Limit how many lines you display to keep the diagram short
    max_lines = 5
    if len(lines) > max_lines:
        lines = lines[:max_lines]
        # Append ellipsis to indicate truncation
        lines[-1] += " ..."

    # Create a Graphviz Digraph with color attributes
    dot = Digraph(comment="Short Summary Diagram")
    dot.attr("node", style="filled", fillcolor="lightblue", shape="box", color="black")

    # Create a node for each line and connect them sequentially
    for i, line in enumerate(lines):
        dot.node(f"node{i}", line)
        if i > 0:
            dot.edge(f"node{i-1}", f"node{i}")

    # Render the diagram to a PNG file
    dot.render(output_file, format="png", cleanup=True)


def main():
    # Optional: Ensure your environment variables (GITHUB_TOKEN, etc.) are already set.
    # e.g. via a .env file or your system environment.

    # Sample text with detailed model names (adjust as needed)
    sample_text = """
    In this study, we present a comprehensive evaluation of several state-of-the-art deep learning architectures for image classification and object detection.
    Our focus includes:
    1) ResNet50, which uses residual connections to mitigate the vanishing gradient problem.
    2) Inception-v3, known for multi-scale processing within its inception modules.
    3) EfficientNet-B7, leveraging compound scaling for improved accuracy and efficiency.
    We also analyze transformer-based models such as the Vision Transformer (ViT) and DeiT, discussing their performance trade-offs.
    Our findings highlight accuracy, computational cost, and scalability, offering guidance for real-world applications.
    """

    # Generate summary (the library reads credentials from environment variables)
    summary = summarize_paper(sample_text, is_pdf=False)
    print("Generated Summary:\n")
    print(summary)

    # Generate a short, colorful diagram from the summary
    output_file = "diagram_short"
    try:
        generate_short_colorful_diagram(summary, output_file=output_file)
        print(f"\nShort, colorful diagram generated successfully: {output_file}.png")
    except Exception as e:
        print("Error generating diagram:", e)


if __name__ == "__main__":
    main()
