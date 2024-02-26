function getClothingSuggestion() {
    // Get input values
    var skinColor = document.getElementById('skinColor').value;
    var occasion = document.getElementById('occasion').value;
    var gender = document.getElementById('gender').value;

    // Send input values to Flask backend using fetch
    fetch(`/suggest-clothing?skinColor=${skinColor}&occasion=${occasion}&gender=${gender}`)
    .then(response => response.json())
    .then(data => {
        // Display suggestion in the output div
        document.getElementById('output').innerHTML = `<p>${data.suggestion}</p>`;
    })
    .catch(error => console.error('Error:', error));
}
