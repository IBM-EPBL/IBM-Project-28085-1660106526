const openHireMeButtons = document.querySelector("[data-hireMe-target]");
const closeHireMeButtons = document.querySelector("[data-close-button]");
const overlay = document.getElementById("overlay");

openHireMeButtons.forEach((button) => {
  button.addEventListener("click", () => {
    const hireMe = document.querySelector(button.dataset.hireMeTarget);
    // selects the #hireMe from html file which is the entire section
    openHireMe(hireMe);
  });
});
overlay.addEventListener("click", () => {
  const hireMes = document.querySelectorAll(".hireMe.active");
  hireMes.forEach((hireMe) => {
    closeHireMe(hireMe);
  });
});

closeHireMeButtons.forEach((button) => {
  button.addEventListener("click", () => {
    const hireMe = button.closest(".hireMe");
    // accessing closest parent class of the hireMe button => <div class="hireMe" id="hireMe">
    closeHireMe(hireMe);
  });
});

function openHireMe(hireMe) {
  if (hireMe == null) return;
  hireMe.classList.add("active");
  overlay.classList.add("active");
}
function closeHireMe(hireMe) {
  if (hireMe == null) return;
  hireMe.classList.remove("active");
  overlay.classList.remove("active");
}
