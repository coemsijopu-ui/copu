// background.js

// This file handles background tasks and acts as a message relay between popup and content scripts.

// Listener for messages from popup
chrome.runtime.onMessage.addListener(function(request, sender, sendResponse) {
    // Process request from popup
    if (request.message === 'popupMessage') {
        console.log('Received message from popup:', request.data);
        // Relay message to content scripts
        chrome.tabs.query({active: true, currentWindow: true}, function(tabs) {
            chrome.tabs.sendMessage(tabs[0].id, {message: 'relayMessage', data: request.data});
        });
    }
});

// Listener for messages from content scripts
chrome.runtime.onMessage.addListener(function(request, sender, sendResponse) {
    if (request.message === 'contentMessage') {
        console.log('Received message from content script:', request.data);
        // Process the message from content script
        // You can send response back if needed
    }
});
