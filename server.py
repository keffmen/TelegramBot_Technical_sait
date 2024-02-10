from flask import Flask, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return 'No file part'

    id_application = request.form.get('id')
    org = request.form.get('org')
    Name = request.form.get('Name')
    phoneNumber = request.form.get('phoneNumber')
    problem = request.form.get('problem')
    file = request.files['image']

    if file.filename == '':
        return 'No selected file'

    # Обработка загруженного файла, например, сохранение на сервере
    file.save(f'database/{id_application}' + file.filename)

    return 'File uploaded successfully'


if __name__ == '__main__':
    app.run(debug=True,
            port=5500)
