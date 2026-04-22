// pour afficher la date actuel en haut à gauche
const d = new Date();
const month = ["January","February","March","April","May","June","July","August","September","October","November","December"];
let name = month[d.getMonth()];
document.getElementById("today").innerHTML = d.getDate().toString()+" "+name+" "+d.getFullYear().toString();

// Journal //
// Bouton
function newEntry() {
    const para = document.createElement("textarea");
    document.getElementById("MainPage").appendChild(para);
}

function valEntry() {
    if (!document.getElementById("EntryInput").value == "") {
    //crée un élément li sous la const 'newNode'
    // = crée la balise dans laquelle la nouvelle entrée va être stockée 
    const newNode = document.createElement("li");
    //associe l'input actuel à la const 'textNode'
    const textNode = document.getElementById("EntryInput");
    //juste pour check : écrit le contenu du textNode (=de l'input actuel) dans la console? je crois?
    console.log(textNode);
    //associe le contenu texte (value) du textNode (=de l'input actuel) à l'innerText du newNode (=de la balise de la nouvelle entrée)
    newNode.innerText = textNode.value;
    //associe la balise de la liste d'entrée (ul) à la const 'list'
    const list = document.getElementById("EntryList");
    //insère/ajoute newNode (=la nouvelle entrée) à la popsition [0] (=tout en haut) de la liste d'entrées 'list'
    list.insertBefore(newNode, list.children[0]);
    }
    //vide le contenu de l'input
    document.getElementById("EntryInput").value = "";

    // à faire mnt :
    // transformer le li en div/container joli avec le texte dedans
    // trouver un moyen de fixe le problème de position?
    // ou bien faire l'option de bouton New Entry > pop up pour la partie écriture de journal
    // avec bouton 'valider' qui crée la nouvelle entrée
}

// TO DO
// new entry => formulaire?
// chaque entrée => a un idée
// check comment une base de données sql fonctionne