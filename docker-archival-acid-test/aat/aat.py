from flask import Flask, request, send_from_directory

# set the project root directory as the static folder, you can set others.
app = Flask(__name__, static_url_path='/')

@app.route('/~mkelly/acid/<path:path>')
def send_aat_remote(path):
    return send_from_directory('archivalAcidTestRemote',path)

@app.route('/', defaults={'path': 'index.html'})
@app.route('/<path:path>')
def send_aat(path):
    return send_from_directory('archivalAcidTest',path)

if __name__ == "__main__":
        app.run(host='0.0.0.0',debug=True)
