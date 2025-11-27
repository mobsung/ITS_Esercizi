import React from 'react'
import { BrowserRouter, Routes, Route, Link } from 'react-router-dom';
import Home from './Home';
import About from './About';
import Profile from './Profile';
import ErrorPage from './ErrorPage';
import SingleProfile from './SingleProfile';
import MyProfile from './MyProfile';

const ProvaRoutes = () => {

    // const [link, setLink] = useState('Home')

    // const RenderComponent = () => {
    //     if (link === 'Home') {
    //         return <Home />;
    //     }
    //     if (link === 'About') {
    //         return <About />;
    //     }
    //     if (link === 'Profile') {
    //         return <Profile />;
    //     }
    // };

    return (
        <>
            <BrowserRouter>
                <nav className="navbar bg-body-tertiary">
                    <div className="container-fluid">
                        <Link to="/">Home</Link>
                        <Link to="/about">About</Link>
                        <Link to="/profile">Profile</Link>
                    </div>
                </nav>
                <Routes>
                    <Route path="/" element={<Home/>}></Route>
                    <Route path="/about" element={<About/>}></Route>
                    <Route path="/profile/" element={<Profile/>}>
                        <Route path=":id" element={<SingleProfile/>}></Route>
                        <Route path="me" element={<MyProfile/>}></Route>
                    </Route>
                    <Route path="*" element={<ErrorPage/>}></Route>
                </Routes>
            </BrowserRouter>

            {/* <nav className="navbar bg-body-tertiary">
                <div className="container-fluid">
                    <button className="btn btn-link nav-link" onClick={() => setLink("Home")}>
                        <link to='/'></link>
                        Home
                    </button>
                    <button className="btn btn-link nav-link" onClick={() => setLink("About")}>
                        <link to='/about'></link>
                        About
                    </button>
                    <button className="btn btn-link nav-link" onClick={() => setLink("Profile")}>
                        <link to='/profile'></link>
                        Profile
                    </button>
                </div>
            </nav>
            <div className='container'>
                <b>{RenderComponent()}</b>
            </div> */}
        </>
    )
}

export default ProvaRoutes