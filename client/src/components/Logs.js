import React, { useEffect, useState } from "react";

function Logs({ user, onLogin }) {
    const [logs, setLogs] = useState([]);

    useEffect(() => {
        fetch("http://127.0.0.1:5557/logs")
            .then((response) => response.json())
            .then((data) => {
                console.log(data); // Check the response data in the console
                setLogs(data);
            })
            .catch((error) => {
                console.error("Error fetching logs:", error);
            });
    }, []);
    console.log(logs);
    return (
        <div className="header">
            <h1>Rabbit Logs</h1>
            <div className="grid-container">
                {logs.map((log) => (
                    <div key={log.id} className="card">
                        <h3>Bunny Name: {log.bunny_name}</h3>
                        <p>Owner: {log.user_name}</p>
                        <p>Age: {log.log}</p>
                        <button className="cardbutton" type="submit">
                            Favorite
                        </button>
                    </div>
                ))}
            </div>
        </div>
    );
}

export default Logs;