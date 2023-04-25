const textarea = document.querySelector("textarea");
  
  function adjustTextareaHeight() {
    textarea.style.height = "63px";
    let scHeight = textarea.scrollHeight;
    textarea.style.height = `${scHeight}px`;
  }
  
  textarea.addEventListener("keyup", adjustTextareaHeight);
  
  adjustTextareaHeight();