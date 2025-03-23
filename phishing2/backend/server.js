const express = require('express');
const mongoose = require('mongoose');
const bodyParser = require('body-parser');
const cors = require('cors');
const app = express();

// Middleware
app.use(bodyParser.json());
app.use(cors());

// MongoDB connection
mongoose.connect('mongodb://localhost/phishing_simulation', {
  useNewUrlParser: true,
  useUnifiedTopology: true,
});

// Routes
const authRoutes = require('./routes/auth');
const campaignRoutes = require('./routes/campaigns');
const reportRoutes = require('./routes/reports');
const heatmapRoutes = require('./routes/heatmap');

app.use('/api/auth', authRoutes);
app.use('/api/campaigns', campaignRoutes);
app.use('/api/reports', reportRoutes);
app.use('/api/heatmap', heatmapRoutes);

const PORT = process.env.PORT || 5000;
app.listen(PORT, () => console.log(`Server running on port ${PORT}`));