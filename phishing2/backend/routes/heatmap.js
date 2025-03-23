const express = require('express');
const MouseMovement = require('../models/MouseMovement');
const router = express.Router();

// Endpoint to save mouse movement data
router.post('/save', async (req, res) => {
  const { movements, userId, phishingPageId } = req.body;
  try {
    const savedMovements = await MouseMovement.insertMany(
      movements.map((movement) => ({
        ...movement,
        userId,
        phishingPageId,
      }))
    );
    res.status(201).json(savedMovements);
  } catch (err) {
    res.status(500).json({ error: 'Failed to save mouse movement data' });
  }
});

// Endpoint to get mouse movement data
router.get('/data', async (req, res) => {
  const { phishingPageId } = req.query;
  try {
    const movements = await MouseMovement.find({ phishingPageId });
    res.json(movements);
  } catch (err) {
    res.status(500).json({ error: 'Failed to fetch mouse movement data' });
  }
});

module.exports = router;