import React, { useState, useEffect } from 'react'
import axios from 'axios'

const url = 'https://jsonplaceholder.typicode.com/users'

const RenderCondizionale = () => {

    const [isLoading, setIsLoading] = useState(true);
    const [isError, setIsError] = useState(true);
    const [users, setusers] = useState([]);

    const getData = async () => {
        setIsError(false);
        setIsLoading(true);
        try {
            const response = await axios.get(url);
            setusers(response.data);
        } catch (err) {
            console.log(err)
            setIsError(true);
        }
        setIsLoading(false);
    };

    useEffect(() => {
        getData();
    },[])

    if (isLoading) {
        return <Loading></Loading>
    };

    if (isError) {
        return <h3>Si è verificato un'errore</h3>
    };

    return <ul>
        {
            users.map((u) => {
                const {id,name,username,email} = u
                return(
                    <li key={id}>
                        <div>
                            <h5>{id} - {name} - {username} - {email}</h5>
                        </div>
                    </li>
                )
            })
        }
    </ul>;
}

const Loading = () => {
    return (<h2>Loading...</h2>)
}

export default RenderCondizionale