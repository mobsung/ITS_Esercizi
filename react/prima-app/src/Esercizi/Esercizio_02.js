import React from 'react'

const Tabellina = (props) => {

    const numeri = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10];
    return(

    numeri.map((numero) => {
        
        return <span key={numero}>{numero * parseInt(props.moltiplicatore)} </span>

    })
)
}

export default Tabellina


{/* <h1>TEST ESERCIZIO 2</h1>
<h1><Tabellina moltiplicatore='5'></Tabellina></h1> */}