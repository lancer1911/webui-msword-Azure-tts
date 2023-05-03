"""
Convert MS Word documents to mp3 by Azure TTS API.
written by lancer1911
May 2, 2023
"""

import os
from flask import Flask, request, render_template, send_from_directory, redirect, url_for
import msword_azure_tts
import shutil

app = Flask(__name__)
uploads_dir = './uploads'

def clear_uploads_directory():
    if os.path.exists(uploads_dir):
        shutil.rmtree(uploads_dir)
        os.makedirs(uploads_dir)

clear_uploads_directory()

@app.route('/', methods=['GET', 'POST'])
def convert():
    if request.method == 'POST':
        subscription_key = request.form['subscription_key']
        region = request.form['region']
        language = request.form['language']
        voice = request.form['voice']
        docx_file = request.files['file']

        if not os.path.exists(uploads_dir):
            os.makedirs(uploads_dir)

        docx_file_path = os.path.join(uploads_dir, docx_file.filename)
        docx_file.save(docx_file_path)

        mp3_file_path = msword_azure_tts.docx_to_mp3(docx_file_path, subscription_key, region, language, voice)
        return redirect(url_for('preview', filename=os.path.basename(mp3_file_path)))

    return render_template('index.html')

@app.route('/preview/<filename>')
def preview(filename):
    return render_template('preview.html', filename=filename)

@app.route('/download/<filename>')
def download(filename):
    return send_from_directory(uploads_dir, filename, as_attachment=True)

@app.route('/delete/<filename>')
def delete(filename):
    mp3_file_path = os.path.join(uploads_dir, filename)
    if os.path.exists(mp3_file_path):
        os.remove(mp3_file_path)
    
    docx_file_path = os.path.join(uploads_dir, os.path.splitext(filename)[0] + '.docx')
    if os.path.exists(docx_file_path):
        os.remove(docx_file_path)

    return redirect(url_for('convert'))

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5321)
