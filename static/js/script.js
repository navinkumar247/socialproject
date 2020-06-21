const navSlide = () => {
    const burger = document.querySelector('.burger');
    const nav = document.querySelector('.nav-links');
    const navLinks = document.querySelectorAll('.nav-links li');

    const dropdown = document.querySelector('.dropdown-menu');
    const profile = document.querySelector('.profile');

    burger.addEventListener('click', () => {
            
        nav.classList.toggle('nav-active');
    
        navLinks.forEach((link, index) => {

            if(link.style.animation){
                link.style.animation = '';
            }
            else{
                let delay = (index / 7 + 1).toString() + 's';
                link.style.animation = "navLinksFade 0.5s ease forwards"+" "+delay ;
            }
            
    });
    });
    profile.addEventListener('click',() => {

        dropdown.classList.toggle('profile-slide');
    });
}

navSlide();

const modalBg = document.querySelector('.modal-bg');
const modalBtn = document.querySelector('.modal-btn');
const modalClose = document.querySelector('.modal-box .close');

modalBtn.addEventListener('click', function(){
    modalBg.classList.add('modal-active');
})
modalClose.addEventListener('click',function(){
    modalBg.classList.remove('modal-active');
})