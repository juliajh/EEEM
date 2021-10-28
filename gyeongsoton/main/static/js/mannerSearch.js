const sideBar = document.querySelector('.side__bar');
const findBtn = document.querySelector('.find__btn');

findBtn.addEventListener('click', () => {
  sideBar.classList.toggle('active');
});