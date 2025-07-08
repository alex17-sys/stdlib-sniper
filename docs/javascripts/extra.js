// Custom JavaScript for stdlib-sniper
document.addEventListener('DOMContentLoaded', function() {
    // Add copy button to code blocks
    const codeBlocks = document.querySelectorAll('pre code');
    codeBlocks.forEach(function(block) {
        const button = document.createElement('button');
        button.innerHTML = '<span>'
            + '<svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-copy" viewBox="0'
            + '  <path fill-rule="evenodd" d="M4 2a2 2 0 0 1 2-2h8a2 2 0 0 1 2 2v8a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2zm2-1a1 1 0 0 0-1 1v8a1 1 0 0 0 1 1h8a1 1 0 0 0 1-1V2a1 1 0 0 0-1-1zM2 5a1 1 0 0 0-1 1v8a1 1 0 0 0 1 1h8a1 1 0 0 0 1-1v-1h1v1a2 2 0 0 1-2 2H2a2 2 0 0 1-2-2V6a2 2 0 0 1 2'
            + '</svg>'
            + '</span>';
        // Tooltip
        const tooltip = document.createElement('span');
        button.appendChild(tooltip);
        button.onclick = function() {
            navigator.clipboard.writeText(block.textContent);
            button.classList.add('copied');
            setTimeout(() => {
                button.classList.remove('copied');
            }, 1000);
        };
        // Insert button as first child of pre (so it's top-right)
        block.parentNode.style.position = 'relative';
        block.parentNode.insertBefore(button, block.parentNode.firstChild);
    });

    // Add tag filtering
    const tags = document.querySelectorAll('.md-badge');
    tags.forEach(function(tag) {
        tag.style.cursor = 'pointer';
        tag.onclick = function() {
            const tagText = this.textContent;
            // Filter snippets by tag (could be enhanced)
            console.log('Filter by tag:', tagText);
        };
    });
});
