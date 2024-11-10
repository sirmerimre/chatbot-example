from flask import Flask, request, jsonify
from transformers import pipeline

app = Flask(__name__)

# Load zero-shot classification pipeline with a pre-trained model
classifier = pipeline("zero-shot-classification", model="facebook/bart-large-mnli")

# Predefined candidate labels
candidate_labels = ["policy_coverage", "exclusions", "claims_process", "cancellation"]

# Function to classify the user's query intent
def classify_intent(user_query):
    result = classifier(user_query, candidate_labels)
    # The label with the highest score is the classified intent
    intent = result['labels'][0]
    return intent

# Generate response based on the identified intent
def generate_response(user_query):
    intent = classify_intent(user_query)

    if intent == "policy_coverage":
        response = "Your travel insurance policy generally covers medical expenses, trip cancellations, and luggage loss. Please check specific policy terms for more detailed information."
    elif intent == "exclusions":
        response = "Exclusions typically include pre-existing conditions, risky activities, and pandemics. Review your policy's exclusions section for a full list."
    elif intent == "claims_process":
        response = "To file a claim, log in to your account, complete the claim form, and submit required documents. The claim processing time varies, usually taking 1-2 weeks."
    elif intent == "cancellation":
        response = "To cancel a policy..."
    else:
        response = "I'm sorry, I didn't understand that. Could you clarify your question about travel insurance?"

    return response


# Main chatbot function
def travel_insurance_chatbot():
    print("Welcome to the Travel Insurance Chatbot!")
    print("Ask me about your policy coverage, exclusions, or claims process.")

    while True:
        user_query = input("You: ")
        if user_query.lower() in ["exit", "quit"]:
            print("Chatbot: Thank you for using the Travel Insurance Chatbot. Goodbye!")
            break

        response = generate_response(user_query)
        print("Chatbot:", response)


@app.route('/classify', methods=['POST'])
def classify():
    # Get the input data (user's query)
    data = request.get_json()
    query = data.get("query")

    # Define candidate labels (example for an insurance chatbot)
    candidate_labels = ["policy_coverage", "exclusions", "claims_process"]

    # Perform zero-shot classification
    result = classifier(query, candidate_labels)
    generatedResponse = generate_response(query)

    response = {
        "result": result,
        "generatedResponse": generatedResponse
    }

    # Return the result as JSON
    return response

if __name__ == '__main__':
    app.run(debug=True)
