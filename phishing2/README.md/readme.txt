# Phishing Simulation Tool

## Overview

This project is a phishing attack simulation tool designed to train employees on cybersecurity best practices. It includes features for creating phishing campaigns, tracking mouse movements, and visualizing hesitation levels using a heatmap. Additionally, AI and ML techniques are implemented to identify and analyze phishing activities effectively.

## Project Structure


phishing-simulation/
├── backend/
│   ├── models/
│   │   ├── User.js
│   │   ├── Campaign.js
│   │   ├── MouseMovement.js
│   ├── routes/
│   │   ├── auth.js
│   │   ├── campaigns.js
│   │   ├── reports.js
│   │   └── heatmap.js
│   ├── ml/
│   │   ├── phishing_detection.py
│   │   ├── model.pkl
│   ├── server.js
├── frontend/
│   ├── public/
│   │   ├── index.html
│   │   ├── phishingPage.html
│   ├── src/
│   │   ├── components/
│   │   │   ├── Login.js
│   │   │   ├── Dashboard.js
│   │   │   ├── Campaigns.js
│   │   │   ├── Reports.js
│   │   │   └── Heatmap.js
│   │   ├── App.js
│   │   ├── index.js
│   └── package.json
├── README.md


## Installation

### Backend

1. Navigate to the backend directory:
   bash
   cd backend
   

2. Install the dependencies:
   bash
   npm install
   

3. Install Python dependencies for AI/ML:
   bash
   pip install -r requirements.txt
   

4. Start the backend server:
   bash
   npm start
   

### Frontend

1. Navigate to the frontend directory:
   bash
   cd frontend
   

2. Install the dependencies:
   bash
   npm install
   

3. Start the frontend development server:
   bash
   npm start
   

## Usage

1. Open your browser and navigate to http://localhost:3000 to access the frontend.
2. Register as a new user and log in.
3. Use the dashboard to create phishing campaigns, view reports, and visualize mouse movement heatmaps.
4. The AI/ML module will automatically analyze phishing activities and provide insights.
