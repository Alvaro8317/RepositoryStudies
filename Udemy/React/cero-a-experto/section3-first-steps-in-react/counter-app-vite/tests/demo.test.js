describe('Test of hello world in test', () => {
  test('This test should not fail', () => {
    /* Arrange */
    const message1 = 'Hola mundo';
    /* Act */
    const message2 = message1.trim();
    /* Assert */
    expect(message1).toBe(message2);
  });
});
