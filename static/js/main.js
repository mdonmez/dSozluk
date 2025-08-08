// Main application logic
document.addEventListener('DOMContentLoaded', () => {
    // State
    let wordData = [];

    // Elements
    const wordListContainer = document.getElementById('word-list');
    const searchBar = document.querySelector('.search-bar');

    // Load dictionary data
    async function loadDictionary() {
        try {
            const [deWords, trWords] = await Promise.all([
                fetchTextFile('de.txt'),
                fetchTextFile('tr.txt')
            ]);

            const deArray = processWordList(deWords);
            const trArray = processWordList(trWords);

            wordData = deArray.map((deWord, index) => ({
                deWord,
                trWord: trArray[index] || ''
            }));

            displayWords(wordData, wordListContainer);
            addEventListeners();
        } catch (error) {
            console.error('Error loading dictionary:', error);
            alert('Error loading dictionary. Please try again later.');
        }
    }

    // Process word list
    function processWordList(words) {
        return words.split('\n').map(word => word.trim()).filter(Boolean);
    }

    // Add event listeners
    function addEventListeners() {
        wordListContainer.addEventListener('click', (event) => {
            const target = event.target;
            const wordItem = target.closest('.word-item');
            if (!wordItem) return;

            const deWord = wordItem.querySelector('.generate-btn').dataset.deWord;

            if (target.classList.contains('generate-btn')) {
                handleGenerateSentence(deWord);
            } else if (!target.closest('.level-select')) {
                toggleContentDisplay(deWord, wordItem);
            }
        });

        searchBar.addEventListener('input', (event) => {
            filterWords(event.target.value);
        });
    }

    // Filter words
    function filterWords(searchQuery) {
        const appExplanation = document.querySelector('.app-explanation');
        const footer = document.querySelector('footer');

        appExplanation.style.display = searchQuery ? 'none' : 'block';
        footer.style.display = searchQuery ? 'none' : 'block';

        const filteredWords = wordData.filter(item =>
            [item.deWord, item.trWord].some(word =>
                word.toLowerCase().includes(searchQuery.toLowerCase())
            )
        );
        displayWords(filteredWords.length > 0 ? filteredWords : wordData, wordListContainer);
    }

    // Handle sentence generation
    async function handleGenerateSentence(deWord) {
        const sentenceContainer = document.getElementById(`sentence-${deWord}`);
        const levelSelector = document.getElementById(`level-${deWord}`);
        const level = levelSelector.value;

        const wordPair = wordData.find(item => item.deWord === deWord);
        if (!wordPair) {
            showErrorInSentenceContainer(deWord, 'Kelime eşleştirme hatası.');
            return;
        }

        const wordPairString = `${wordPair.deWord}|${wordPair.trWord}`;
        showLoadingSpinner(sentenceContainer);

        try {
            const data = await generateSentence(wordPairString, level);
            displayGeneratedSentence(sentenceContainer, data.sentence, data.translated_sentence);
        } catch (error) {
            showErrorInSentenceContainer(deWord, error.message);
        }
    }

    // Initial load
    loadDictionary();
});
