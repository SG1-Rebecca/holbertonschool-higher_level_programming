const redHeader = document.getElementById('redHeader');
redHeader.addEventListener('click', ()=> {
    const header = document.querySelector('header');
    header.classList.add('red');
});