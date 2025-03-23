import React, { useState, useEffect } from 'react';
import axios from 'axios';

function Reports() {
  const [reports, setReports] = useState([]);

  useEffect(() => {
    const fetchReports = async () => {
      try {
        const response = await axios.get('/api/reports');
        setReports(response.data);
      } catch (err) {
        console.error('Failed to fetch reports', err);
      }
    };

    fetchReports();
  }, []);

  return (
    <div>
      <h2>Reports</h2>
      <ul>
        {reports.map((report) => (
          <li key={report._id}>{report.name}</li>
        ))}
      </ul>
    </div>
  );
}

export default Reports;