from flask import Flask
import random

app = Flask(__name__)

@app.route("/")
def hello_world():
    return '<h1>Hello, World!</h1> <a href="/random_facts">View a random fact!</a> <a href="/coin">Flip a coin!</a>'

@app.route("/random_facts")
def random_f():
    facts_list = [
        "Salah satu cara untuk memerangi ketergantungan teknologi adalah dengan mencari kegiatan yang membawa kesenangan dan meningkatkan suasana hati",
        "Elon Musk mengklaim bahwa jejaring sosial dirancang untuk membuat kita tetap berada di dalam platform, sehingga kita menghabiskan waktu sebanyak mungkin untuk melihat konten",
        "Elon Musk juga menganjurkan regulasi jejaring sosial dan perlindungan data pribadi pengguna. Dia mengklaim bahwa jejaring sosial mengumpulkan sejumlah besar informasi tentang kita, yang kemudian dapat digunakan untuk memanipulasi pikiran dan perilaku kita"
    ]

    return f'<p>{random.choice(facts_list)}</p>'

@app.route("/coin")
def flip_coin():
    result = random.choice(["Kepala", "Ekor"])
    return f'<p>{result}</p>'

app.run(debug=True)
