const express = require('express');
const Campaign = require('../models/Campaign');
const router = express.Router();

// Get campaign report
router.get('/:id', async (req, res) => {
  const { id } = req.params;
  try {
    const campaign = await Campaign.findById(id);
    if (!campaign) {
      return res.status(404).json({ error: 'Campaign not found' });
    }
    res.json(campaign);
  } catch (err) {
    res.status(500).json({ error: 'Failed to fetch campaign report' });
  }
});

module.exports = router;