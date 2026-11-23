from flask import Flask, render_template, request

app = Flask(__name__)

# Route utama mendukung GET (menampilkan halaman) dan POST (menerima data form)
