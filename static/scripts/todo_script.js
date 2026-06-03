//----------To Do----------//

// pour avoir la date dans le bon format
const td = new Date();
const mois = ["01","02","03","04","05","06","07","08","09","10","11","12"];
let num_mois = mois[td.getMonth()];
const jour = ["00", "01", "02", "03", "04","05","06","07","08","09","10","11","12","13","14","15","16","17","18","19","20","21","22","23","24","25","26","27","28","29","30","31"]
let num_jour = jour[td.getDate()];
// formater la date du todo en YYYY-MM-DD
//todo_date = td.getFullYear()+"-"+num_mois+"-"+num_jour;
//console.log(todo_date)

// fonction pour fetch la méthode 'tache' POST
function fetchNewToDo() {
    console.log("Hello world, la fonction todo POST marche!");  
    if (!document.getElementById("nom").value == "") {
        var todo_name = document.getElementById("nom").value;
        var todo_date = document.getElementById("date").value;
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
        .then(response => response.json())
        .then(responseObj => {
            console.log(responseObj);
            console.log(todo_name);
            console.log(todo_date);

            let li = document.createElement("li");
            li.classList.add("li_todo");

            // date
            let div_date = document.createElement("div");
            div_date.classList.add("date_class");
            div_date.innerText = todo_date;
            
            // checkbox
            let checkbox = document.createElement("input"); //crée un élément input
            checkbox.type = "checkbox"; // ajoute l'attribut 'checkbox' au nouvel input
            checkbox.id = "statut";

            // nom
            div_nom = document.createElement("div");
            div_nom.innerText = todo_name;
            
            li.appendChild(div_date);
            li.appendChild(div_nom);
            li.appendChild(checkbox);
            const list = document.getElementById("ul_todos");
            list.insertBefore(li, list.children[0]);
        })

        document.getElementById("nom").value = " "; // vide l'input
    } else {
        console.log("aucune nouvelle tâche trouvée")
    }
}

// fonction pour fetch la méthode 'tache' GET
function fetchAllToDo() {
    console.log("Hello world, la fonction todo GET marche!"); 
    fetch("tache", {
        "method": "GET",
        "headers": {"Content-Type": "application/json"},
    })
    .then(response => response.json())
    .then(responseObj => {
        console.log(responseObj)
        
        responseObj.forEach((todo) => {
            console.log(todo)
            let li = document.createElement("li");
            li.id = todo.Tache_ID;
            li.classList.add("li_todo");

            // date
            let div_date = document.createElement("div");
            div_date.innerText = todo.Tache_date;
            
            // checkbox
            let checkbox = document.createElement("input"); //crée un élément input
            checkbox.type = "checkbox"; // ajoute l'attribut 'checkbox' au nouvel input
            checkbox.id = "statut";
            checkbox.for = todo.Tache_ID;

            // nom
            div_nom = document.createElement("div");
            div_nom.innerText = todo.Tache_nom;
            
            li.appendChild(div_date)
            li.appendChild(div_nom)
            li.appendChild(checkbox);
            const list = document.getElementById("ul_todos");
            list.insertBefore(li, list.children[0]);
        })
    })
}

