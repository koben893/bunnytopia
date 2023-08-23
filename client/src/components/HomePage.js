import React, { useEffect, useState } from "react";

function HomePage({user, onLogin}) {
    
        const [bunnies, setBunnies] = useState([])
    
    useEffect(() => {
        fetch('http://127.0.0.1:5557/bunnies')
            .then((response) => response.json())
            .then((data) => setBunnies(data));
    }, []);
    
    return (
        <div className="header">
            <h1 className="center">Your Bun Buns</h1>
            <div className="grid-container">
                {bunnies.map((bunny) => (
                    <div key={bunny.id} className="card">
                        <img>{bunny.image}</img>
                        <h1>
                            {bunny.logs}
                        </h1>
                        <h3>{bunny.name}</h3>
                        <button className="cardbutton" type="submit">Favorites</button>
                    </div>
                ))}
            </div>
        </div>
        )
    }


export default HomePage;