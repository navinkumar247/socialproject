const navSlide = () => {
    const burger = document.querySelector('.burger');
    const nav = document.querySelector('.nav-links');
    const navLinks = document.querySelectorAll('.nav-links li');

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


}

navSlide();