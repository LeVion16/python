const article = document.querySelector('section');
const btn = document.querySelector('button');
const h1 = document.querySelector('h1')
const color1 = document.querySelector('h1');
const color2 = document.querySelector('h3');
const color3 = document.querySelector('button');
let countP = document.querySelector('.count');
let c = 0

function handleClick() {
    c++;
    countP.textContent = `Kattintások száma: ${c}`;
    if (article.className === "like"){
        article.classList.remove("like");
    }else{
        article.classList.add("like");
    }
    if (c === 10){
        h1.style.visibility = 'hidden';
    }
}

btn.addEventListener("click", handleClick)

/* 
function handleClick() {
    console.log("1.", article.style.backgroundColor)
    article.style.backgroundColor === 'rgba(138, 36, 36, 0.34)';
    // color1.style.color = 'rgba(255, 0, 234, 0.86)';
    // color2.style.color = 'rgba(255, 0, 234, 0.86)';
    // color3.style.color = 'rgba(255, 0, 234, 0.86)';
    if (article.style.backgroundColor){
        console.log("2.", article.style.backgroundColor)
        article.style.backgroundColor = "";
    }else{
        article.style.backgroundColor = "rgba(138, 36, 36, 0.34)"
        console.log("3.", article.style.backgroundColor)
    }
} 
*/