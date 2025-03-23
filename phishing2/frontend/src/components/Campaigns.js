import React, { useState, useEffect } from 'react';
import axios from 'axios';

function Campaigns() {
  const [campaigns, setCampaigns] = useState([]);

  useEffect(() => {
    const fetchCampaigns = async () => {
      try {
        const response = await axios.get('/api/campaigns');
        setCampaigns(response.data);
      } catch (err) {
        console.error('Failed to fetch campaigns', err);
      }
    };

    fetchCampaigns();
  }, []);

  return (
    <div>
      <h2>Campaigns</h2>
      <ul>
        {campaigns.map((campaign) => (
          <li key={campaign._id}>{campaign.name}</li>
        ))}
      </ul>
    </div>
  );
}

export default Campaigns;