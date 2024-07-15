document.getElementById('upload').addEventListener('change', loadImage);

function loadImage(event) {
    const file = event.target.files[0];
    if (file) {
        const reader = new FileReader();
        reader.onload = function(e) {
            const img = new Image();
            img.onload = function() {
                const canvas = document.getElementById('canvas');
                const ctx = canvas.getContext('2d');
                canvas.width = img.width;
                canvas.height = img.height;
                ctx.drawImage(img, 0, 0);
                document.getElementById('options').style.display = 'block';
            }
            img.src = e.target.result;
        }
        reader.readAsDataURL(file);
    }
}

function processImage() {
    const operation = document.getElementById('operation').value;
    const intensity = parseFloat(document.getElementById('intensity').value);
    const canvas = document.getElementById('canvas');
    const ctx = canvas.getContext('2d');
    const imgData = ctx.getImageData(0, 0, canvas.width, canvas.height);
    // Placeholder for image processing
    // Here you would implement the image processing based on the selected operation and intensity
    console.log(`Operation: ${operation}, Intensity: ${intensity}`);
    ctx.putImageData(imgData, 0, 0);
}
