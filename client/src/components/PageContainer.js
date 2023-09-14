import React from 'react';
import { Switch, Route } from 'react-router-dom';
import Logs from './Logs'
import BunnyApp from "./BunnyApp"
import Reviews from './Reviews';
import Login from './Login'
import Schedule from './Schedule';
import Signup from './Signup'

function PageContainer({ user, handleUser }) {


    return (
        <>
            <Switch>
                <Route path="/logs">
                <Logs user={user} handleUser={handleUser}/>
                </Route>

                <Route path="/bunnies">
                <BunnyApp user={user} handleUser={handleUser}/>
                </Route>

                <Route path="/reviews">
                <Reviews user={user} handleUser={handleUser}/>
                </Route>

                <Route path="/login">
                <Login user={user} handleUser={handleUser}/>
                </Route>

                <Route path="/schedule">
                <Schedule user={user} handleUser={handleUser}/>
                </Route>

                <Route path="/signup">
                <Signup user={user} handleUser={handleUser}/>
                </Route>
            </Switch>
        </>
    );
}

export default PageContainer;