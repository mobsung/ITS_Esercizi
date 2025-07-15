import React from 'react'
import { useState } from 'react'

const Hidden = () => {
    const [show, setShow] = useState(false)

  return (
    <>
    {show && <Elemento></Elemento>}
    <button onClick={() => setShow(!show)}>{show ? 'Hide': 'Show'}</button>
    </>
  )
}

const Elemento = () => {
    return <h2>Elemento</h2>
}

export default Hidden