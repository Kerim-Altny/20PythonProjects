import numpy as np
from PIL import Image
from sklearn.cluster import KMeans

def get_top_colors(image_path, num_colors=10):
    
    img = Image.open(image_path).convert('RGB')
    
    img = img.resize((150, 150))
    
    pixels = np.array(img).reshape(-1, 3)
    
  
    kmeans = KMeans(n_clusters=num_colors, random_state=42)
    kmeans.fit(pixels)
    
    dominant_colors = kmeans.cluster_centers_
    
    hex_colors = []
    for color in dominant_colors:
        r, g, b = [int(c) for c in color]
        hex_color = f"#{r:02x}{g:02x}{b:02x}"
        hex_colors.append(hex_color)
        
    return hex_colors

