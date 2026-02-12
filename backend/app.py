from flask import Flask, request, jsonify
import openai
import datetime

app = Flask(__name__)

# Configure OpenAI API key
openai.api_key = 'YOUR_OPENAI_API_KEY'

@app.route('/process_email', methods=['POST'])
def process_email():
    data = request.json
    email_content = data.get('email_content', '')

    # Call ChatGPT to process the email
    response = openai.ChatCompletion.create(
        model='gpt-3.5-turbo',
        messages=[{'role': 'user', 'content': email_content}]
    )
    processed_content = response['choices'][0]['message']['content']

    return jsonify({'processed_content': processed_content})

@app.route('/add_event', methods=['POST'])
def add_event():
    data = request.json
    event_details = data.get('event_details', {})
    event_time = event_details.get('time')

    # Integrate with Google Calendar API (pseudo code)
    # google_calendar.add_event(event_details)

    return jsonify({'status': 'Event added to Google Calendar'})

if __name__ == '__main__':
    app.run(debug=True)