import React from 'react';
import './Bunnies.css';

function Schedule({ selectedBunnies }) {
    return (
        <div className="header">
            <h1 className="center">Selected Bunnies for Breeding:</h1>
            <div className="grid-container">
            {selectedBunnies.map((bunnyId) => (
                <div key={bunnyId.id} className="card">
                <h1>
                {bunnyId.logs}
                </h1>
                <h3>{bunnyId.name}</h3>
            </div>
            ))}
            </div>
        </div>
    );
}

export default Schedule;