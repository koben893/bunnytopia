import React from "react";
import { NavLink, useHistory } from "react-router-dom";

const linkStyles = {
  display: "inline-block",
  width: "300px",
  padding: "12px",
  margin: "0 18px 6px",
  background: "black",
  textDecoration: "none",
  color: "orange",
};

function NavBar({ user, handleUser }) {

  const history = useHistory()
  const handleLogout = () => {
    fetch('/logout', {
      method : "DELETE",
    }).then(() => {
      handleUser(null);
      history.push('/')
    })
  }

  function handleLogin(){
    history.push('/login', {from:history.location.pathname})
  }
  function handleSignup(){
    history.push('/signup', {from:history.location.pathname})
  }

  return (
    <div>
      <NavLink
        className="nav-buttons"
        to="/login"
        exact
        style={linkStyles}
      >
        Login
      </NavLink>

      <NavLink
        className="nav-buttons"
        to="/bunnies"
        exact
        style={linkStyles}
      >
        Bunnies
      </NavLink>

      <NavLink
        className="nav-buttons"
        to="/schedule"
        exact
        style={linkStyles}
      >
        Schedule
      </NavLink>

      <NavLink
        to="/reviews"
        className="nav-buttons"
        exact
        style={linkStyles}
      >
        Reviews
      </NavLink>

      <NavLink
        to="/logs"
        className="nav-buttons"
        exact
        style={linkStyles}
      >
        Logs
      </NavLink>
      
      <NavLink
        to="/signup"
        className="nav-buttons"
        exact
        style={linkStyles}
      >
        Signup
      </NavLink>
    </div>
  );
}

export default NavBar;