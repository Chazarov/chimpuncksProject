const menuButton = document.getElementById('menu-button');
const navigationDrawer = document.getElementById('navigation-drawer');
const togglePersonalDataButton = document.getElementById('toggle-personal-data');
const personalDataContent = document.getElementById('personal-data-content');
const toggleEducationButton = document.getElementById('toggle-education');
const educationContent = document.getElementById('education-content');


menuButton.addEventListener('click', () => {
  navigationDrawer.classList.toggle('closed');
});

togglePersonalDataButton.addEventListener('click', () => {
  personalDataContent.style.display = personalDataContent.style.display === 'none' ? 'block' : 'none';
});

toggleEducationButton.addEventListener('click', () => {
  educationContent.style.display = educationContent.style.display === 'none' ? 'block' : 'none';
});

const navItems = document.querySelectorAll('.nav-item');
navItems.forEach(item => {
    item.addEventListener('click', (event) => {
        // Удаляем класс 'active' у всех элементов
        navItems.forEach(navItem => navItem.classList.remove('active'));

        // Добавляем класс 'active' к выбранному элементу
        event.target.classList.add('active');

        // Получаем индекс выбранной секции
        const selectedIndex = event.target.getAttribute('data-index');

        // Здесь нужно добавить логику загрузки контента 
        // в зависимости от selectedIndex
        console.log("Выбрана секция:", selectedIndex);
    });
});