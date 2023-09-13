import React from 'react'
import { useEffect, useState } from 'react';
import axios from "axios"
import { Scatter } from 'react-chartjs-2';


const Assignment2 = () => {

    const [data, setData] = useState(null);
    const [loading, setLoading] = useState(true);


    
  useEffect(() => {
    axios.get('http://localhost:8000/assignment2')
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
        <>
        <p>Loading...</p>
        </>
      ) : data ? (
        <div className="container mt-5">
          
          
            <h1><u>Name Of File :{data.name}</u></h1>
            <h2>result: {data.result}</h2>
            <h2>p: {data.p}</h2>
            <h2>chi2: {data.chi2}</h2>
            <h2>dof: {data.dof}</h2>




        
        </div>

      ) : (
        <p>No data available.</p>
      )}
    </div>
  )
}

export default Assignment2