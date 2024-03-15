from flask import Flask, request, jsonify
import openai
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# OpenAI API key
openai.api_key = os.getenv('OPENAI_API_KEY')

app = Flask(__name__)

@app.route('/complete_chat', methods=['POST'])
def complete_chat():
    try:
        # Parse request data    
        data = request.get_json()

        # Check if data is valid JSON
        if not data:
            raise ValueError("Invalid input. Request data is not valid JSON.")

        # Check if 'partial_text' field is present
        if 'partial_text' not in data:
            raise ValueError("Invalid input. 'partial_text' field is missing.")
        
        # Check if 'partial_text' field is empty
        if not data['partial_text'].strip():
            raise ValueError("Invalid input. 'partial_text' field is empty.")

        user_input = data["partial_text"]

        # Prepare prompt
        prompt = f"User Input: {user_input}"

        # Call OpenAI chat completion API
        response = openai.Completion.create(
            model="gpt-3.5-turbo-instruct",
            prompt=prompt,
            max_tokens=150
        )

        # Extract generated text from response
        generated_text = response.choices[0].text.strip()

        # Return response
        return jsonify({"completed_text": generated_text})

    except ValueError as ve:
            return jsonify({"error": str(ve)}), 400
    except Exception as e:
            return jsonify({"error": "An unexpected error occurred."}), 500

if __name__ == '__main__':
  app.run(debug=True)
