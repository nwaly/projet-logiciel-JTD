//----------To Do----------//

// pour avoir la date dans le bon format
const td = new Date();
const mois = ["01","02","03","04","05","06","07","08","09","10","11","12"];
let num_mois = mois[td.getMonth()];
const jour = ["00", "01", "02", "03", "04","05","06","07","08","09","10","11","12","13","14","15","16","17","18","19","20","21","22","23","24","25","26","27","28","29","30","31"]
let num_jour = jour[td.getDate()];
// formater la date du todo en YYYY-MM-DD
todo_date = td.getFullYear()+"-"+num_mois+"-"+num_jour;
console.log(todo_date)

// fonction pour fetch la méthode 'tache'
function fetchNewToDo() {
    console.log("Hello world, la fonction marche!"); 
    var todo_name = document.getElementById("nom").value; 
    let todo_data = {
        "nom": todo_name,
        "date": todo_date,
        "statut": 0,
        "sous_tache": 0
    }
    fetch("tache", {
        "method": "POST",
        "headers": {"Content-Type": "application/json"},
        "body": JSON.stringify(todo_data),
    })
    .then(response => response.json()) //.then(response => console.log(response))
    .then(responseObj => console.log(responseObj))

    document.getElementById("nom").value = " "; // vide l'input
}

fetchNewToDo()

//me fait syntax error : json.parse unexpectedd char at line 1