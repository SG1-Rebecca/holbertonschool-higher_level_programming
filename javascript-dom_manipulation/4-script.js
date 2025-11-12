const add_item = document.getElementById('add_item');
add_item.addEventListener('click', () => {
  const my_list = document.querySelector('.my_list');
  const li = document.createElement('li');
  li.textContent = 'Item';
  my_list.append(li);
});
