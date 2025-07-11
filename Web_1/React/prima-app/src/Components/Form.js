import React from 'react'

const Form = () => {
  return (
    <div className="container">
      <form className="row g-3">
        <div className="col-md-6">
          <label htmlFor="inputNome" className="form-label">Nome</label>
          <input type="text" className="form-control" id="inputNome" />
        </div>
        <div className="col-md-6">
          <label htmlFor="inputCognome" className="form-label">Cognome</label>
          <input type="text" className="form-control" id="inputCognome" />
        </div>
        <div className="col-12">
          <button type="submit" className="btn btn-primary">Invia</button>
        </div>
      </form>
    </div>
  )
}

export default Form