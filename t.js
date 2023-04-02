const menuBtn = document.querySelector(".menu-btn");
const nav = document.querySelector("nav");
const navLinks = document.querySelectorAll("nav ul li");

let menuOpen = false;

menuBtn.addEventListener("click", () => {
  if (!menuOpen) {
    menuBtn.classList.add("open");
    nav.classList.add("open");
    navLinks.forEach((link) => link.classList.add("open"));
    menuOpen = true;
  } else {
    menuBtn.classList.remove("open");
    nav.classList.remove("open");
    navLinks.forEach((link) => link.classList.remove("open"));
    menuOpen = false;
  }
});
