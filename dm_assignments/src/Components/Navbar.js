import React from 'react'
import logo from '../infinity.png'
import './Navbar.css'


const Navbar = () => {
  return (
    <nav className="navbar navbar-expand-lg pt-3 pb-3 bg-dark text-light">
    <a className="navbar-brand" href="/">Rising Apexx</a>
    <button className="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNavDropdown" aria-controls="navbarNavDropdown" aria-expanded="false" aria-label="Toggle navigation">
      <span className="navbar-toggler-icon"></span>
    </button>
    <div className="collapse navbar-collapse" id="navbarNavDropdown">
      <ul className="navbar-nav">
        <li className="nav-item active">
          <a className="nav-link" href="/">Home <span className="sr-only"></span></a>
        </li>
        <li className="nav-item">
          <a className="nav-link" href="/file_upload">File Upload</a>
        </li>
        <li className="nav-item">
          <a className="nav-link" href="/assignment_1">Assignment1</a>
        </li>
        <li className="nav-item">
          <a className="nav-link" href="/assignment_2">Assignment2</a>
        </li>
        <li className="nav-item">
          <a className="nav-link" href="/assignment_3">Assignment3</a>
        </li>
        <li className="nav-item">
          <a className="nav-link" href="/assignment_4">Assignment4</a>
        </li>
        <li className="nav-item">
          <a className="nav-link" href="/assignment5">Assignment5</a>
        </li>
      </ul>
    </div>
  </nav>
  )
}

export default Navbar