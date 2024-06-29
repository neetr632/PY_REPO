from flask import Flask, request, render_template
import os

app = Flask(__name__)

UPLOADS_DIR = 'received_files'

@app.route('/logs', methods=['GET', 'POST'])
def receive_logs():
    if request.method == 'POST':
        files = request.files
        if len(files) == 0:
            return "No files found in the request with key 'file'", 400
        
        # Process the files here
        for file_name, file_content in files.items():
            # Save the file to disk
            file_path = os.path.join(UPLOADS_DIR, file_name)
            file_content.save(file_path)

        return "Files received successfully", 200
    else:
        # Get the list of files in the UPLOADS_DIR directory
        files = os.listdir(UPLOADS_DIR)
        return render_template('index.html', files=files)

@app.route('/file/<file_name>', methods=['GET'])
def view_file_content(file_name):
    file_path = os.path.join(UPLOADS_DIR, file_name)
    try:
        with open(file_path, 'r') as file:
            content = file.read()
        return render_template('file_content.html', file_name=file_name, content=content)
    except FileNotFoundError:
        return f"File '{file_name}' not found", 404

if __name__ == '__main__':
    # Create the UPLOADS_DIR directory if it doesn't exist
    os.makedirs(UPLOADS_DIR, exist_ok=True)
    app.run(host='0.0.0.0', port=8080)
