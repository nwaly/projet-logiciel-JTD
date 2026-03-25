// pour afficher la date actuel en haut à gauche
const d = new Date();
const month = ["January","February","March","April","May","June","July","August","September","October","November","December"];
let name = month[d.getMonth()];
document.getElementById("demo").innerHTML = d.getDate().toString()+" "+name+" "+d.getFullYear().toString();

// Journal
// Bouton
function newEntry() {
    const para = document.createElement("textarea");
    document.body.getElementById("MainPage").appendChild(para);
}