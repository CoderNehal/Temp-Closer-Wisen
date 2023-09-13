import axios from "axios"
import React, { useEffect, useState } from 'react';


const Assignment1 = () => {

    const [data, setData] = useState(null);
    const [loading, setLoading] = useState(true);

    
  useEffect(() => {
    axios.get('http://localhost:8000/assignment1')
      .then((response) => {
        setData(response.data);
        setLoading(false);
      })
      .catch((error) => {
        console.error('Axios error:', error);
        setLoading(false);
      });
  }, []);

  return (
    <div>
      {loading ? (
        <p>Loading...</p>
      ) : data ? (
        <div className="container mt-5">
          
           <h1><u>Name Of File :{data.name}</u></h1>
            <h2>Mean: {data.mean}</h2>
            <h2>Median: {data.median}</h2>
            <h2>Mode: {data.mode}</h2>
            <h2>Variance: {data.variance}</h2>
            <h2>Standard deviation: {data.std}</h2>




        
        </div>
      ) : (
        <p>No data available.</p>
      )}
    </div>
    
  )
}

export default Assignment1