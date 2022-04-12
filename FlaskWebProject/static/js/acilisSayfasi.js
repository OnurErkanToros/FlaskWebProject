let body = document.body;
let logo = document.querySelector(".logo");
let progressBar = document.querySelector(".progressBar");
let ilkSayfa = document.querySelector(".ilkSayfa");
let tanitimVideosu = document.querySelector("#tanitimVideosu");
let videoEkrani = document.querySelector(".videoEkrani");
let counter = 0;

body.addEventListener("click", eventListener);
body.addEventListener("keypress", eventListener);

function eventListener() {
  if (counter === 0) {
    logo.classList.add("janti-logo-animation");
    progressBar.classList.add("progress-doldur-animation");

    setTimeout(() => {
      ilkSayfa.classList.add("sayfayiGizle");
      videoEkrani.classList.remove("sayfayiGizle");
      body.style.overflow = "hidden";
      tanitimVideosu.play();
      tanitimVideosu.addEventListener('ended',()=>{
          window.location = "http://127.0.0.1:1999/anasayfa"
      });
    }, 4000);
  }
  counter++;
}
