def generate_response(valid_results):

    if not valid_results:
        return "I'm sorry, I didn't understand that. Could you clarify your question about travel insurance?"

    intent = valid_results[0]['label']

    # Generate response based on intent
    if intent == "policy coverage":
        response = "Your travel insurance policy generally covers medical expenses, trip cancellations, and luggage loss. Please check specific policy terms for more detailed information."
    elif intent == "exclusions":
        response = "Exclusions typically include pre-existing conditions, risky activities, and pandemics. Review your policy's exclusions section for a full list."
    elif intent == "claims process":
        response = "To file a claim, log in to your account, complete the claim form, and submit required documents. The claim processing time varies, usually taking 1-2 weeks."
    elif intent == "cancellation":
        response = "To cancel a policy, please contact our support team for further instructions."
    elif intent == "excess":
        response = "A policy excess is...."
    elif intent == "coronavirus":
        response = "Your coronavirus cover is included in your travel insurance"
    else:
        response = "I'm sorry, I didn't understand that. Could you clarify your question about travel insurance?"

    return response


class ResponseGenerator:
    def __init__(self, classifier):
        self.classifier = classifier
