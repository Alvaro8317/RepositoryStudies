import { TodoList } from './components/TodoList';
import { TodoAdd } from './components/TodoAdd';
import { useTodos } from '../hooks';
export const TodoApp = () => {
  const { todos, totalTodosCount, pendingTodosCount, onHandlerDeleteTodo, onHandleNewTodo, onHandlerToggleTodo } = useTodos()
  return (
    <>
      <h1>
        TodoApp {totalTodosCount} <small>pendientes: {pendingTodosCount}</small>
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
