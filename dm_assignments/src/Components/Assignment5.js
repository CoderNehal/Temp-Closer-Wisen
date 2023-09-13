import React from 'react';
import { useEffect, useState } from 'react';
import axios from "axios"


const Assignment5 = () => {
    const [data, setData] = useState(null);
    const [loading, setLoading] = useState(true);


    
  useEffect(() => {

    axios.get('http://localhost:8000/assignment5')
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
           


   

            




  
        </div>

      ) : (
        <p>No data available.</p>
      )}
    </div>
  )
}

export default Assignment5