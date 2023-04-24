const textarea = document.querySelector("textarea");
console.log(textarea);
textarea.addEventListener("keyup", e => {
    textarea.style.height = "63px";
    let scHeight = e.target.scrollHeight;
    textarea.style.height = `${scHeight}px`;
});