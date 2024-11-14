// Load dictionary data from text files
async function loadDictionary() {
    try {
        const [deWords, trWords, types] = await Promise.all([
            fetchTextFile('de.txt'),
            fetchTextFile('tr.txt'),
            fetchTextFile('types.txt')
        ]);

        const deArray = deWords.split('\n').map(word => word.trim()).filter(Boolean);
        const trArray = trWords.split('\n').map(word => word.trim()).filter(Boolean);
        const typesArray = types.split('\n').map(type => type.trim()).filter(Boolean);

        // Store word data globally for search and display purposes
        window.wordData = deArray.map((deWord, index) => ({
            deWord,
            trWord: trArray[index] || '',
            type: typesArray[index] || ''
        }));

        displayWords(window.wordData); // Initially display all words
    } catch (error) {
        console.error('Error loading dictionary:', error);
        alert('Error loading dictionary. Please try again later.');
    }
}

// Fetch content of a text file
async function fetchTextFile(filename) {
    const response = await fetch(`/dictionary/${filename}`);
    if (!response.ok) throw new Error(`Failed to load file: ${filename}`);
    return response.text();
}

// Display words in the word list
function displayWords(wordData) {
    const wordListContainer = document.getElementById('word-list');
    wordListContainer.innerHTML = ''; // Clear previous content

    wordData.forEach(item => {
        const wordItem = document.createElement('div');
        wordItem.classList.add('word-item');
        wordItem.innerHTML = `
            <strong>${item.deWord}</strong> → ${item.trWord} <span>[${item.type}]</span>
            <div class="word-content" id="content-${item.deWord}" style="display: none;">
                <div class="level-select">
                    <label for="level-${item.deWord}">Seviye Seçin:</label>
                    <select id="level-${item.deWord}" class="level-selector">
                        <option value="A1">A1 - Başlangıç Seviyesi</option>
                        <option value="A2">A2 - Temel Seviye</option>
                        <option value="B1">B1 - Orta Seviye</option>
                        <option value="B2">B2 - Orta Üstü Seviye</option>
                        <option value="C1">C1 - İleri Seviye</option>
                        <option value="C2">C2 - Usta Seviye</option>
                    </select>
                </div>
                <button class="generate-btn" data-de-word="${item.deWord}">Cümle Oluştur</button>
                <div class="generated-sentence" id="sentence-${item.deWord}" style="display: none;">
                    <div class="loading-spinner" id="loading-${item.deWord}" style="display: none;">
                        <div class="spinner"></div>
                        <span>Yükleniyor...</span>
                    </div>
                </div>
            </div>
        `;

        wordItem.onclick = (event) => {
            if (!event.target.closest('.level-select') && !event.target.closest('.generate-btn')) {
                toggleContentDisplay(item.deWord, wordItem);
            }
        };

        wordListContainer.appendChild(wordItem);
    });

    document.querySelectorAll('.generate-btn').forEach(button => {
        button.addEventListener('click', () => {
            const deWord = button.dataset.deWord;
            handleGenerateSentence(deWord).catch(error => {
                console.error('Error generating sentence:', error);
                showErrorInSentenceContainer(deWord, 'Cümle oluşturulamadı.');
            });
        });
    });
}

// Toggle word content display
function toggleContentDisplay(deWord, wordItem) {
    const content = document.getElementById(`content-${deWord}`);
    content.style.display = content.style.display === 'none' ? 'block' : 'none';
    wordItem.classList.toggle('expanded');
}

// Filter words based on search input
function filterWords(searchQuery) {
    const filteredWords = window.wordData.filter(item =>
        [item.deWord, item.trWord, item.type].some(word =>
            word.toLowerCase().includes(searchQuery.toLowerCase())
        )
    );
    displayWords(filteredWords.length > 0 ? filteredWords : window.wordData);
}

// Add event listener for real-time search
document.querySelector('.search-bar').addEventListener('input', (event) => {
    filterWords(event.target.value);
});

// Generate sentence based on selected word and level
async function handleGenerateSentence(deWord) {
    const sentenceContainer = document.getElementById(`sentence-${deWord}`);
    const levelSelector = document.getElementById(`level-${deWord}`);
    const level = levelSelector.value;

    showLoadingSpinner(sentenceContainer);

    try {
        const response = await fetch('/', {
            method: 'POST',
            headers: { 'Content-Type': 'application/x-www-form-urlencoded' },
            body: new URLSearchParams({ word: deWord, level })
        });

        if (!response.ok) throw new Error(`Server error: ${response.status}`);

        const data = await response.json();
        displayGeneratedSentence(sentenceContainer, data.sentence, data.translated_sentence);
    } catch (error) {
        showErrorInSentenceContainer(deWord, error.message);
    }
}

// Show loading spinner while generating sentence
function showLoadingSpinner(container) {
    container.style.display = 'block';
    container.innerHTML = `
        <div class="loading-spinner">
            <div class="spinner"></div>
            <span>Yükleniyor...</span>
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

// Load the dictionary on page load
window.onload = loadDictionary;
