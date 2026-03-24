const header = document.querySelector('header');
const changeText = document.getElementById('update_header');

header.addEventListener('click', () => {
  changeText.textContent = 'New Header!!!';
});
