
//------------------//

// Journal //
// Boutons
function newEntry() {
  // crée nouvel élément sous 'para'
  const para = document.createElement("textarea");
  // ajoute le nouvel élément (para) à l'élément de page dont l'id est #MainPage
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

// pour récup les header + footer ----------------------------------
// Function to load HTML content into a target element
async function loadHTML(elementId, filePath) {
  try {
    // Fetch the external HTML file
    const response = await fetch(filePath);
    
    // Check if the request was successful
    if (!response.ok) {
      throw new Error(`Failed to load ${filePath}: ${response.statusText}`);
    }
    
    // Extract HTML text from the response
    const html = await response.text();
    
    // Insert the HTML into the target element
    const element = document.getElementById(elementId);
    if (element) {
      element.innerHTML = html;
    } else {
      throw new Error(`Element with ID "${elementId}" not found`);
    }
  } catch (error) {
    console.error('Error loading content:', error);
    // Optional: Display a fallback message in the UI
    document.getElementById(elementId)?.innerHTML = `<p>Error loading content.</p>`;
  }
}
 
// Load header and footer when the DOM is fully loaded
document.addEventListener('DOMContentLoaded', () => {
  loadHTML('header', 'header.html'); // Load header into #header
  loadHTML('footer', 'footer.html'); // Load footer into #footer
});
// Inside includes.js, after inserting the header HTML:
async function loadHTML(elementId, filePath) {
  try {
    // ... (previous fetch code) ...
 
    // After inserting HTML, initialize dynamic elements
    if (elementId === 'header') {
      initHeaderEvents(); // Call a function to set up header interactions
    }
  } catch (error) {
    // ... (error handling) ...
  }
}
 
// Initialize header event listeners
function initHeaderEvents() {
  const themeToggle = document.getElementById('theme-toggle');
  if (themeToggle) {
    themeToggle.addEventListener('click', () => {
      document.body.classList.toggle('dark-mode');
    });
  }
}
//--------------------------------------