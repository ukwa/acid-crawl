import os
from flask import Flask, request, send_from_directory, render_template

# set the project root directory as the static folder, you can set others.
app = Flask(__name__, static_url_path='')


@app.route('/')
def root():
    return render_template('homepage.html')

@app.route('/simple/', defaults={'req_path': ''})
@app.route('/simple/<path:req_path>')
def dir_listing(req_path):
    BASE_DIR = 'static/simple'

    # Joining the base and the requested path
    abs_path = os.path.join(BASE_DIR, req_path)

    # Return 404 if path doesn't exist
    if not os.path.exists(abs_path):
        return abort(404)

    # Check if path is a file and serve
    if os.path.isfile(abs_path):
        return send_file(abs_path)

    # Show directory contents
    files = os.listdir(abs_path)
    return render_template('files.html', files=files)

@app.route('/archivalAcidTest/<path:path>')
def send_js(path):
    return send_from_directory('static/archivalAcidTest', path)

if __name__ == "__main__":
        app.run(host='0.0.0.0',debug=True)
