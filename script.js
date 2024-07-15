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
    
    if (intensity < 0 || intensity > 5 || isNaN(intensity)) {
        alert("Invalid intensity value. Please enter a number between 0 and 5.");
        return;
    }

    // Example: Apply a simple operation (just for demonstration)
    if (operation === 'gaussianBlur') {
        const kernelSize = Math.round(3 * intensity);
        const kernel = [];
        for (let i = 0; i < kernelSize; i++) {
            kernel.push(Array(kernelSize).fill(1 / (kernelSize * kernelSize)));
        }
        convolve(imgData, kernel);
    }

    ctx.putImageData(imgData, 0, 0);
}

function convolve(imgData, kernel) {
    const src = imgData.data;
    const sw = imgData.width;
    const sh = imgData.height;
    const dst = new Uint8ClampedArray(src);
    const kw = kernel.length;
    const kh = kernel[0].length;
    const halfKw = Math.floor(kw / 2);
    const halfKh = Math.floor(kh / 2);

    for (let y = 0; y < sh; y++) {
        for (let x = 0; x < sw; x++) {
            let r = 0, g = 0, b = 0, a = 0;
            for (let ky = 0; ky < kh; ky++) {
                for (let kx = 0; kx < kw; kx++) {
                    const px = x + kx - halfKw;
                    const py = y + ky - halfKh;
                    if (px >= 0 && px < sw && py >= 0 && py < sh) {
                        const srcPos = (py * sw + px) * 4;
                        const wt = kernel[ky][kx];
                        r += src[srcPos] * wt;
                        g += src[srcPos + 1] * wt;
                        b += src[srcPos + 2] * wt;
                        a += src[srcPos + 3] * wt;
                    }
                }
            }
            const dstPos = (y * sw + x) * 4;
            dst[dstPos] = r;
            dst[dstPos + 1] = g;
            dst[dstPos + 2] = b;
            dst[dstPos + 3] = a;
        }
    }

    imgData.data.set(dst);
}
