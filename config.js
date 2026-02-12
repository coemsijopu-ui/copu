// config.js

const config = {
    chatGPT: {
        apiKey: 'YOUR_CHATGPT_API_KEY', // Replace with your ChatGPT API key
        endpoint: 'https://api.openai.com/v1/chat/completions',
    },
    googleCalendar: {
        apiKey: 'YOUR_GOOGLE_CALENDAR_API_KEY', // Replace with your Google Calendar API key
        clientID: 'YOUR_GOOGLE_CLIENT_ID', // Replace with your Google client ID
        clientSecret: 'YOUR_GOOGLE_CLIENT_SECRET', // Replace with your Google client secret
    }
};

module.exports = config;