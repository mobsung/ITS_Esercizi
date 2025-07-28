import { useState, useEffect } from 'react'
import React from 'react'
import axios from 'axios';



const users_url = 'https://jsonplaceholder.typicode.com/users'



const UserAlbums = () => {

    const [isLoading, setIsLoading] = useState(true);
    const [isError, setIsError] = useState(true);
    const [users, setusers] = useState([]);
    const [selectedUser, setSelectedUser] = useState();

    const [albumIsLoading, setAlbumIsLoading] = useState(true);
    const [AlbumsError, setAlbumsIsError] = useState(true);
    const [albums, setAlbums] = useState([]);
    const [selectedAlbum, setSelectedAlbum] = useState();


    const getUsersData = async () => {
        setIsError(false);
        setIsLoading(true);
        try {
            const response = await axios.get(users_url);
            setusers(response.data);
        } catch (err) {
            console.log(err)
            setIsError(true);
        }
        setIsLoading(false);
    };

    const getAlbumsData = async () => {
        setAlbumsIsError(false);
        setAlbumIsLoading(true);
        try {
            const response = await axios.get(albums_url);
            setAlbums(response.data)
        } catch (err) {
            console.log(err);
            setAlbumsIsError(true);
        }
        setAlbumIsLoading(false);
    };

    useEffect(() => {
        getUsersData();
    }, []);

    useEffect(() => {
        const albums_url = 'https://jsonplaceholder.typicode.com/albums?userId='+{selectedUser}
        getAlbumsData();
    }, [selectedUser]);


    if (isLoading || albumIsLoading) {
        return <Loading></Loading>
    };

    if (isError || AlbumsError) {
        return <h3>Si è verificato un'errore</h3>
    };

    const handleUsersChange = (e) => {
        setSelectedUser(e.target.value);
    };

    const handleAlbumsChange = (e) => {
        setSelectedAlbum(e.target.value);
    };

    return (
        <>
            <div className="container">
                <div className="row">
                    <div className="col">
                        <select value={selectedUser} onChange={handleUsersChange}>
                            <option value="">Seleziona utente</option>
                            {users.map((user) => {
                                const { id, name, username, email } = user;
                                return (
                                    <option key={id} value={id}>
                                        {id} - {name} - {username}
                                    </option>
                                );
                            })}
                        </select>
                        <select value={selectedAlbum} onChange={handleAlbumsChange}>
                            <option value=''>Seleziona album</option>
                            {albums.map((album) => {
                                const { userId, id, title } = album;
                                return (
                                    <option key={id} value={id}>
                                        {title}
                                    </option>
                                );
                            })}
                        </select>
                    </div>
                </div>
            </div>
        </>
    );

}

const Loading = () => {
    return (<h2>Loading...</h2>)
}
export default UserAlbums