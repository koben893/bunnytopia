import React, { useEffect, useState } from 'react';
import './Bunnies.css';

function Schedule({selectedBunnies}) {
    const [scheduledBunnies, setScheduledBunnies] = useState([]);

    useEffect(() => {
        // Fetch the scheduled bunnies from the server when the component mounts
        fetch("/breeding")
            .then((response) => response.json())
            .then((data) => setScheduledBunnies(data))
            .catch((error) => {
                console.error("Error getting scheduled bunnies:", error);
            });
    }, []);

    return (
        <div className="header">
            <h1 className="center">Scheduled Bunnies for Breeding:</h1>
            <div className="grid-container">
                {scheduledBunnies.map((entry) => (
                    <div key={entry.id} className="card">
                        <h1>{entry.user.username}</h1>
                        <h3>{entry.bunny.name}</h3>
                        {/* Add other bunny and user attributes as needed */}
                    </div>
                ))}
            </div>
        </div>
    );
}

export default Schedule;