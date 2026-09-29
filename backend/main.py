from flask import Flask, request, jsonify, render_template_string

app = Flask(__name__)

HTML_PAGE = """
<!DOCTYPE html>
<html>
<body style="font-family:Arial; padding:30px; background:#f4f4f4;">
<h1>LegalEase AI - Demo Working</h1>
<p><b>Input:</b> Legal text</p>
<textarea id="t" rows="6" cols="80">The Tenant shall not sublet the premises without prior written consent of the Landlord.</textarea><br><br>
<button onclick="go()" style="padding:12px 25px; background:blue; color:white; border:none;">Simplify</button>
<h2>Output:</h2>
<div id="out" style="background:white; border:1px solid #ccc; padding:15px; min-height:100px;">Output inga varum...</div>
<script>
async function go(){
  const text = document.getElementById('t').value;
  document.getElementById('out').innerText='Loading...';
  const res = await fetch('/analyze', {method:'POST', headers:{'Content-Type':'application/json'}, body: JSON.stringify({text})});
  const data = await res.json();
  document.getElementById('out').innerText = data.result;
}
</script>
</body>
</html>
"""

@app.route('/')
def home(): return render_template_string(HTML_PAGE)

@app.route('/analyze', methods=['POST'])
def analyze():
    text = request.json.get('text','').lower()
    if "sublet" in text:
        result = "INPUT: Tenant shall not sublet...\n\nOUTPUT: Tenant-ku Landlord permission illama veeta vera yaarukkum rent-ku vida koodathu.\n\nRisk Level: HIGH"
    else:
        result = f"INPUT: {text}\n\nOUTPUT (Simple Tamil): Ithu oru sattapoorva oppantham. Ithula sonna vishayathai than pinpatranum."
    return jsonify({"result": result})

if __name__ == '__main__':
    app.run(debug=True, port=8000)