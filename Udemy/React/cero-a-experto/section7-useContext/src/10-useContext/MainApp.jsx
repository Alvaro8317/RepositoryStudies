import { Routes, Route, Navigate } from 'react-router-dom'
import { HomePage } from './HomePage'
import { AboutPage } from './AboutPage'
import { LoginPage } from './LoginPage'
import { NavBar } from './NavBar'
import { UserProvider } from './context/UserProvider'
export const MainApp = () => {
  return (
    <UserProvider>
      {/* A partir de aquí, cualquier elemento podrá obtener los datos del contexto */}
      <h1>MainApp</h1>
      <NavBar />
      <hr />
      <Routes>
        {/* Se puede cerrar solo el componente Route */}
        <Route path='/' element={<HomePage />} />
        <Route path='login' element={<LoginPage />} />
        <Route path='about' element={<AboutPage />} />
        {/* Formas de gestionar errores 404 */}
        {/* Primera */}
        {/* <Route path='/*' element={<ErrorPage />} /> */}
        {/* Segunda */}
        <Route path='/*' element={<Navigate to={"/about"} />} />
      </Routes>
    </UserProvider>
  )
}
