import React from 'react'

const UserForm = () => {

  return (
    <div className="d-flex justify-content-center align-items-center vh-100">
      <form className="p-4 border rounded" style={{ minWidth: '300px' }}>
        <div className="form-group">
          <input
            type="text"
            className="form-control mb-3"
            id="inputName"
            placeholder="Enter Name"
          />
        </div>
        <div className="form-group">
          <input
            type="text"
            className="form-control mb-3"
            id="inputLastName"
            placeholder="Enter Last Name"
          />
        </div>
        <div className="form-group">
          <input
            type="email"
            className="form-control mb-3"
            id="inputEmail1"
            placeholder="Enter Email"
          />
        </div>
        <div className="form-group">
          <input
            type="tel"
            className="form-control mb-3"
            id="inputPhoneNumber"
            placeholder="Enter Phone Number"
          />
        </div>
        <button type="submit" className="btn btn-primary w-100">
          Submit
        </button>
      </form>
    </div>
  );
};

export default UserForm;