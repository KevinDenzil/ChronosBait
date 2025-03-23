const mongoose = require('mongoose');

const MouseMovementSchema = new mongoose.Schema({
  x: {
    type: Number,
    required: true,
  },
  y: {
    type: Number,
    required: true,
  },
  timestamp: {
    type: Date,
    default: Date.now,
  },
  userId: {
    type: mongoose.Schema.Types.ObjectId,
    ref: 'User',
    required: true,
  },
  phishingPageId: {
    type: mongoose.Schema.Types.ObjectId,
    ref: 'PhishingPage', // Assuming you have a PhishingPage model
    required: true,
  },
});

module.exports = mongoose.model('MouseMovement', MouseMovementSchema);