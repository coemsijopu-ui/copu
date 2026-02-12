// popup.js

// This script handles the popup button click and communicates with the content script

document.addEventListener('DOMContentLoaded', function () {
    const button = document.getElementById('popup-button');
    button.addEventListener('click', function () {
        // Communication with content script
        chrome.runtime.sendMessage({ action: 'popupButtonClicked' }, function (response) {
            console.log('Response from content script:', response);
        });
    });
});