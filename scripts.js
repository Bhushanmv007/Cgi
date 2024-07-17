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

    const src = cv.matFromImageData(imgData);
    const dst = new cv.Mat();

    switch (operation) {
        case 'gaussianBlur':
            const ksize = new cv.Size(15 * intensity, 15 * intensity);
            cv.GaussianBlur(src, dst, ksize, 0, 0, cv.BORDER_DEFAULT);
            break;
        case 'medianBlur':
            cv.medianBlur(src, dst, 15 * intensity);
            break;
        case 'sharpen':
            const kernel = cv.matFromArray(3, 3, cv.CV_32F, [
                0, -1, 0,
                -1, 5 + intensity, -1,
                0, -1, 0
            ]);
            cv.filter2D(src, dst, cv.CV_8U, kernel);
            kernel.delete();
            break;
        case 'edgeDetection':
            cv.Canny(src, dst, 100 * intensity, 200 * intensity);
            break;
        case 'noiseReduction':
            cv.fastNlMeansDenoisingColored(src, dst, 10 * intensity, 10 * intensity, 7, 21);
            break;
        case 'brightnessAdjustment':
            src.convertTo(dst, -1, 1, 30 * intensity);
            break;
        case 'contrastAdjustment':
            src.convertTo(dst, -1, 1 + intensity, 0);
            break;
        case 'histogramEqualization':
            cv.cvtColor(src, dst, cv.COLOR_RGBA2GRAY);
            cv.equalizeHist(dst, dst);
            cv.cvtColor(dst, dst, cv.COLOR_GRAY2RGBA);
            break;
        case 'saturationAdjustment':
            cv.cvtColor(src, dst, cv.COLOR_RGBA2RGB);
            cv.cvtColor(dst, dst, cv.COLOR_RGB2HSV);
            const hsvPlanes = new cv.MatVector();
            cv.split(dst, hsvPlanes);
            let s = hsvPlanes.get(1);
            s.convertTo(s, -1, intensity, 0);
            cv.merge(hsvPlanes, dst);
            cv.cvtColor(dst, dst, cv.COLOR_HSV2RGB);
            cv.cvtColor(dst, dst, cv.COLOR_RGB2RGBA);
            s.delete();
            hsvPlanes.delete();
            break;
        case 'gammaCorrection':
            const lookUpTable = new cv.Mat(1, 256, cv.CV_8U);
            const data = lookUpTable.data;
            for (let i = 0; i < 256; i++) {
                data[i] = Math.pow(i / 255.0, 1.0 / intensity) * 255.0;
            }
            cv.LUT(src, lookUpTable, dst);
            lookUpTable.delete();
            break;
        default:
            dst.delete();
            return;
    }

    cv.imshow('canvas', dst);
    src.delete();
    dst.delete();
}
