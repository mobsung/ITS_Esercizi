
import { useState, useEffect } from "react"

const usersUrl = 'https://jsonplaceholder.typicode.com/users';

const UserCrud = () => {
    const [users, setUsers] = useState([]);

    const getUsers = () => {
        fetch(usersUrl).then(response => response.json()).then(ris => setUsers(ris))
    };

    useEffect(() => {
        getUsers()
    }, []);

    const deleteUser = (id) => {
        const newUsers = users.filter((u) => u.id !== id);
        if(window.confirm('Sei sicuro di voler cancellare')){
            setUsers(newUsers);
        }
    };

    return (
        <>
            <div className="container">
                <h1>USER CRUD</h1>
                <div>
                    {users.map((u) => {
                        return (
                            <div className="row my-1 border">
                                <div className="col-8 p-2 d-flex justify-content-start">{u.name}</div>
                                <div className="col-4 p-2 d-flex justify-content-end">
                                    <button className="btn btn-primary">Update</button>
                                    <button className="btn btn-danger" onClick={() => {deleteUser(u.id)}}>Delete</button>
                                </div>
                            </div>
                        );
                    })}
                </div>
            </div>
        </>
    )
}

export default UserCrud