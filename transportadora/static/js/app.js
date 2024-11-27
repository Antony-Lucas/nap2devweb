// para fazer a rolagem da pagina

const menuLink = document.querySelectorAll('.menu a[href^="#"]');

console.log(menuLink);

function scrollToSection(event) {
  // event.preventDefault();
  // console.log(event.target);
  const element = event.target;
  const id = element.getAttribute("href");
  const section = document.querySelector(id);
  console.log(section);
}

menuLink.forEach((link) => {
  link.addEventListener("click", scrollToSection);
});
