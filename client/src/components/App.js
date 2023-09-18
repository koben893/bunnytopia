import React, { useState, useEffect } from 'react';
import '../App.css';
import Header from "./Header"
import PageContainer from "./PageContainer"
import '../darkMode.css';



function App() {
  const [user, setUser] = useState(null);
  const handleUser = (user) => setUser(user);

  useEffect(()=>{
    fetch('/check_session').then((res) => {
      if (res.ok) {
        res.json().then((userObj) => setUser(userObj));
      }
    })
  }, [setUser])
  
  return (
    <div className="App">
      <header className="App-header">
        <Header user={user} handleUser={handleUser}/>
      </header>
      <PageContainer user={user} handleUser={handleUser}/>
    </div>
  );
}
export default App;
