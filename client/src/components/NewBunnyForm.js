import React, { useState } from "react";
import "./Bunnies.css"

function NewBunnyForm({ addBunnyToState }) {
    const [name, setName] = useState("");
    const [log, setLog] = useState("");

    const handleNameChange = (event) => {
    setName(event.target.value);
    };

    const handleLogChange = (event) => {
    setLog(event.target.value);
    };

    const handleSubmit = async (event) => {
    event.preventDefault();
    

    if (!name || isNaN(log) || log < 1 || log > 1825) {
        alert("Rabbit must be between 1 day and 1825 dys old");
        return;
    }

    const newBunny = {
        name: name,
        log: parseInt(log),
    };

    // Call the function provided by the parent component to add the bunny
    addBunnyToState(newBunny);

    // Reset form fields
    setName("");
    setLog("");
    };

    return (
    <div className="new-bunny-form">
        <h2>Add a New Bunny</h2>
        <form onSubmit={handleSubmit}>
        <input
            type="text"
            placeholder="Bunny Name"
            value={name}
            onChange={handleNameChange}
        />
        <input
            type="number"
            placeholder="Age in days"
            value={log}
            onChange={handleLogChange}
        />
        <button type="submit">Add Bunny</button>
        </form>
        <p></p>
    </div>
    );
}

export default NewBunnyForm;