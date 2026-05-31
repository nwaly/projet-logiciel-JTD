// check si le lien au script marche//
// console.log("JavaScript file linked successfully!");  
// alert("Hello from Flask + JavaScript!");

//----------Header----------//

// affiche la date actuelle
const d = new Date();
const month = ["Janvier","Février","Mars","Avril","Mai","Juin","Juillet","Août","Septembre","Octobre","Novembre","Décembre"];
let month_name = month[d.getMonth()];
document.getElementById("today").innerHTML = d.getDate().toString()+" "+month_name+" "+d.getFullYear().toString();

