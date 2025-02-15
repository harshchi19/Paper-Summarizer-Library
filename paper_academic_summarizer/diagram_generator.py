from graphviz import Digraph

def generate_diagram(summary: str, output_file: str = "diagram") -> None:
    """
    Generates a simple diagram from the summary text using Graphviz.
    """
    dot = Digraph(comment="Paper Summary Diagram")
    
    # Assume each non-empty line in the summary is a key point
    points = [line.strip() for line in summary.split("\n") if line.strip()]
    
    for i, point in enumerate(points):
        dot.node(f"node{i}", point)
        if i > 0:
            dot.edge(f"node{i-1}", f"node{i}")
    
    dot.render(output_file, format="png", cleanup=True)
