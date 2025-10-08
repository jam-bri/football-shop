function showToast(title, message, type = "normal", duration = 3000) {
  // get HTML elements
  const toast = document.getElementById("toast-component");
  const titleEl = document.getElementById("toast-title");
  const messageEl = document.getElementById("toast-message");

  // safety: if not found, stop
  if (!toast) return;

  // change colors based on type
  if (type === "success") {
    toast.className = "fixed bottom-8 right-8 p-4 px-6 rounded-xl shadow-lg border z-50 bg-green-50 border-green-500 text-green-700 opacity-0 translate-y-10 transition-all duration-300";
  } else if (type === "error") {
    toast.className = "fixed bottom-8 right-8 p-4 px-6 rounded-xl shadow-lg border z-50 bg-red-50 border-red-500 text-red-700 opacity-0 translate-y-10 transition-all duration-300";
  } else {
    toast.className = "fixed bottom-8 right-8 p-4 px-6 rounded-xl shadow-lg border z-50 bg-yellow-50 border-yellow-400 text-yellow-700 opacity-0 translate-y-10 transition-all duration-300";
  }

  // set title & message
  titleEl.textContent = title;
  messageEl.textContent = message;

  // show the toast (fade in)
  toast.classList.remove("opacity-0", "translate-y-10");
  toast.classList.add("opacity-100", "translate-y-0");

  // hide after a few seconds
  setTimeout(() => {
    toast.classList.remove("opacity-100", "translate-y-0");
    toast.classList.add("opacity-0", "translate-y-10");
  }, duration);
}
