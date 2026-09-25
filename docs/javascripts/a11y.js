// Donne un nom accessible à la boîte de dialogue de recherche de Material (audit d'accessibilité).
document.addEventListener("DOMContentLoaded", function () {
  var search = document.querySelector('[data-md-component="search"]');
  if (search && !search.getAttribute("aria-label")) {
    search.setAttribute("aria-label", document.documentElement.lang === "en" ? "Search" : "Recherche");
  }
});

// Donne un nom accessible aux cases des listes de tâches (désactivées, décoratives) : le texte de l'élément.
document.addEventListener("DOMContentLoaded", function () {
  document.querySelectorAll('.task-list-item input[type="checkbox"]').forEach(function (box) {
    if (box.getAttribute("aria-label")) {
      return;
    }
    var item = box.closest("li");
    var text = item ? item.textContent.replace(/\s+/g, " ").trim() : "";
    if (text) {
      box.setAttribute("aria-label", text);
    }
  });
});
