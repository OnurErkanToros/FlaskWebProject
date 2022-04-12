window.onscroll = function() {myFunction()};

var navbar = document.querySelector("#navbar");
var navbarBrandImg= document.querySelector(".navbar-brand>img");
var sticky = navbar.offsetTop;
var carousel = document.querySelector("#carousel");
var baseDiv = document.querySelector(".base-div");

// Add the sticky class to the navbar when you reach its scroll position. Remove "sticky" when you leave the scroll position
function myFunction() {
  if (window.pageYOffset >= sticky) {
    let navbarHeight =  navbar.clientHeight;
    navbarBrandImg.classList.add("scroll-nav-img")
    navbar.classList.add("fixed-top");
    navbar.classList.add("bg-light");
    baseDiv.style.paddingTop="200px";
  } else {
    navbarBrandImg.classList.remove("scroll-nav-img")
    navbar.classList.remove("fixed-top");
    navbar.classList.remove("bg-light");
    baseDiv.style.paddingTop="10px";
  }
}