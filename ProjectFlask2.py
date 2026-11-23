from flask import Flask, render_template, request

app = Flask(__name__)

# Route utama mendukung GET (menampilkan halaman) dan POST (menerima data form)
@app.route('/', methods=['GET', 'POST'])
def index():
    hasil_nama = None
    hasil_pesan = None

    if request.method == 'POST':
        # Parsing parameter dari input form berdasarkan atribut 'name'
        hasil_nama = request.form.get('nama')
        hasil_pesan = request.form.get('pesan')

