/* El estado inicial, como quiero que inicie mi aplicación */
const initialState = [
  { id: 1, todo: 'Recolectar la piedra del alma', done: false },
];

/* un Reducer no es más que una función pura */
/* El estado por defecto es el estado inicial y el action es lo que cambia el estado, siempre debe de devolver un nuevo estado */
/* Ideal para casos complejos, para variables booleanas se puede hacer también con un useState*/
const todoReducer = (state = initialState, action = {}) => {
  if (action.type === '[TODO] add todo') {
    /* Con el spread operator se evita mutar el estado inicial */
    /* El push se debe de evitar en react porque afecta el estado inicial, lo muta, mejor generar un nuevo estado */
    return [...state, action.payload];
  }
  return state;
};
let todos = todoReducer();
console.log(todos);

/* MALA PRÁCTICA, NO SE DEBE DE MUTAR EL ESTADO DE ESTA MANERA PORQUE NO RENDERIZARÁ EL COMPONENTE, esto se debe de hacer con el reducer */
// todos.push({ id: 2, todo: 'Recolectar la piedra del poder', done: false });
/* Correcto */
const newTodo = { id: 2, todo: 'Recolectar la piedra del poder', done: false };
/* Este es un estándar que se verá en redux */
/* El payload no es siempre necesario, como borar todos los todos */
const addTodoAction = {
  type: '[TODO] add todo',
  payload: newTodo,
};
todos = todoReducer(todos, addTodoAction);

console.log({ state: todos });
