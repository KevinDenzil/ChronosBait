import React, { useEffect } from 'react';
import h337 from 'heatmap.js';

function Heatmap({ phishingPageId }) {
  useEffect(() => {
    const fetchMouseMovements = async () => {
      const response = await fetch(`/api/heatmap/data?phishingPageId=${phishingPageId}`);
      const data = await response.json();
      return data.map((movement) => ({
        x: movement.x,
        y: movement.y,
        value: movement.value || 1,
      }));
    };

    const renderHeatmap = async () => {
      const heatmapInstance = h337.create({
        container: document.getElementById('heatmapContainer'),
      });

      const data = await fetchMouseMovements();
      heatmapInstance.setData({
        max: 5, // Adjust the max value based on your data
        data: data,
      });
    };

    renderHeatmap();
  }, [phishingPageId]);

  return <div id="heatmapContainer" style={{ width: '100%', height: '100vh' }}></div>;
}

export default Heatmap;