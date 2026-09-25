// Donne un nom accessible à la boîte de dialogue de recherche de Material (audit d'accessibilité).
document.addEventListener("DOMContentLoaded", function () {
  var search = document.querySelector('[data-md-component="search"]');
  if (search && !search.getAttribute("aria-label")) {
    search.setAttribute("aria-label", document.documentElement.lang === "en" ? "Search" : "Recherche");
  }
});
