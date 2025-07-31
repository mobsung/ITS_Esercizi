import { useEffect, useState } from "react";

// json-server --watch db.json --port 3100
const urlUser = "/api/users";
const UserCrud = () => {
    const [users, setUsers] = useState([]);


    const getUsers = () => {
        fetch(urlUser)
            .then((response) => response.json())
            .then((ris) => setUsers(ris));
    };
    useEffect(() => {
        getUsers();
    }, []);


    const deleteUser = async (id) => {
        //const newUsers = users.filter((u) => u.id !== id);
        if (window.confirm("Sei sicuro di voler cancellare questo utente?")) {
            //setUsers(newUsers);
            try {
                const response = await fetch(urlUser + '/' + id, {
                    method: 'DELETE'
                });
                if (!response.ok) throw new Error('Si è verificato un errore durante la richiesta di cancellazione')
                getUsers();
            } catch (err) {
                console.log(err);
            }
        }
    };


    return (
        <>
            <div className="container">
                <h1>USER CRUD</h1>

                <div className="card shado-sm mb-4">
                    <div className="card-body">
                        <h2 className="card-title mb-4">Gestione utente</h2>
                        <form >

                            <div className="row g-3 mb-3">
                                <div className="col-md-6">
                                    <label htmlFor="nome" className="form-label fw-bold">Nome *</label>
                                    <input
                                        type="text"
                                        id="nome"
                                        name="nome"
                                        className="form-control"

                                        required
                                    />
                                </div>
                                <div className="col-md-6">
                                    <label htmlFor="cognome" className="form-label fw-bold">Cognome *</label>
                                    <input
                                        type="text"
                                        id="cognome"
                                        name="cognome"
                                        className="form-control"

                                        required
                                    />
                                </div>
                            </div>
                            <div className="row g-3 mb-4">
                                <div className="col-md-6">
                                    <label htmlFor="telefono" className="form-label fw-bold">Telefono</label>
                                    <input
                                        type="tel"
                                        id="telefono"
                                        name="telefono"
                                        className="form-control"

                                    />
                                </div>
                                <div className="col-md-6">
                                    <label htmlFor="email" className="form-label fw-bold">Email *</label>
                                    <input
                                        type="email"
                                        id="email"
                                        name="email"
                                        className="form-control"

                                        required
                                    />
                                </div>
                            </div>


                            <div className="d-flex gap-2">
                                <button type="submit" className="btn btn-primary">
                                    Salva dati
                                </button>


                            </div>
                        </form>
                    </div>
                </div>

                <div class="mb-3 row">
                    <label htmlfor="staticEmail" className="col-sm-2 col-form-label">
                        Email
                    </label>
                    <div className="col-sm-10">
                        <input
                            type="text"
                            readonly
                            className="form-control-plaintext"
                            id="staticEmail"
                            value="email@example.com"
                        ></input>
                    </div>
                </div>
                <div className="mb-3 row">
                    <label htmlfor="inputPassword" className="col-sm-2 col-form-label">
                        Password
                    </label>
                    <div className="col-sm-10">
                        <input
                            type="password"
                            className="form-control"
                            id="inputPassword"
                        ></input>
                    </div>
                </div>


                <div className="row">
                    <div className="col-8 p-2 d-flex justify-content-start bg-secondary text-white">
                        Utente
                    </div>
                    <div className="col-4 p-2 d-flex justify-content-end bg-secondary text-white">
                        Azioni
                    </div>
                </div>
                <div>
                    {users.map((u) => {
                        return (
                            <div className="row my-1 border">
                                <div className="col-8 p-2 d-flex justify-content-start">
                                    {u.name}
                                </div>
                                <div className="col-4 p-2 d-flex justify-content-end gap-2">
                                    <button className="btn btn-primary">Update</button>
                                    <button
                                        className="btn btn-danger"
                                        onClick={() => {
                                            deleteUser(u.id);
                                        }}
                                    >
                                        Delete
                                    </button>
                                </div>
                            </div>
                        );
                    })}
                </div>
            </div>
        </>
    );
};


export default UserCrud;
