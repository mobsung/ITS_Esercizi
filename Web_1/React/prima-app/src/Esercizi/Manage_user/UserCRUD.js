import React from 'react'
import { useState, useRef } from "react";

const UserCRUD = () => {
  const IDRef = useRef(null)
  const nameRef = useRef(null);
  const lastNameRef = useRef(null);
  const mailRef = useRef(null);
  const phoneNumberRef = useRef(null);

  const [persone, setPersone] = useState([]);
  const gestionDati = (e) => {
    e.preventDefault();
    const id = IDRef.current.value;
    const name = nameRef.current.value;
    const lastName = lastNameRef.current.value;
    const mail = mailRef.current.value;
    const phoneNumber = phoneNumberRef.current.value;
    if (id && name && lastName && mail && phoneNumber) {
      setPersone([
        ...persone,
        {
          id,
          name,
          lastName,
          mail,
          phoneNumber
        }
      ]);
    } else {
      alert('compila tutti i campi')
    }
  };
  const rimuoviPersona = (id) => {
    setPersone(persone.filter((p) => p.id !== id));
  };

  return (
    <div className="container mt-5" onSubmit={gestionDati} style={{ backgroundColor: '#f5f7fa', padding: '20px', borderRadius: '10px' }}>
      <div className="row">
        <div className="col-12 col-md-6">
          <form className="p-4 border rounded shadow" style={{ background: 'linear-gradient(to right, #ffffff, #f0f2f5)' }}>
            <div className="form-group">
              <input
                type="text"
                ref={IDRef}
                className="form-control mb-3"
                placeholder="Enter ID"
                style={{ backgroundColor: '#f9f9f9', border: '1px solid #ced4da' }}
              />
            </div>
            <div className="form-group">
              <input
                type="text"
                ref={nameRef}
                className="form-control mb-3"
                placeholder="Enter Name"
                style={{ backgroundColor: '#f9f9f9', border: '1px solid #ced4da' }}
              />
            </div>
            <div className="form-group">
              <input
                type="text"
                ref={lastNameRef}
                className="form-control mb-3"
                placeholder="Enter Last Name"
                style={{ backgroundColor: '#f9f9f9', border: '1px solid #ced4da' }}
              />
            </div>
            <div className="form-group">
              <input
                type="text"
                ref={mailRef}
                className="form-control mb-3"
                placeholder="Enter Email"
                style={{ backgroundColor: '#f9f9f9', border: '1px solid #ced4da' }}
              />
            </div>
            <div className="form-group">
              <input
                type="text"
                ref={phoneNumberRef}
                className="form-control mb-3"
                placeholder="Enter Phone Number"
                style={{ backgroundColor: '#f9f9f9', border: '1px solid #ced4da' }}
              />
            </div>
            <button
              type="submit"
              className="btn w-100"
              style={{
                backgroundColor: '#4dabf7',
                border: 'none',
                color: 'white',
                fontWeight: 'bold'
              }}
            >
              Submit
            </button>
          </form>
        </div>
        <div className="col-12 col-md-6">
          {
            persone.map((p) => {
              return (
                <div key={p.id}
                  className="card mb-3 shadow-sm border-0"
                  style={{
                    background: 'linear-gradient(to right, #fdfdfd, #f0f2f5)',
                    color: '#343a40',
                    borderRadius: "10px"
                  }}>
                  <div className="card-body d-flex justify-content-between align-items-center">
                    <div className="text-muted">
                      <p className="mb-1"><strong style={{ color: '#495057' }}>ID:</strong> {p.id}</p>
                      <p className="mb-1"><strong style={{ color: '#495057' }}>Nome:</strong> {p.name} {p.lastName}</p>
                      <p className="mb-1"><strong style={{ color: '#495057' }}>Email:</strong> {p.mail}</p>
                      <p className="mb-0"><strong style={{ color: '#495057' }}>Telefono:</strong> {p.phoneNumber}</p>
                    </div>
                    <button
                      className="btn btn-sm"
                      onClick={() => rimuoviPersona(p.id)}
                      style={{
                        backgroundColor: '#ff6b6b',
                        color: '#fff',
                        border: 'none',
                        borderRadius: '5px',
                        padding: '5px 10px',
                        fontWeight: 'bold'
                      }}
                    >
                      Remove
                    </button>
                    <button
                      className="btn btn-sm"
                      onClick={() => rimuoviPersona(p.id)}
                      style={{
                        backgroundColor: '#6bff6b',
                        color: '#fff',
                        border: 'none',
                        borderRadius: '5px',
                        padding: '5px 10px',
                        fontWeight: 'bold'
                      }}
                    >
                      Update
                    </button>
                  </div>
                </div>
              )
            })
          }
        </div>
      </div>
    </div>
  );
};

export default UserCRUD;