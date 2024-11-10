from flask import Flask, request, abort, jsonify
from classifier import Classifier
from response_generator import generate_response
from config import MAX_REQUESTS, TIME_WINDOW, API_KEY
from MIddleware import rateLimiter

app = Flask(__name__)
classifier = Classifier()


def check_api_key():
    """Function to check if the API key is correct."""
    api_key = request.headers.get('X-API-Key')  # You can use any custom header name here, like 'X-API-Key'
    if api_key != f"{API_KEY}":  # Match the API key with 'Bearer <api_key>'
        abort(403)


@app.route('/classify', methods=['POST'])
def classify():
    check_api_key()

    ip_address = request.remote_addr  # Get the IP address of the client
    if not rateLimiter.rate_limiter(ip_address, MAX_REQUESTS, TIME_WINDOW):
        return jsonify({"error": "Rate limit exceeded. Please try again later."}), 429

    data = request.get_json()
    query = data.get("query")

    result = classifier.classify(query)
    generated_response = generate_response(result)

    response = {
        "result": result,
        "generatedResponse": generated_response
    }

    # Return the result as JSON
    return response


@app.errorhandler(403)
def forbidden_error(error):
    """Return custom 403 error message in JSON format."""
    response = {
        "error": "Forbidden",
        "message": "Invalid API Key"
    }
    return jsonify(response), 403


if __name__ == '__main__':
    app.run(debug=True)
