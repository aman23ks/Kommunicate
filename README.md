
# Kommunicate API Project - Backend Interview

This project implements a Flask-based API that utilizes the OpenAI API to provide chat completion functionality. Users can submit partial text prompts, and the API will generate a continuation using the specified OpenAI model.


## API Overview

#### Endpoint

```http
  POST /complete_chat
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `partial_text` | `string` | **Required** |

#### Request Payload (JSON):
`partial_text (string, required)` 

The initial text prompt for chat completion.

#### Response (JSON):
`completed_text (string)`

The generated text continuation for the provided prompt.

`error (string, optional)`

Contains an error message if the request fails (e.g., invalid input, unexpected error).

#### Status Codes
`200: Success` - The request was processed successfully, and a response is returned.

`400: Bad Request` - The request could not be processed due to 
invalid input (e.g., missing required field, invalid JSON).

`500: Internal Server Error` - An unexpected error occurred during processing.
## Environment Variables

To run this project, you will need to add the following environment variables to your .env file

`OPENAI_API_KEY`


## Installation
#### Install dependencies using pip
`pip install flask openai python-dotenv requests pytest flask-pytest`
## Running the app
#### Start the Flask development server
`flask run`

This will run the API on `http://127.0.0.1:5000/`.
## Testing
This project includes unit tests (using `pytest`) and an integration test (using `requests`) to ensure functionality

#### Unit Tests `(test_api.py)`
These tests verify the API's behavior for various input scenarios, including valid, empty, invalid JSON, and missing field cases.

#### Integration Test `(test_integration.py)`
This test simulates a client request to the `/complete_chat` endpoint and asserts the expected response structure and content.

#### To run the tests - 

`pytest test_api.py` for running unit tests (type in terminal).

`pytest test_integration.py` for running integration tests (type in terminal).
