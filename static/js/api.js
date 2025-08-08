// Fetch content of a text file
async function fetchTextFile(filename) {
    const response = await fetch(`/dictionary/${filename}`);
    if (!response.ok) throw new Error(`Failed to load file: ${filename}`);
    return response.text();
}

// Generate sentence based on selected word and level
async function generateSentence(wordPairString, level) {
    const response = await fetch('/', {
        method: 'POST',
        headers: { 'Content-Type': 'application/x-www-form-urlencoded' },
        body: new URLSearchParams({ word: wordPairString, level })
    });

    if (!response.ok) throw new Error(`Server error: ${response.status}`);
    return response.json();
}
