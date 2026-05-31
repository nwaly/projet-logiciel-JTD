//----------Journal----------//

function sendData() { // pas utilisé...
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

function ajouterEntree() { // pas utilisé...
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