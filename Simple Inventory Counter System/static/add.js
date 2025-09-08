document.addEventListener("DOMContentLoaded", function () {
  const body = document.body;
  const btn = document.getElementById("darkToggle") || document.querySelector(".toggle-dark");

  function applyTheme(mode) {
    if (mode === "dark") {
      body.classList.add("dark-mode");
      if (btn) {
        btn.setAttribute("aria-pressed", "true");
        btn.textContent = "☀️ Light";
      }
    } else {
      body.classList.remove("dark-mode");
      if (btn) {
        btn.setAttribute("aria-pressed", "false");
        btn.textContent = "🌙 Dark";
      }
    }
  }

  // Restore saved theme or follow system preference
  const saved = localStorage.getItem("theme");
  if (saved) {
    applyTheme(saved);
  } else if (window.matchMedia && window.matchMedia("(prefers-color-scheme: dark)").matches) {
    applyTheme("dark");
  } else {
    applyTheme("light");
  }

  if (!btn) {
    console.warn("Dark mode toggle button not found. Add <button id='darkToggle' class='toggle-dark'>🌙 Dark</button>");
    return;
  }

  btn.addEventListener("click", function () {
    const isDark = body.classList.toggle("dark-mode");
    localStorage.setItem("theme", isDark ? "dark" : "light");
    btn.setAttribute("aria-pressed", String(isDark));
    btn.textContent = isDark ? "☀️ Light" : "🌙 Dark";
  });
});

