let notice = document.querySelector('.msg')

if (notice) {
    setTimeout(() => {
        notice.classList.add('hide')
    }, 5000)
}
let dropDown=document.querySelector('.drop')
let dropContent=document.querySelector('.drop-menu')
let icon=document.querySelector('.drop-down-arrow')
dropDown.addEventListener('mouseenter',()=>{dropContent.style.display="block"})
dropDown.addEventListener('mouseleave',()=>{dropContent.style.display="none"})
dropDown.addEventListener('mouseenter',()=>{icon.style.transform="rotate(180deg)"})
dropDown.addEventListener('mouseleave',()=>{icon.style.transform="rotate(0deg)"})