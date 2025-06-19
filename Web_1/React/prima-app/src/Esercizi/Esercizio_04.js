import React from 'react'

const StampanumeriPari = () => {
    const numeri = []
    for(let i = 0; i <= 20; i+=2){

       numeri.push(i)
    }

    return(
        numeri.map((numero) => {
            return <span key={numero}>{numero}, </span>
        })
    ) 
}

export default StampanumeriPari


{/* <h1>TEST ESERCIZIO 4</h1>
<h1><StampanumeriPari></StampanumeriPari></h1> */}