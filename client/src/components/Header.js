import React from 'react'
import NavBar from './NavBar'
import DarkMode from './DarkMode';

function Header({user, onLogin, handleUser}) {
    return (
        <div>
            <DarkMode />
            <div>
                <img className='banner-img' src="https://images-wixmp-ed30a86b8c4ca887773594c2.wixmp.com/f/ebe3ea08-6d15-4b56-a300-abd30049dcbe/dfxyilh-e0c58ef0-afd2-4af5-8066-a45109c939a0.jpg/v1/fill/w_1280,h_536,q_75,strp/256bec45_9788_49ea_ae4d_1db0d554ef1d_by_log14_dfxyilh-fullview.jpg?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ1cm46YXBwOjdlMGQxODg5ODIyNjQzNzNhNWYwZDQxNWVhMGQyNmUwIiwiaXNzIjoidXJuOmFwcDo3ZTBkMTg4OTgyMjY0MzczYTVmMGQ0MTVlYTBkMjZlMCIsIm9iaiI6W1t7ImhlaWdodCI6Ijw9NTM2IiwicGF0aCI6IlwvZlwvZWJlM2VhMDgtNmQxNS00YjU2LWEzMDAtYWJkMzAwNDlkY2JlXC9kZnh5aWxoLWUwYzU4ZWYwLWFmZDItNGFmNS04MDY2LWE0NTEwOWM5MzlhMC5qcGciLCJ3aWR0aCI6Ijw9MTI4MCJ9XV0sImF1ZCI6WyJ1cm46c2VydmljZTppbWFnZS5vcGVyYXRpb25zIl19.gKWfc5d-q61fmakh4ApGZdfy4BBmTl0jjf0gVOzQ33Y" alt='' /> <br />
            </div>
            <NavBar user={user} handleUser={handleUser}/>
        </div>
    );
}

export default Header;