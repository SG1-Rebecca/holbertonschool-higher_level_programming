const addItem = document.getElementById('add_item');
addItem.addEventListener('click', () => {
  const myList = document.querySelector('.my_list');
  const li = document.createElement('li');
  li.textContent = 'Item';
  myList.append(li);
});
