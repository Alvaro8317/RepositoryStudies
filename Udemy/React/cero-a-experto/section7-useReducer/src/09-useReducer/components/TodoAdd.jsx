import PropTypes from 'prop-types';
import { useForm } from '../../hooks/useForm';

export const TodoAdd = ({ onHandleNewTodo }) => {
  const { description, onInputChange, onResetForm } = useForm({
    description: '',
  });
  const onSubmit = (event) => {
    event.preventDefault()
    if (description.length <= 1) return;
    onHandleNewTodo({
      id: new Date().getTime(),
      description: description,
      done: false
    })
    onResetForm()
  }
  return (
    <form onSubmit={onSubmit}>
      <input type="text" placeholder="¿Qué hay que hacer?" name='description' className="form-control" value={description} onChange={onInputChange} />
      <button type="submit" className="btn btn-outline-primary mt-1">Agregar</button>
      <button onClick={onResetForm} className='btn btn-danger mt-1'>Resetear el campo</button>
    </form>
  )
}

TodoAdd.propTypes = {
  onHandleNewTodo: PropTypes.func.isRequired,
}
/* Forma manual */
// const [descriptionToDo, setDescriptionToDo] = useState("")
// const onInputChange = ({ target }) => {
//   setDescriptionToDo(target.value)
// }
// const onSubmit = (event) => {
//   event.preventDefault()
//   onHandleNewTodo({
//     id: new Date().getTime(),
//     description: descriptionToDo,
//     done: false
//   })
// }
// return (
//   <form onSubmit={onSubmit}>
//     <input type="text" placeholder="¿Qué hay que hacer?" className="form-control" value={descriptionToDo} onChange={onInputChange} />
//     <button type="submit" className="btn btn-outline-primary mt-1">Agregar</button>
//   </form>
// )
/* Usando customHook */