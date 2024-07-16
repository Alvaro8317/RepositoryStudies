import { useEffect, useReducer } from 'react';
import { todoReducer } from './todoReducer';
import { TodoList } from './components/TodoList';
import { TodoAdd } from './components/TodoAdd';
const initialState = [
  // {
  //   id: new Date().getTime(),
  //   description: 'Recolectar la piedra del alma',
  //   done: false,
  // },
  // {
  //   id: new Date().getTime() * 3,
  //   description: 'Recolectar la piedra del espacio',
  //   done: false,
  // },
];
/* Si solo se tiene un reducer, lo ideal es dejar el dispatch con ese nombre, si no, se puede dejar como dispatchTodo, dispatchNotTodo, etc. */
/* Init es la función que inicializa el reducer */
const init = () => JSON.parse(localStorage.getItem('todos')) || [];
export const TodoApp = () => {
  /* useTodo
  
  Debe de exponer
  todos, handleDeleteTodo, handleToggleTodo, handleNewTodo
  const {todos, handleDeleteTodo, handleToggleTodo, handleNewTodo} ) useTodos();
  */
  const [todos, dispatch] = useReducer(todoReducer, initialState, init);
  useEffect(() => {
    localStorage.setItem('todos', JSON.stringify(todos));
  }, [todos])

  const onHandleNewTodo = (todo) => {
    const action = {
      type: '[TODO]: Add Todo',
      payload: todo,
    };
    dispatch(action);
  };
  const onHandlerDeleteTodo = (id) => {
    dispatch({
      type: '[TODO]: Remove Todo',
      payload: id
    })
  }
  const onHandlerToggleTodo = (id) => {
    dispatch({
      type: '[TODO]: Toggle Todo',
      payload: id
    })
  }
  return (
    <>
      e
      <h1>
        TodoApp 10 <small>pendientes: 2</small>
      </h1>
      <hr />
      <div className='row'>
        <div className='col-7'>
          <TodoList
            todos={todos}
            onHandleTodo={onHandlerDeleteTodo}
            onToggleTodo={onHandlerToggleTodo}
          />
        </div>
        <div className='col-5'>
          <h4>Agregar TODO</h4>
          <hr />
          <TodoAdd
            onHandleNewTodo={onHandleNewTodo}
          />
        </div>
      </div>
    </>
  );
};
