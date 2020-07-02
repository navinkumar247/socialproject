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

if (modalBtn){
    modalBtn.addEventListener('click', function(){
        modalBg.classList.add('modal-active');
    });
};
if (modalClose){
    modalClose.addEventListener('click',function(){
        modalBg.classList.remove('modal-active');
    });
}


// 
// LIKE BUTTON - AJAX
// 

const likeBtn = document.querySelectorAll('.like-btn');

likeBtn.forEach((item)=>{item.addEventListener('click',function(e){
    e.preventDefault();
    const postId = item.attributes.id;
    const likeText = item.textContent.trim();
    const url1 = 'posts/like/'+postId.value;
    const url = new URL(url1, 'http://127.0.0.1:8000');

    var xhr = new XMLHttpRequest();
        xhr.open('GET',url, true);

        xhr.onload = function (){
            if(this.status == 200){
                if(likeText=='Like'){
                    item.innerHTML = 'Unlike'
                }else {
                    item.innerHTML = 'Like';
                }
            }
        }
        xhr.onerror = function(){
            console.log('error');
        }
        xhr.send();

})})
    
    
    
    