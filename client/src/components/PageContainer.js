import React from 'react';
import { Switch, Route } from 'react-router-dom';
import Logs from './Logs'
import BunnyApp from "./BunnyApp"
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
                <BunnyApp />
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