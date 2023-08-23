import React from 'react';
import { Switch, Route } from 'react-router-dom';
// import Home from './Home'
import Logs from './Reviews'
import Bunnies from "./Bunnies"
import Reviews from './Reviews';
import About from './About'

function PageContainer() {
    return (
        <>
            <Switch>
        <Route path="/logs">
            <Logs />
        </Route>
        <Route path="/bunnies">
            <Bunnies />
        </Route>
        <Route path="/reviews">
            <Reviews />
        </Route>
        {/* <Route path="/">
            <Home />
        </Route> */}
        <Route path="/about">
            <About />
        </Route>
        </Switch>
        
    </>
    );
}

export default PageContainer;