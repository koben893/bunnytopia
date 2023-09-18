import React, { useEffect,useState } from "react";
import NewBunnyForm from "./NewBunnyForm";
import './Bunnies.css';


function Bunnies({ setSelectedBunnies }) {

    const [bunnies, setBunnies] = useState([]);
    const [selectedBunnies, updateSelectedBunnies] = useState([]); // Change the state variable name

    const addBunnyToState = NewBunnyObj => {
        setBunnies([...bunnies, NewBunnyObj]);
    }

    useEffect(() => {
        fetch('http://127.0.0.1:5557/bunnies')
            .then((response) => response.json())
            .then((data) => setBunnies(data));
    }, []);

    const handleSlaughter = (bunnyId) => {
        fetch(`http://127.0.0.1:5557/bunnies/${bunnyId}`, {
            method: 'DELETE',
        })
        .then((response) => {
            if (response.ok) {
                // Remove the bunny from the state
                setBunnies(bunnies.filter((bunny) => bunny.id !== bunnyId));
            }
        })
        .catch((error) => {
            console.error('Error deleting bunny:', error);
        });
    };

    const handleBreedClick = (bunnyId) => {
        updateSelectedBunnies((prevSelectedBunnies) => [...prevSelectedBunnies, bunnyId]);
    };

    useEffect(() => {
        // Use the prop function directly here
        setSelectedBunnies(selectedBunnies);
    }, [selectedBunnies, setSelectedBunnies]);

    const sendSelectedBunniesToBackend = () => {
        fetch("/breeding", {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify(selectedBunnies),
        })
        .then((response) => {
            if (response.ok) {
                setSelectedBunnies([]);
            } else {
                console.error("Failed to send selected bunnies to the backend.");
            }
        })
        .catch((error) => {
            console.error("Error sending selected bunnies:", error);
        });
    };

    return (
        <div className="header">
            <h1 className="center">Your Bun Buns</h1>
            <NewBunnyForm addBunnyToState={addBunnyToState}/>
            <div className="grid-container">
                {bunnies.map((bunny) => (
                    <div key={bunny.id} className="card">
                        <h1>
                            {bunny.logs}
                        </h1>
                        <h3>{bunny.name}</h3>
                        <button className="cardbutton" onClick={() => handleBreedClick(bunny)}>Ready to Breed</button>
                        <button className="cardbutton" onClick={() => handleSlaughter(bunny.id)}>Harvest</button>
                    </div>
                ))}
            </div>
            <button className="submit-button" onClick={sendSelectedBunniesToBackend}>Submit</button>
        </div>
    )
}



export default Bunnies;