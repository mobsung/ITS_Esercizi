import React from 'react'
import { useNavigate } from 'react-router-dom'

const ErrorPage = () => {

    const navigate = useNavigate();

    return (
        <div>
            <b>Questa pagina non esiste</b>
            <br /><button className='btn btn-success' onClick={() => navigate('/')}>Torna alla Home</button>
        </div>
    )
}

export default ErrorPage