
from flask import Flask, render_template, request, flash, redirect, url_for
from pathlib import Path
from datetime import datetime
import json

app = Flask(__name__)
app.secret_key = "kunci-rahasia-cortez"

FILE_PESAN = Path(__file__).parent / "pesan.json"


def baca_pesan():
    if not FILE_PESAN.exists():
        return []

    try:
        return json.loads(FILE_PESAN.read_text(encoding="utf-8"))
    except (json.JSONDecodeError, OSError):
        return []


@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        nama = request.form.get("name", "").strip()
        isi = request.form.get("message", "").strip()

        if not nama or not isi:
            flash("Nama dan pesan wajib diisi.", "error")
        else:
            pesan = baca_pesan()
            pesan.append({
                "nama": nama,
                "isi": isi,
                "waktu": datetime.now().strftime("%d-%m-%Y %H:%M:%S")
            })

            FILE_PESAN.write_text(
                json.dumps(pesan, ensure_ascii=False, indent=2),
                encoding="utf-8"
            )

            flash("Pesan berhasil disimpan!", "success")
            return redirect(url_for("home"))

    return render_template("index.html")


@app.route("/pesan")
def lihat_pesan():
    pesan = baca_pesan()
    return render_template("pesan.html", pesan=pesan)


@app.route("/profil")
def profil():
    return render_template("profil.html")


if __name__ == "__main__":
    app.run(debug=True)
