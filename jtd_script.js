// pour afficher la date actuel en haut à gauche
const d = new Date();
const month = ["January","February","March","April","May","June","July","August","September","October","November","December"];
let name = month[d.getMonth()];
document.getElementById("today").innerHTML = d.getDate().toString()+" "+name+" "+d.getFullYear().toString();

// Journal
// Bouton
function newEntry() {
    const para = document.createElement("textarea");
    document.getElementById("MainPage").appendChild(para);
}

function valEntry() {
    const newNode = document.createElement("li");
    const textNode = document.getElementById("EntryInput");
    console.log(textNode);
    newNode.innerText = textNode.value;
    const list = document.getElementById("EntryList");
    list.insertBefore(newNode, list.children[0]);
}