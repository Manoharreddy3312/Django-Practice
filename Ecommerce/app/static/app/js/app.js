(function () {
  // Small enhancement: allow dropdowns on touch by toggling class.
  const dropdowns = document.querySelectorAll(".nav-dropdown");
  dropdowns.forEach((d) => {
    d.addEventListener("click", (e) => {
      // Only toggle when clicking inside the dropdown trigger (button).
      if (e.target && e.target.tagName && e.target.tagName.toLowerCase() === "button") {
        d.classList.toggle("open");
      }
    });
  });
})();

