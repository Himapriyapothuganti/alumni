// Function to send a message
function sendMessage() {
    const inputElement = document.getElementById('message-input');
    const messageText = inputElement.value.trim();

    if (messageText !== '') {
        fetch('/send_message', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ message: messageText })
        })
        .then(response => response.json())
        .then(data => {
            console.log(data); // Log success or error message from Flask
            // Refresh messages after sending
            fetchMessages();
        })
        .catch(error => console.error('Error:', error));
    }
}

// Function to fetch messages
function fetchMessages() {
    fetch('/fetch_messages')
        .then(response => response.json())
        .then(data => {
            console.log(data); // Log fetched messages
            // Update messages array with fetched data (assuming messages is a global variable)
            messages = data;
            // Re-display messages with new data (assuming displayMessages() is defined elsewhere)
            displayMessages();
        })
        .catch(error => console.error('Error:', error));
}
