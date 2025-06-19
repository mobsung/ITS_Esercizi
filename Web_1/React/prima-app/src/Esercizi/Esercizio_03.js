import React from 'react'

const Stampanumeri = () => {
    const numeri = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10];
    return(

    numeri.map((numero) => {

        return <span key={numero}>{numero}, </span>

    })
)
}

export default Stampanumeri


{/* <h1>TEST ESERCIZIO 3</h1>
<h1><Stampanumeri></Stampanumeri></h1> */}

