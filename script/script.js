async function getOutfit() {
    const gender = document.getElementById('gender').value;
    const skin_color = document.getElementById('skinColor').value;
    const bodyType = document.getElementById('bodyType').value;
    const occasion = document.getElementById('occasion').value;
    const size = document.getElementById('size').value;
  
    try {
      const response = await fetch('http://localhost:5000/get_outfit', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ gender,skin_color, bodyType, occasion,size }),
      });
  
      const data = await response.json();
  
      const outputDiv = document.getElementById('output');
      outputDiv.innerHTML = `<p>${data.result}</p>`;
    } catch (error) {
      console.error('Error:', error);
    }
}
  