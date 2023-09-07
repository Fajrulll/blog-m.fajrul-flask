# import aplikasi falsk untuk diPakai di web kita
from flask import Flask

#mengatur nama aplikasi
app = Flask(__name__)

# mengatur URI (universal resource identifier), dan aoa yang di tampilkan jika URI tersebut diakses
@app.route('/')# ketika alamat http://127.0.0.1:5000/ dispnggil, maka server akan mengeksekusi fungsi hello() 
def hello():# function dengan nama hello
    return 'hello,world!'

# mengatur URI ke http://127.0.0.1:5000/login, dan mengeksekusi fungsi login() jika diakses di alamat URI http://127.0.0.1:5000/login
@app.route("/login")
def login():
    return 'halaman login'