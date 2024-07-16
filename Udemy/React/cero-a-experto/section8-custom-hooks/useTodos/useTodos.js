import { useEffect, useReducer } from 'react';
import { todoReducer } from '.todoReducer';
const init = () => JSON.parse(localStorage.getItem('todos')) || [];
export const useTodos = () => {
  const [todos, dispatch] = useReducer(todoReducer, [], init);
  useEffect(() => {
    localStorage.setItem('todos', JSON.stringify(todos));
  }, [todos]);
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
      payload: id,
    });
  };
  const onHandlerToggleTodo = (id) => {
    dispatch({
      type: '[TODO]: Toggle Todo',
      payload: id,
    });
  };
  return {
    todos,
    totalTodosCount: todos.length,
    pendingTodosCount: todos.filter((todo) => !todo.done).length,
    onHandlerDeleteTodo,
    onHandlerToggleTodo,
    onHandleNewTodo,
  };
};
