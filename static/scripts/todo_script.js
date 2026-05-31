//----------To Do----------//
todo_items = []

function fetchNewToDo() {
    console.log("Hello world, la fonction marche!"); 
    var todo_name = document.getElementById("nom").value; 
    //const todo_url = {{ url_for('tache')|tojson }}
    let todo_data = {
        "nom": "nom todo exemple",
        "date": "date exemple",
        "statut": "statut exemple",
        "sous-tache": "sous tache exemple",
    }
    fetch("tache", {
        "method": "POST",
        "headers": {"Content-Type": "application/json"},
        "body": JSON.stringify(todo_data),
    })
    .then(response => console.log(response))
    //.then(response => response.json())
    //.then(responseObj => console.log(responseObj))
    
    todo_name.value = ""; // vide l'input
}

fetchNewToDo()

//me fait syntax error : json.parse unexpectedd char at line 1