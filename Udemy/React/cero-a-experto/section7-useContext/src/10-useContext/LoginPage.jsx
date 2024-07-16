import { useContext } from "react"
import { UserContext } from './context/UserContext'
/* Si se tienen varios contextos con el mismo nombre, useContext traerá el contexto superior más cercano */
export const LoginPage = () => {
  const { user, setUser } = useContext(UserContext);
  return (
    <>
      <h1>LoginPage</h1>
      <hr />
      <pre>
        {JSON.stringify(user, null, 3)}
      </pre>
      <button className="btn btn-primary" onClick={() => setUser({ id: 123, name: "Alvaro Garzón", email: "eduardo831_@hotmail.com" })}>
        Establecer usuario
      </button>
    </>
  )
}
