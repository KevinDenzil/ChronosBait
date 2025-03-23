const express = require('express');
const Campaign = require('../models/Campaign');
const router = express.Router();

// Create a new campaign
router.post('/', async (req, res) => {
  const { name, description, startDate, endDate } = req.body;
  try {
    const campaign = new Campaign({ name, description, startDate, endDate });
    await campaign.save();
    res.status(201).json(campaign);
  } catch (err) {
    res.status(500).json({ error: 'Failed to create campaign' });
  }
});

// Get all campaigns
router.get('/', async (req, res) => {
  try {
    const campaigns = await Campaign.find({});
    res.json(campaigns);
  } catch (err) {
    res.status(500).json({ error: 'Failed to fetch campaigns' });
  }
});

module.exports = router;