import { useState } from "react"
import { UserContext } from "./UserContext"

/* La diferencia entre un componente y un HOC, es que en los props se reciben los children */
/* El hola mundo es todo lo que cada hijo podrá obtener del contexto */
export const UserProvider = ({ children }) => {
  const [user, setUser] = useState()
  return (
    <>
      <UserContext.Provider value={{ user, setUser }}>
        {children}
      </UserContext.Provider>
    </>
  )
}
