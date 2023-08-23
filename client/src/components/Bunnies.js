import React, { useEffect,useState } from "react";
import NewBunnyForm from "./NewBunnyForm";
import './Bunnies.css';


function Bunnies() {

    const [bunnies, setBunnies] = useState([])
    const addBunnyToState = NewBunnyObj =>{
        setBunnies( [...bunnies, NewBunnyObj])
    }

        useEffect(() => {
            fetch('http://127.0.0.1:5557/bunnies')
                .then((response) => response.json())
                .then((data) => setBunnies(data));
        }, []);

        return (
            <div className="header">
                <h1 className="center">Your bun buns</h1>
                <NewBunnyForm addBunnyToState={addBunnyToState}/>
                <div className="grid-container">
                    {bunnies.map((bunny) => (
                        <div key={bunny.id} className="card">
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



export default Bunnies;