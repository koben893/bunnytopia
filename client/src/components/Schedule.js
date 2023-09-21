import React, { useEffect, useState } from 'react';
import './Bunnies.css';

function Schedule({selectedBunnies}) {
    const [scheduledBunnies, setScheduledBunnies] = useState([]); // Change the state variable name

    useEffect(() => {
        fetch("/breeding")
            .then((response) => response.json())
            .then((data) => setScheduledBunnies(data))
        .catch((error) => {
            console.error("Error getting bunny:", error);
        });
    }, []);

    return (
        <div className="header">
            <h1 className="center">Selected Bunnies for Breeding:</h1>
            <div className="grid-container">
                {selectedBunnies?.map((bunny) => (
                    <div key={bunny.id} className="card">
                    <h1>{bunny.logs}</h1>
                    <h3>{bunny.name}</h3>
                    </div>
                ))}
            </div>
        </div>
    );
}

export default Schedule;