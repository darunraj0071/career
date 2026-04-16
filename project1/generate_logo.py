"""
Logo generator script - converts SVG to PNG
Run this script once to generate the logo.png file
"""

from PIL import Image, ImageDraw
import os

def create_logo_image():
    """Create a professional logo image for the AI Career Recommender"""
    
    # Image dimensions
    size = 200
    
    # Create a new image with black background
    img = Image.new('RGB', (size, size), color='#0E1117')
    draw = ImageDraw.Draw(img)
    
    # Colors
    cyan = '#00D9FF'
    dark_bg = '#161B22'
    
    # Draw outer circle
    margin = 5
    draw.ellipse(
        [(margin, margin), (size - margin, size - margin)],
        outline=cyan,
        width=3
    )
    
    # Draw inner circle
    inner_margin = 20
    draw.ellipse(
        [(inner_margin, inner_margin), (size - inner_margin, size - inner_margin)],
        fill=dark_bg,
        outline=cyan,
        width=2
    )
    
    # Draw neural network nodes (circles)
    node_radius = 8
    center = size // 2
    
    # Node positions
    nodes = [
        (center - 30, center - 30),  # Top left
        (center + 30, center - 30),  # Top right
        (center, center + 30),       # Bottom
        (center, center)             # Center
    ]
    
    # Draw nodes
    for i, (x, y) in enumerate(nodes):
        radius = node_radius if i < 3 else 6
        draw.ellipse(
            [(x - radius, y - radius), (x + radius, y + radius)],
            fill=cyan
        )
    
    # Draw connecting lines
    # Top left to center
    draw.line(
        [(center - 30, center - 30), (center, center)],
        fill=cyan,
        width=2
    )
    # Top right to center
    draw.line(
        [(center + 30, center - 30), (center, center)],
        fill=cyan,
        width=2
    )
    # Bottom to center
    draw.line(
        [(center, center + 30), (center, center)],
        fill=cyan,
        width=2
    )
    
    # Draw rocket/growth arrow at top
    arrow_x = center
    arrow_y = center - 55
    draw.polygon(
        [
            (arrow_x, arrow_y),           # Top point
            (arrow_x + 5, arrow_y + 15),  # Right
            (arrow_x, arrow_y + 10),      # Center
            (arrow_x - 5, arrow_y + 15)   # Left
        ],
        fill=cyan
    )
    
    # Save as PNG
    output_path = os.path.join(os.path.dirname(__file__), 'assets', 'logo.png')
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    img.save(output_path)
    print(f"✅ Logo created successfully: {output_path}")

if __name__ == "__main__":
    create_logo_image()
