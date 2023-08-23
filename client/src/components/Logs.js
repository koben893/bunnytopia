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
            <h1>Top Logs</h1>
            <div className="grid-container">
                {logs.map((log) => (
                    <div key={log.id} className="card">
                        <h3>Log: {log.log}</h3>
                        <p>User: {log.user_name}</p>
                        <p>Bunny: {log.bunny_name}</p>
                        <button className="cardbutton" type="submit">
                            Favorites
                        </button>
                    </div>
                ))}
            </div>
        </div>
    );
}

export default Logs;