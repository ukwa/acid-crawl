from flask import Flask, request, send_from_directory

# Set up a simple Flask app
app = Flask(__name__)

@app.route('/~mkelly/acid/<path:path>')
def send_aat_remote(path):
    return send_from_directory('archivalAcidTestRemote',path)

@app.route('/')
def send_aat_index():
    return send_from_directory('archivalAcidTest', 'index.html')

@app.route('/<path:path>')
def send_aat(path):
    return send_from_directory('archivalAcidTest',path)

if __name__ == "__main__":
        app.run(host='0.0.0.0',port=80,debug=True)
