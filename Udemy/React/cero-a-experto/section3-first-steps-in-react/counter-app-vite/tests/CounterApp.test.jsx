import { fireEvent, render, screen } from '@testing-library/react';
import CounterApp from '../src/CounterApp';
/*
 * Uno puede simular cualquier tipo de evento con fireEvent
 */
describe('Tests of CounterApp', () => {
  const initialValueOfCounter = 100;
  test('should match the snapshot', () => {
    const { container } = render(<CounterApp value={initialValueOfCounter} />);
    expect(container).toMatchSnapshot();
  });
  test('should show the initial value of 100', () => {
    render(<CounterApp value={initialValueOfCounter} />);
    expect(screen.getByText(initialValueOfCounter)).toBeTruthy();
  });
  test('should increase +1 with the button', () => {
    render(<CounterApp value={initialValueOfCounter} />);
    fireEvent.click(screen.getByText('+1'));
    expect(screen.getByText(initialValueOfCounter + 1)).toBeTruthy();
  });
  test('should decrease -1 with the button', () => {
    render(<CounterApp value={initialValueOfCounter} />);
    fireEvent.click(screen.getByText('-1'));
    expect(screen.getByText(initialValueOfCounter - 1)).toBeTruthy();
  });
  test('should works the reset button', () => {
    render(<CounterApp value={initialValueOfCounter} />);
    fireEvent.click(screen.getByText('+1'));
    fireEvent.click(screen.getByText('+1'));
    fireEvent.click(screen.getByText('+1'));
    // fireEvent.click(screen.getByText('Reset')); Forma no tan cool
    fireEvent.click(screen.getByRole('button', { name: 'btn-reset' }));
    expect(screen.getByText(initialValueOfCounter)).toBeTruthy();
  });
});
