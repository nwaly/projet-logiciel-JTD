//----------Journal----------//

// pour avoir la date dans le bon format
const td = new Date();
const mois = ["01","02","03","04","05","06","07","08","09","10","11","12"];
let num_mois = mois[td.getMonth()];
const jour = ["00", "01", "02", "03", "04","05","06","07","08","09","10","11","12","13","14","15","16","17","18","19","20","21","22","23","24","25","26","27","28","29","30","31"]
let num_jour = jour[td.getDate()];
// formater la date du todo en YYYY-MM-DD
let today_date = td.getFullYear()+"-"+num_mois+"-"+num_jour;
console.log(today_date)

function fetchNewJournal() {
    console.log("Hello world, la fonction journal POST marche!");  
    if (!document.getElementById("titre").value == " " && !document.getElementById("contenu").value == " ") {
        var journal_titre = document.getElementById("titre").value;
        var journal_date = today_date;
        var journal_contenu = document.getElementById("contenu").value;
        let journal_data = {
            "titre": journal_titre,
            "date": journal_date,
            "contenu": journal_contenu,
            "modification": 0,
        }
        fetch("journal", {
            "method": "POST",
            "headers": {"Content-Type": "application/json"},
            "body": JSON.stringify(journal_data),
        })
        .then(response => response.json())
        .then(responseObj => {
            console.log(responseObj);
            console.log(journal_titre);
            console.log(journal_date);

            let div = document.createElement("div");
            div.classList.add("journal_container");

            // titre
            div_titre = document.createElement("div");
            div_titre.classList.add("titre_class");
            div_titre.innerText = journal_titre;

            // date
            let div_date = document.createElement("div");
            div_date.classList.add("date_class");
            div_date.innerText = journal_date;
            
            // div titre-date container
            let div_cont = document.createElement("div");
            div_cont.classList.add("div_container");

            // contenu
            let p_contenu = document.createElement("p");
            p_contenu.innerText = journal_contenu;
            p_contenu.classList.add("p_contenu");
            
            div_cont.appendChild(div_titre);
            div_cont.appendChild(div_date);
            div.appendChild(div_cont);
            div.appendChild(p_contenu);
            const list = document.getElementById("output");
            list.insertBefore(div, list.children[0]);
        })

        document.getElementById("titre").value = " "; // vide l'input
        document.getElementById("contenu").value = " ";
    } else {
        console.log("aucune nouvelle entrée trouvée")
    }
}

// fonction pour fetch la méthode 'journal' GET
function fetchAllJournal() {
    console.log("Hello world, la fonction journal GET marche!"); 
    fetch("journal", {
        "method": "GET",
        "headers": {"Content-Type": "application/json"},
    })
    .then(response => response.json())
    .then(responseObj => {
        console.log(responseObj)
        
        responseObj.forEach((entry) => {
            console.log(entry)

            let div = document.createElement("div");
            div.classList.add("journal_container");
            div.id = entry.ID;

            // titre
            div_titre = document.createElement("div");
            div_titre.classList.add("titre_class");
            div_titre.innerText = entry.Journal_titre;

            // date
            let div_date = document.createElement("div");
            div_date.classList.add("date_class");
            div_date.innerText = entry.Journal_date;
            
            // div titre-date container
            let div_cont = document.createElement("div");
            div_cont.classList.add("div_container");

            // contenu
            let p_contenu = document.createElement("p");
            p_contenu.innerText = entry.Journal_contenu;
            p_contenu.classList.add("p_contenu");
            
            div_cont.appendChild(div_titre);
            div_cont.appendChild(div_date);
            div.appendChild(div_cont);
            div.appendChild(p_contenu);
            const list = document.getElementById("output");
            list.insertBefore(div, list.children[0]);
        })
    })
}
