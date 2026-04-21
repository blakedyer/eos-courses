document.addEventListener("DOMContentLoaded", () => {
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
