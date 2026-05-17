// check si le lien au script marche//
// console.log("JavaScript file linked successfully!");  
// alert("Hello from Flask + JavaScript!");

//----------Header----------//

// affiche la date actuelle
const d = new Date();
const month = ["January","February","March","April","May","June","July","August","September","October","November","December"];
let month_name = month[d.getMonth()];
document.getElementById("today").innerHTML = d.getDate().toString()+" "+month_name+" "+d.getFullYear().toString();

//----------Journal----------//

function sendData() {
    var value = document.getElementById('titre').value;
    $.ajax({
        url: '/submit_form',
        type: 'POST',
        contentType: 'application/json',
        data: JSON.stringify({ 'value': value }),
        success: function(response) {
            document.getElementById('output').innerHTML = response.result;
        },
        error: function(error) {
            console.log(error);
        }
    });
}

function ajouterEntree() {
    if (!document.getElementById("contenu").value == "") {
        //crée un élément li sous la const 'newNode'
        // = crée la balise dans laquelle la nouvelle entrée va être stockée 
        const newEntry = document.createElement("li");

        //associe l'input actuel à la const 'textNode'
        const textContenu = document.getElementById("contenu");

        //juste pour check : écrit le contenu du textNode (=de l'input actuel) dans la console? je crois?
        console.log(textContenu);

        //associe le contenu texte (value) du textNode (=de l'input actuel) à l'innerText du newNode (=de la balise de la nouvelle entrée)
        newEntry.innerText = textContenu.value;

        //associe la balise de la liste d'entrée (ul) à la const 'list'
        const list = document.getElementById("output");

        //insère/ajoute newNode (=la nouvelle entrée) à la popsition [0] (=tout en haut) de la liste d'entrées 'list'
        list.insertBefore(newEntry, list.children[0]);
    }
    document.getElementById("contenu").value = "";
}
