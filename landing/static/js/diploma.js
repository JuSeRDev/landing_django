const buttonSkills = document.querySelectorAll(".title-diploma")
const diplomas = document.querySelectorAll(".diploma")
const diplomasDiv = document.querySelectorAll(".diplomas-div")

buttonSkills.forEach((skill, i) => {
  skill.addEventListener("click",()=>{
    diplomas[i].classList.toggle("active")
    diplomasDiv[i].classList.toggle("dv-active")
  })
});