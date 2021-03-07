import React, { Component } from 'react';

class NavBar extends Component {
    state = {  }
    render() { 
        return (     
        <nav className="navbar navbar-expand-lg navbar-dark bg-dark">
            <a className="navbar-brand" href="#">StudyTimeBoard
                <div style={{color:"gray", fontSize: "50%"}}>(Beta v0.5.0)</div>
            </a>

            <button className="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNavAltMarkup"
                aria-controls="navbarNavAltMarkup" aria-expanded="false" aria-label="Toggle navigation">
                <span className="navbar-toggler-icon"></span>
            </button>
            
            <div className="collapse navbar-collapse" id="navbarNavAltMarkup">
                <div className="navbar-nav mr-auto">
                    <a className="nav-link" href="/" id="nav-home">Home</a>
                    <a className="nav-link" href="/" id="nav-personal-analysis">Personal Analysis</a>
                    <a className="nav-link" href="/" id="nav-leaderboard">Leaderboard</a>
                    <a className="nav-link" href="/" id="nav-about">About</a>
                </div>
                <div className="navbar-nav">
                    <a className="nav-item nav-link" href="/">Login</a>
                    <a className="nav-item nav-link" href="/">Register</a>
            </div>
            </div>
        </nav>);
    }
}
 
export default NavBar;