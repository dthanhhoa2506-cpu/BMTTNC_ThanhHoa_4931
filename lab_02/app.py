from flask import Flask, render_template, request

from caesar.caesar_cipher import CaesarCipher

from vigenere import VigenereCipher
from .playfair_cipher import PlayFairCipher
from railfence import RailFenceCipher
from transposition import TranspositionCipher

app = Flask(__name__)

# ================= HOME =================
@app.route("/")
def home():
    return render_template("index.html")


# ================= CAESAR =================
@app.route("/caesar")
def caesar():
    return render_template("caesar.html")


@app.route("/caesar/encrypt", methods=["POST"])
def caesar_encrypt():
    text = request.form["inputPlainText"]
    key = int(request.form["inputKeyPlain"])

    cipher = CaesarCipher()
    result = cipher.encrypt_text(text, key)

    return f"Plain Text: {text}<br>Key: {key}<br>Encrypted: {result}"


@app.route("/caesar/decrypt", methods=["POST"])
def caesar_decrypt():
    text = request.form["inputCipherText"]
    key = int(request.form["inputKeyCipher"])

    cipher = CaesarCipher()
    result = cipher.decrypt_text(text, key)

    return f"Cipher Text: {text}<br>Key: {key}<br>Decrypted: {result}"


# ================= VIGENERE =================
@app.route("/vigenere")
def vigenere():
    return render_template("vigenere.html")


@app.route("/vigenere/encrypt", methods=["POST"])
def vigenere_encrypt():
    text = request.form["inputPlainText"]
    key = request.form["inputKey"]

    cipher = VigenereCipher()
    result = cipher.encrypt(text, key)

    return f"Plain Text: {text}<br>Key: {key}<br>Encrypted: {result}"


@app.route("/vigenere/decrypt", methods=["POST"])
def vigenere_decrypt():
    text = request.form["inputCipherText"]
    key = request.form["inputKey"]

    cipher = VigenereCipher()
    result = cipher.decrypt(text, key)

    return f"Cipher Text: {text}<br>Key: {key}<br>Decrypted: {result}"


# ================= RAIL FENCE =================
@app.route("/railfence")
def railfence():
    return render_template("railfence.html")


@app.route("/railfence/encrypt", methods=["POST"])
def railfence_encrypt():
    text = request.form["inputPlainText"]
    key = int(request.form["inputKey"])

    cipher = RailFenceCipher()
    result = cipher.encrypt(text, key)

    return f"Plain Text: {text}<br>Key: {key}<br>Encrypted: {result}"


@app.route("/railfence/decrypt", methods=["POST"])
def railfence_decrypt():
    text = request.form["inputCipherText"]
    key = int(request.form["inputKey"])

    cipher = RailFenceCipher()
    result = cipher.decrypt(text, key)

    return f"Cipher Text: {text}<br>Key: {key}<br>Decrypted: {result}"


# ================= PLAYFAIR =================
@app.route("/playfair")
def playfair():
    return render_template("playfair.html")


@app.route("/playfair/encrypt", methods=["POST"])
def playfair_encrypt():
    text = request.form["inputPlainText"]
    key = request.form["inputKey"]

    cipher = PlayFairCipher()
    result = cipher.encrypt(text, key)

    return f"Plain Text: {text}<br>Key: {key}<br>Encrypted: {result}"


@app.route("/playfair/decrypt", methods=["POST"])
def playfair_decrypt():
    text = request.form["inputCipherText"]
    key = request.form["inputKey"]

    cipher = PlayFairCipher()
    result = cipher.decrypt(text, key)

    return f"Cipher Text: {text}<br>Key: {key}<br>Decrypted: {result}"


# ================= TRANSPOSITION =================
@app.route("/transposition")
def transposition():
    return render_template("transposition.html")


@app.route("/transposition/encrypt", methods=["POST"])
def transposition_encrypt():
    text = request.form["inputPlainText"]
    key = int(request.form["inputKey"])

    cipher = TranspositionCipher()
    result = cipher.encrypt(text, key)

    return f"Plain Text: {text}<br>Key: {key}<br>Encrypted: {result}"


@app.route("/transposition/decrypt", methods=["POST"])
def transposition_decrypt():
    text = request.form["inputCipherText"]
    key = int(request.form["inputKey"])

    cipher = TranspositionCipher()
    result = cipher.decrypt(text, key)

    return f"Cipher Text: {text}<br>Key: {key}<br>Decrypted: {result}"


# ================= RUN =================
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5050, debug=True)