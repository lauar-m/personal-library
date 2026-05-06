from flask import Flask, send_file, abort, request, render_template, send_from_directory
from ebooklib import epub, ITEM_IMAGE
from PIL import Image
import io
import os

app = Flask(__name__)

BOOK_DIR = "books"
COVER_DIR = "covers"

os.makedirs(BOOK_DIR, exist_ok=True)
os.makedirs(COVER_DIR, exist_ok=True)

def extract_cover(epub_path, cover_name):
    try:
        book = epub.read_epub(epub_path)
        images = [item for item in book.get_items() if item.get_type() == ITEM_IMAGE]
        if images:
            cover_data = images[0].get_content()
            img = Image.open(io.BytesIO(cover_data))
            img.thumbnail((150, 230))
            img.save(os.path.join(COVER_DIR, cover_name + ".jpg"), "JPEG")
            return True
    except:
        pass
    return False

def _get_book_list():
    files = sorted([f for f in os.listdir(BOOK_DIR) if f != ".gitkeep"])
    return {i: fname for i, fname in enumerate(files, start=1)}

@app.route("/")
def home():
    return render_template("index.html")

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

    extract_cover(save_path, filename)

    return {"message": "Success"}, 201

@app.route("/books")
def get_books():
    return {"available_books": _get_book_list()}

@app.route("/cover/<int:book_id>")
def get_cover(book_id):
    books = _get_book_list()
    filename = books.get(book_id)
    cover_path = os.path.join(COVER_DIR, filename + ".jpg")
    
    if os.path.exists(cover_path):
        return send_file(cover_path, mimetype='image/jpeg')
    else:
        abort(404)

@app.route("/download/<int:book_id>")
def download_book(book_id):
    books = _get_book_list()
    filename = books.get(book_id)
    if not filename:
        abort(404, description="Book not found")
    return send_from_directory(BOOK_DIR, filename, as_attachment=True)

@app.route("/edit/<int:book_id>", methods=["POST"])
def edit_book(book_id):
    new_name = request.json.get("new_name")
    if not new_name:
        abort(400, description="Invalid name")
    
    if not new_name.lower().endswith(('.epub', '.pdf')):
        books_list = _get_book_list()
        old_filename = books_list.get(book_id)
        ext = os.path.splitext(old_filename)[1]
        new_name += ext

    books = _get_book_list()
    old_filename = books.get(book_id)
    
    if not old_filename:
        abort(404, description="Book not found")

    old_path = os.path.join(BOOK_DIR, old_filename)
    new_path = os.path.join(BOOK_DIR, new_name)
    old_cover = os.path.join(COVER_DIR, old_filename + ".jpg")
    new_cover = os.path.join(COVER_DIR, new_name + ".jpg")

    try:
        os.rename(old_path, new_path)
        if os.path.exists(old_cover):
            os.rename(old_cover, new_cover)
        return {"message": "Renamed successfully"}, 200
    except Exception as e:
        return {"error": str(e)}, 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)