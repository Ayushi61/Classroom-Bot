import React from 'react';
import Navbar from 'react-bootstrap/Navbar';

function TopBar() {

    return (
        <div>
            <Navbar bg="dark" variant="dark" expand="lg">
                <Navbar.Brand href="/">Classroom Slack Bot - Admin</Navbar.Brand>
                <Navbar.Toggle aria-controls="basic-navbar-nav" />
                <Navbar.Collapse id="basic-navbar-nav">
                </Navbar.Collapse>
            </Navbar>
        </div>
    )
}

export default TopBar;