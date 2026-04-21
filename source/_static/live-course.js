document.addEventListener("DOMContentLoaded", () => {
  const courseSidebarToggle =
    document.getElementById("pst-primary-sidebar-checkbox") ||
    document.getElementById("__primary");
  const openButtons = document.querySelectorAll(".teaching-mobile-nav-toggle");
  const closeButtons = document.querySelectorAll(".teaching-mobile-nav-close");
  const mobileSidebarMedia = window.matchMedia("(max-width: 959.98px)");

  if (courseSidebarToggle) {
    const syncSidebarButtons = () => {
      const expanded = courseSidebarToggle.checked ? "true" : "false";
      openButtons.forEach((button) => button.setAttribute("aria-expanded", expanded));
      closeButtons.forEach((button) => button.setAttribute("aria-expanded", expanded));
    };

    const syncSidebarMode = () => {
      if (!mobileSidebarMedia.matches) {
        courseSidebarToggle.checked = false;
      }
      syncSidebarButtons();
    };

    openButtons.forEach((button) => {
      button.addEventListener("click", () => {
        courseSidebarToggle.checked = !courseSidebarToggle.checked;
        syncSidebarButtons();
      });
    });

    closeButtons.forEach((button) => {
      button.addEventListener("click", () => {
        courseSidebarToggle.checked = false;
        syncSidebarButtons();
      });
    });

    courseSidebarToggle.addEventListener("change", syncSidebarButtons);
    mobileSidebarMedia.addEventListener("change", syncSidebarMode);
    syncSidebarMode();
  }

  const lastModified = document.getElementById("lastModified");
  if (!lastModified) {
    return;
  }

  const options = {
    weekday: "short",
    year: "numeric",
    month: "short",
    day: "numeric",
  };

  const modifiedDateString = document.lastModified;
  const lastModDate = new Date(modifiedDateString);
  const formattedTime =
    lastModDate.toLocaleDateString("en-US", options) +
    " at " +
    lastModDate.toLocaleTimeString([], { hour: "2-digit", minute: "2-digit" });

  lastModified.textContent = "Last updated " + formattedTime;
});
