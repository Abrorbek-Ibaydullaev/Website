// ============================= typing animation =====================
var typed = new Typed(".typing", {
    strings: ["", "Web Designer", "YouTuber", "Graphic Designer", "Web Developer"],
    typeSpeed: 150,
    BackSpeed: 60,
    loop: true,
})
// ============================= Aside =====================
const nav = document.querySelector(".nav"),
    navList = nav.querySelectorAll("li"),
    totalNavList = navList.length,
    allSection = document.querySelectorAll(".section"),
    totalSection = allSection.length;
