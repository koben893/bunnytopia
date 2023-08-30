import React from 'react';
import { Switch, Route } from 'react-router-dom';
// import Home from './Home'
import Logs from './Logs'
import Bunnies from "./Bunnies"
import Reviews from './Reviews';
import Login from './Login'

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

                <Route path="/login">
                <Login />
                </Route>
            </Switch>
        </>
    );
}

export default PageContainer;