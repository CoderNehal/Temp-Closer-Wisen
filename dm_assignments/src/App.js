// src/App.js
import React from 'react';
import './App.css';
import HomePage from './Components/Home';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import Navbar from './Components/Navbar';
import Assignment1 from './Components/Assignment1';
import FileUpload from './Components/FileUpload';
import CSVUploader from './Components/CSVUploader';
import Assignment2 from './Components/Assignment2';
import Assignment3 from './Components/Assignment3';
import Assignment4 from './Components/Assignment4';
import Assignment5 from './Components/Assignment5';
import Footer from './Components/Footer';


function App() {
  return (
    <Router>
      <Navbar/>
      <Routes>
        <Route path="/" exact element={<HomePage/>} />
        <Route path="/file_upload" exact element={<FileUpload/>} />
        <Route path="/csv_upload" exact element={<CSVUploader/>} />
        <Route path="/assignment_1" exact element={<Assignment1/>} />
        <Route path="/assignment_2" exact element={<Assignment2/>} />
        {/* <Route path="/assignment_3" exact element={<Assignment3/>} /> */}
        <Route path="/assignment_4" exact element={<Assignment4/>} />
        <Route path="/assignment_5" exact element={<Assignment5/>} />


      </Routes>
      <Footer/>
    </Router>
  );
}

export default App;