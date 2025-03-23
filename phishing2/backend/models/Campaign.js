const mongoose = require('mongoose');

const CampaignSchema = new mongoose.Schema({
  name: {
    type: String,
    required: true,
  },
  description: {
    type: String,
  },
  emailsSent: {
    type: Number,
    default: 0,
  },
  emailsOpened: {
    type: Number,
    default: 0,
  },
  linksClicked: {
    type: Number,
    default: 0,
  },
  startDate: {
    type: Date,
    required: true,
  },
  endDate: {
    type: Date,
    required: true,
  },
});

module.exports = mongoose.model('Campaign', CampaignSchema);