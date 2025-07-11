from flask import Flask, request, render_template, jsonify

app = Flask(__name__)
data_store = []

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html', data=data_store)

@app.route('/webhook', methods=['POST'])
def webhook():
    json_data = request.get_json()
    if json_data:
        data_store.append(json_data)
    return jsonify({"status": "received"}), 200

@app.route('/merge-webhook', methods=['POST'])
def merge_webhook():
    json_data = request.get_json()
    if json_data and json_data.get('action') == 'closed' and json_data.get('pull_request', {}).get('merged'):
        data_store.append({'merge': json_data})
    return jsonify({"status": "merge received"}), 200

if __name__ == '__main__':
    app.run(debug=True)