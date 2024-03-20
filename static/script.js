async function loadModel() {
    const model = await tf.loadLayersModel('https://teachablemachine.withgoogle.com/models/blAMVc866/model.json');
    return model;
}

// Define a mapping of numerical labels to human-readable labels
const labelMapping = {
    0: 'Credit Card',
    1: 'Debit Card',
    2: 'ID Card'
    // Add more labels as per your model's output
};

async function classify() {
    const model = await loadModel();
    const inputElement = document.getElementById('image-input');
    const image = inputElement.files[0];

    if (image) {
        const reader = new FileReader();
        reader.onload = async function() {
            const img = new Image();
            img.src = reader.result;
            img.onload = async function() {
                const canvas = document.createElement('canvas');
                canvas.width = 224;
                canvas.height = 224;
                const ctx = canvas.getContext('2d');
                ctx.drawImage(img, 0, 0, 224, 224);
                const tensor = tf.browser.fromPixels(canvas).toFloat().expandDims();
                const prediction = await model.predict(tensor).data();
                const resultElement = document.getElementById('result');
                // Convert numerical prediction to human-readable label
                const label = labelMapping[prediction.indexOf(Math.max(...prediction))];
                resultElement.innerText = 'Prediction: ' + label;
            }
        }
        reader.readAsDataURL(image);
    } else {
        alert('Please select an image.');
    }
}











// async function loadModel() {
//     const model = await tf.loadLayersModel('https://teachablemachine.withgoogle.com/models/blAMVc866/model.json');
//     return model;
// }

// async function classify() {
//     const model = await loadModel();
//     const inputElement = document.getElementById('image-input');
//     const image = inputElement.files[0];

//     if (image) {
//         const reader = new FileReader();
//         reader.onload = async function() {
//             const img = new Image();
//             img.src = reader.result;
//             img.onload = async function() {
//                 const canvas = document.createElement('canvas');
//                 canvas.width = 224;
//                 canvas.height = 224;
//                 const ctx = canvas.getContext('2d');
//                 ctx.drawImage(img, 0, 0, 224, 224);
//                 const tensor = tf.browser.fromPixels(canvas).toFloat().expandDims();
//                 const prediction = await model.predict(tensor).data();
//                 const resultElement = document.getElementById('result');
//                 resultElement.innerText = 'Prediction: ' + prediction;
//             }
//         }
//         reader.readAsDataURL(image);
//     } else {
//         alert('Please select an image.');
//     }
// }
