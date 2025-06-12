const elementRoot=document.querySelector("#root");
const root=ReactDOM.createRoot(elementRoot);

const App = ({children}) => {
    return(
        <main>
            <h1>Il primo componente</h1>
            {children}
        </main>
    )

}

const List = () => {
    return(

        <ul>
            <li>PHP</li>
            <li>WEP</li>
            <li>PYTHON</li>
        </ul>
    )

}

root.render(
    <>
        <App>
            <h2>Lista Competenze</h2>
            <List/>
        </App>
    </>
)