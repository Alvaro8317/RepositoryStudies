import { fireEvent, render, screen } from '@testing-library/react';
import { AddCategory } from '../../src/components/AddCategory';

/*
 * Los jest functions permiten mockear funciones
 */

describe('Tests of AddCategory', () => {
  const inputValueOfTest = 'Metal Gear';
  test('should change the value of the text box', () => {
    render(<AddCategory onNewCategory={() => {}} />);
    const input = screen.getByRole('textbox');
    fireEvent.input(input, { target: { value: inputValueOfTest } });
    expect(input.value).toBe(inputValueOfTest);
  });

  test('should call onNewCategory if the input has a value and after that, must be blank', () => {
    const onNewCategory = jest.fn();
    render(<AddCategory onNewCategory={onNewCategory} />);
    const input = screen.getByRole('textbox');
    const form = screen.getByRole('form');
    fireEvent.input(input, { target: { value: inputValueOfTest } });
    fireEvent.submit(form);
    expect(input.value).toBe('');
    expect(onNewCategory).toHaveBeenCalled();
    expect(onNewCategory).toHaveBeenCalledTimes(1);
    expect(onNewCategory).toHaveBeenCalledWith(inputValueOfTest);
  });
  test('should not call onNewCategory if the input is empty', () => {
    const onNewCategory = jest.fn();
    render(<AddCategory onNewCategory={onNewCategory} />);
    const form = screen.getByRole('form');
    fireEvent.submit(form);
    expect(onNewCategory).not.toHaveBeenCalled()
    expect(onNewCategory).toHaveBeenCalledTimes(0)
  });
});
