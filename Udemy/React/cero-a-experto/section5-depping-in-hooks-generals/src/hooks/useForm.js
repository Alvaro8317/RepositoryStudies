import { useState } from 'react';

export const useForm = (initialValuesOfForm = {}) => {
  const [formState, setFormState] = useState(initialValuesOfForm);
  const onInputChange = ({ target }) => {
    const { name, value } = target;
    setFormState({ ...formState, [name]: value });
  };
  const onResetForm = () => {
    setFormState(initialValuesOfForm);
  };
  return { ...formState, onInputChange, onResetForm };
};
