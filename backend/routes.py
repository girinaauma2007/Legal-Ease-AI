from flask import Blueprint, request, jsonify

# Blueprint create pannrom
legal_bp = Blueprint('legal', __name__)

def get_simple_output(text):
    text = text.lower()
    
    if "sublet" in text:
        return "Tenant-ku Landlord permission illama veeta vera yaarukkum rent-ku vida koodathu. Risk: HIGH - Ungalukku prachanai varalam"
    elif "security" in text and "non-refundable" in text:
        return "Rs.50,000 security deposit kattanum, athu thirumba kedaikathu. Risk: HIGH - Paisa loss"
    elif "terminate" in text or "notice" in text:
        return "30 naal munnadi notice kuduthu agreement-a yaarum mudikalam. Risk: LOW"
    elif "indemnify" in text:
        return "Oru side ku loss vantha, inoru side antha loss-a katta venum. Risk: MEDIUM"
    elif "rent" in text and "5th" in text:
        return "Prathi maasam 5th date kulla rent kattanum, late na fine. Risk: MEDIUM"
    else:
        return f"Input Text: {text[:100]}... \n\nSimple Meaning: Ithu oru sattapoorva nigazhvuga patriya oppantham. Neenga ithai pinpatra vendum. Risk: LOW"

@legal_bp.route('/analyze', methods=['POST'])
def analyze():
    data = request.get_json()
    user_text = data.get('text', '')
    
    if not user_text:
        return jsonify({"result": "Input kudunga bro!"})
    
    # Input -> Output Logic
    simplified = get_simple_output(user_text)
    
    final_result = f"INPUT: {user_text}\n\nOUTPUT (Tamil Simple):\n{simplified}"
    
    return jsonify({"result": final_result})

@legal_bp.route('/health', methods=['GET'])
def health():
    return jsonify({"status": "LegalEaseAI Backend Working", "input_output": "Ready"})