import React, { useState } from 'react';
import Bunnies from './Bunnies';
import Schedule from './Schedule';
import './Bunnies.css';

function BunnyApp() {
  const [selectedBunnies, setSelectedBunnies] = useState([]);
  const [scheduleBunnies, setScheduleBunnies] = useState([]);


  const handleSelectedBunnyChange = (newSelectedBunnies) => {
    setSelectedBunnies(newSelectedBunnies);
  };
  const setSelectedBunniesInParent = (selectedBunnies) => {
    // Update the schedule state with the selected bunnies
    setScheduleBunnies([...scheduleBunnies, ...selectedBunnies]);
};

  return (
    <div className="bunny-app">
      <Bunnies setSelectedBunnies={handleSelectedBunnyChange} setSelectedBunniesInParent={setSelectedBunniesInParent}/>
      <Schedule selectedBunnies={selectedBunnies} />
    </div>
  );
}

export default BunnyApp;