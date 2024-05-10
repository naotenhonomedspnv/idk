fetch('https://rawcdn.githack.com/naotenhonomedspnv/idk/d57de3b5dc39cae3c716b96c4650e7afc6f5a023/main.html')
    .then(response => response.text())
    .then(html => {
        const parser = new DOMParser();
        const doc = parser.parseFromString(html, 'text/html');
        const value = doc.getElementById('valueContainer').innerText;
        console.log(value); // This will log "Hello, world!" in the console
    });
