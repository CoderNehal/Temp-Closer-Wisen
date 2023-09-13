import React from 'react'
import { useEffect, useState } from 'react';
import axios from "axios"
import image from 'file:///C:/Users/Saurabh/Desktop/DM%20assignments/dm_assignments/backend/static/plot/image.png'


const Assignment3 = () => {
    const [data, setData] = useState(null);
    const [loading, setLoading] = useState(true);


    
  useEffect(() => {

    console.log("calling.....")
    axios.get('http://localhost:8000/assignment3')
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
            <h2>data: {data.text}</h2>
   
            <img src={image} alt="no_image">

            </img>
            




        
        </div>

      ) : (
        <p>No data available.</p>
      )}
    </div>
  )
}

export default Assignment3