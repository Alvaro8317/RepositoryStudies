import { createContext } from "react";

/* Este es el valor que se expondrá a todos los componentes */
/* Sirve para dos cosas este contexto, 1. para que el componente de react busque este context
y 2. para definir el proveedor */
export const UserContext = createContext({});