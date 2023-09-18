import React, { useState } from 'react';
import Bunnies from './Bunnies';
import Schedule from './Schedule';
import './Bunnies.css';

function BunnyApp() {
  const [selectedBunnies, setSelectedBunnies] = useState([]);

  const handleSelectedBunnyChange = (newSelectedBunnies) => {
    setSelectedBunnies(newSelectedBunnies);
  };

  return (
    <div className="bunny-app">
      <Bunnies setSelectedBunnies={handleSelectedBunnyChange} />
      <Schedule selectedBunnies={selectedBunnies} />
    </div>
  );
}

export default BunnyApp;