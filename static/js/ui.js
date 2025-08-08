// Display words in the word list
function displayWords(wordData, wordListContainer) {
    wordListContainer.innerHTML = ''; // Clear previous content

    // Create and display word items dynamically
    wordData.forEach(item => {
        const wordItem = createWordItem(item);
        wordListContainer.appendChild(wordItem);
    });
}

// Create individual word item for display
function createWordItem(item) {
    const wordItem = document.createElement('div');
    wordItem.classList.add('word-item');
    wordItem.innerHTML = `
        <strong>${item.deWord}</strong> → ${item.trWord}
        <div class="word-content" id="content-${item.deWord}" style="display: none;">
            ${createLevelSelector(item.deWord)}
            <button class="generate-btn" data-de-word="${item.deWord}">Cümle Oluştur</button>
            <div class="generated-sentence" id="sentence-${item.deWord}" style="display: none;">
                <div class="loading-spinner" id="loading-${item.deWord}" style="display: none;">
                    <div class="spinner"></div>
                    <span>Cümle oluşturuluyor...</span>
                </div>
            </div>
        </div>
    `;
    return wordItem;
}

// Create level selector dropdown for word
function createLevelSelector(deWord) {
    return `
        <div class="level-select">
            <label for="level-${deWord}">Seviye Seçin:</label>
            <select id="level-${deWord}" class="level-selector">
                <option value="A1">A1 - Başlangıç Seviyesi</option>
                <option value="A2">A2 - Temel Seviye</option>
                <option value="B1">B1 - Orta Seviye</option>
                <option value="B2">B2 - Orta Üstü Seviye</option>
                <option value="C1">C1 - İleri Seviye</option>
                <option value="C2">C2 - Usta Seviye</option>
            </select>
        </div>
    `;
}

// Toggle word content display
function toggleContentDisplay(deWord, wordItem) {
    const content = document.getElementById(`content-${deWord}`);
    content.style.display = content.style.display === 'none' ? 'block' : 'none';
    wordItem.classList.toggle('expanded');
}

// Show loading spinner while generating sentence
function showLoadingSpinner(container) {
    container.style.display = 'block';
    container.innerHTML = `
        <div class="loading-spinner">
            <div class="spinner"></div>
            <span>Cümle oluşturuluyor...</span>
        </div>
    `;
}

// Display generated sentence
function displayGeneratedSentence(container, germanSentence, turkishSentence) {
    container.innerHTML = `
        <div>
            <strong>Almanca:</strong> ${germanSentence}<br>
            <strong>Türkçe:</strong> ${turkishSentence}
        </div>
    `;
}

// Show error in sentence container
function showErrorInSentenceContainer(deWord, errorMessage) {
    const sentenceContainer = document.getElementById(`sentence-${deWord}`);
    sentenceContainer.innerHTML = `<div><strong>Hata:</strong> ${errorMessage}</div>`;
}
