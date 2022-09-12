const themeToggle = document.querySelector(".theme-toggle")
const slider = document.querySelector(".slider")
const currentTheme = localStorage.getItem("current-theme")

function themeChanger(){
    slider.style.backgroundColor="hsl(271, 28%, 12%)"
    slider.style.webkitTransform = "rotate(180deg)"
    // slider.style.transform = 'translateX(15px)';
    // slider.style.transform = 'translateX(15px)'
}

document.addEventListener("DOMContentLoaded", function(event) {
    if (currentTheme){
        if (currentTheme=="dark"){
            themeChanger()
        }else{
            slider.style.backgroundColor="hsl(0, 0%, 80%)"
            slider.style.webkitTransform = "rotate(0deg)"
        }
        document.documentElement.setAttribute("data-theme", currentTheme)
    }else{
        document.documentElement.setAttribute("data-theme", "light")
    }
  }
)

themeToggle.addEventListener('click', ()=>{
    let current = document.documentElement.getAttribute("data-theme")
    if(current=="light"){
        themeChanger()
    }else{
        slider.style.backgroundColor="hsl(0, 0%, 80%)"
        slider.style.webkitTransform = "rotate(0deg)"
    }
    let switchTheme = current == 'dark' ? 'light': 'dark'
    document.documentElement.setAttribute("data-theme", switchTheme)
    localStorage.setItem('current-theme', switchTheme)
   
})

const navItems = document.querySelector(".nav-items")
const collapseToggle = document.querySelector(".collapse-toggle")
collapseToggle.addEventListener('click', ()=>{
    collapseToggle.classList.toggle("active")
    navItems.classList.toggle("nav-items-show")
})

const postsScroll= document.querySelector(".posts-scroll")
const posts = document.querySelector(".posts")

posts.onscroll =()=>{
    if (posts.scrollTop > 20) {
        postsScroll.style.display = "block";
      } else {
        postsScroll.style.display = "none";
      }
}

    
postsScroll.addEventListener("click", ()=>{
    posts.scrollTop = 0
    
})

const messagesClose = document.getElementById("messages-close-icon")
const messages = document.getElementById("messages")

const closeMessages = ()=>{
    messages.style.display='none'
}

const newsletter = document.querySelector(".newsletter")
const subscribeClose = document.querySelector(".subscribe-close-icon")
const subscribeLink = document.getElementById("subscribe-link")
subscribeLink.addEventListener("click", ()=>{
    newsletter.style.opacity = 1
    newsletter.style.visibility= 'visible'
   
})
const closeSubscribe = ()=>{
    newsletter.style.opacity = 0
    newsletter.style.visibility= 'hidden'
    collapseToggle.classList.remove("active")
    navItems.classList.toggle("nav-items-show")
}


const contactMeLink = document.getElementById("contact-me")
const categoriesLink = document.getElementById("categories-link")
const recentArticlesLink = document.getElementById("recent-articles-link")
const rightSideBar = document.querySelector(".side-bar-right")
const leftSideBar = document.querySelector(".side-bar-left")

contactMeLink.addEventListener("click", ()=>{
    posts.style.display='none'
    leftSideBar.style.display="none"
    rightSideBar.style.display='block'
    collapseToggle.classList.remove("active")
    navItems.classList.remove("nav-items-show")
})


categoriesLink.addEventListener("click", ()=>{
    leftSideBar.style.display="block"
    posts.style.display="none"
    rightSideBar.style.display='none'
    collapseToggle.classList.remove("active")
    navItems.classList.remove("nav-items-show")
})

recentArticlesLink.addEventListener("click", ()=>{
    leftSideBar.style.display="none"
    posts.style.display="block"
    rightSideBar.style.display='none'
    collapseToggle.classList.remove("active")
    navItems.classList.remove("nav-items-show")
})

const footer = document.querySelector(".copyright")
footer.innerHTML = "2022"

const downloadLink = document.getElementById("downloads-link")
const downloads = document.getElementById("downloads")
const downloadClose = document.getElementById("download-close")
downloadLink.addEventListener("click",()=>{
    downloads.style.opacity = 1
    downloads.style.visibility = "visible"
})

downloadClose.addEventListener("click",()=>{
    downloads.style.opacity = 0
    downloads.style.visibility = "hidden"
    collapseToggle.classList.remove("active")
    navItems.classList.toggle("nav-items-show")
})