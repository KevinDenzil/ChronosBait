from flask import Flask, request, jsonify
import json
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import os

app = Flask(__name__)

# Endpoint to receive mouse data
@app.route('/mouse-data', methods=['POST'])
def receive_mouse_data():
    data = request.get_json()
    username = data.get('username', 'unknown_user')
    mouse_data = data.get('mouseData', [])

    # Save mouse data to a file
    file_name = f"{username}_mouse_data.json"
    with open(file_name, 'w') as f:
        json.dump(mouse_data, f, indent=4)

    # Generate a heatmap
    generate_heatmap(mouse_data, username)
    return jsonify({"message": "Mouse data recorded!"}), 200

def generate_heatmap(mouse_data, username):
    # Extract coordinates for heatmap
    x_coords = [entry['x'] for entry in mouse_data if entry['type'] == 'move']
    y_coords = [entry['y'] for entry in mouse_data if entry['type'] == 'move']

    if not x_coords or not y_coords:
        return

    # Create a 2D histogram for the heatmap
    heatmap, x_edges, y_edges = np.histogram2d(x_coords, y_coords, bins=(50, 50))

    # Plot the heatmap
    plt.figure(figsize=(8, 6))
    sns.heatmap(heatmap.T, cmap='coolwarm', cbar=True, xticklabels=False, yticklabels=False)
    plt.title(f"Mouse Movement Heatmap - {username}")
    plt.xlabel('X Coordinate')
    plt.ylabel('Y Coordinate')

    # Save the heatmap
    output_file = f"{username}_heatmap.png"
    plt.savefig(output_file)
    plt.close()

if __name__ == '__main__':
    app.run(debug=True)
