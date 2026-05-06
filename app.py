from flask import Flask, send_file, abort, request, render_template
from ebooklib import epub
import os


app = Flask(__name__)

BOOK_DIR = "books"

def _get_book_list():
    files = sorted(os.listdir(BOOK_DIR))
    books = {}
    for i, fname in enumerate(files, start=1):
        books[i] = fname
    return books

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/download/<int:book_id>")
def download_book(book_id):
    print(book_id)
    books = _get_book_list()
    filename = books.get(book_id, None)
    if not filename:
        abort(404, description="Book not found")
    file_path = os.path.join(BOOK_DIR, filename)
    if not os.path.isfile(file_path):
        abort(404, description="Book file missing")
    return send_file(
        file_path,
        as_attachment=True,
        download_name=filename,
        mimetype="application/epub+zip"
    )

@app.route("/upload", methods=["POST"])
def upload_book():
    if 'file' not in request.files:
        abort(400, description="No file part in the request")
    file = request.files['file']
    if file.filename == '':
        abort(400, description="No selected file")
    
    filename = file.filename
    save_path = os.path.join(BOOK_DIR, filename)
    file.save(save_path)

    books = _get_book_list()
    book_id = list(books.keys())[-1]

    return {"message": "Book uploaded successfully", "filename": filename}, 201
    
@app.route("/books")
def get_books():
    return {"available_books": _get_book_list()}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)