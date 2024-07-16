import { TodoItem } from './TodoItem'
import PropTypes from 'prop-types';
export const TodoList = ({ todos = [], onHandleTodo, onToggleTodo: handleToggleTodo }) => {
  return (
    <ul className="list-group">
      {
        todos.map(todoElement =>
        (
          <TodoItem
            key={todoElement.id}
            todo={todoElement}
            onHandleTodo={onHandleTodo}
            onToggleTodo={handleToggleTodo}
          />)
        )
      }
    </ul>
  )
}

TodoList.propTypes = {
  todos: PropTypes.array.isRequired,
  onHandleTodo: PropTypes.func.isRequired,
  onToggleTodo: PropTypes.func.isRequired
}