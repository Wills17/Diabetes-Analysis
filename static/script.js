// Load and display prediction result (for result.html)
document.addEventListener('DOMContentLoaded', function() {
    // Get the container elements
    const iconWrapper = document.querySelector('.result-icon');
    const iconSvg = iconWrapper ? iconWrapper.querySelector('svg') : null;
    const statusTitle = document.querySelector('.result-status-title');
    const statusDescription = document.querySelector('.result-status-description');
    const modelNameEl = document.querySelector('.result-model');

    // These values are injected by Flask (via Jinja templating)
    const risk = document.body.getAttribute('data-risk');   // "true" or "false"
    const model = document.body.getAttribute('data-model'); // "logreg" or "knn"
    const modelName = model === 'logreg' ? 'Logistic Regression' : 'K-Nearest Neighbors';

    if (modelNameEl) {
        modelNameEl.textContent = `Model: ${modelName}`;
    }

    if (!iconWrapper || !iconSvg || !statusTitle || !statusDescription) return;

    if (risk === 'true') {
        // Diabetic
        iconWrapper.className = 'result-icon result-icon-warning';
        iconSvg.innerHTML =
            '<path d="M10.29 3.86L1.82 18a2 2 0 0 0 1.71 3h16.94a2 2 0 0 0 1.71-3L13.71 3.86a2 2 0 0 0-3.42 0z"></path><line x1="12" y1="9" x2="12" y2="13"></line><line x1="12" y1="17" x2="12.01" y2="17"></line>';
        statusTitle.textContent = 'Diabetes Risk Detected';
        statusTitle.className = 'result-status-title result-status-warning';
        statusDescription.textContent =
            'The analysis indicates potential diabetes risk. Please consult with a healthcare professional for proper diagnosis and treatment.';
    } else {
        // No diabetes
        iconWrapper.className = 'result-icon result-icon-success';
        iconSvg.innerHTML =
            '<path d="M22 11.08V12a10 10 0 1 1-5.93-9.14"></path><polyline points="22 4 12 14.01 9 11.01"></polyline>';
        statusTitle.textContent = 'No Diabetes Detected';
        statusTitle.className = 'result-status-title result-status-success';
        statusDescription.textContent =
            'Great news! Based on the provided health indicators, the patient shows no signs of diabetes.';
    }
});
