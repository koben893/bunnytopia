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
                .then((data) => setRestaurants(data));
        }, []);

        return (
            <div className="header">
                <h1 className="center">Top Rated Restaurants</h1>
                <NewBunnyForm addRestaurantToState={addRestaruantToState}/>
                <div className="grid-container">
                    {restaurants.map((restaurant) => (
                        <div key={restaurant.id} className="card">
                            <h1>
                                {restaurant.ratings}
                            </h1>
                            <h3>{restaurant.name}</h3>

                            <button className="cardbutton" type="submit">Favorites</button>
                        </div>
                    ))}
                </div>
            </div>
            )
        }



export default Bunnies;