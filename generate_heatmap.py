import json
import os
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Load data from the saved JSON file
DATA_DIR = "mouse_data"
file_path = os.path.join(DATA_DIR, "mouse_data.json")

def load_mouse_data(file_path):
    data = []
    if os.path.exists(file_path):
        with open(file_path, "r") as f:
            for line in f:
                data.extend(json.loads(line))  # Append all mouse movements
    return data

def generate_heatmap(data):
    x_coords = [entry["x"] for entry in data if entry["type"] == "movement"]
    y_coords = [entry["y"] for entry in data if entry["type"] == "movement"]

    # Create a 2D histogram
    heatmap, xedges, yedges = np.histogram2d(x_coords, y_coords, bins=(50, 50))

    # Plot the heatmap
    plt.figure(figsize=(10, 8))
    sns.heatmap(heatmap.T, cmap="coolwarm", cbar=True)
    plt.title("Mouse Movement Heatmap")
    plt.xlabel("X-axis")
    plt.ylabel("Y-axis")
    plt.gca().invert_yaxis()  # Invert y-axis for screen-like coordinates
    plt.show()

if __name__ == "__main__":
    mouse_data = load_mouse_data(file_path)
    if mouse_data:
        generate_heatmap(mouse_data)
    else:
        print("No data found. Perform some mouse movements on the login page.")
