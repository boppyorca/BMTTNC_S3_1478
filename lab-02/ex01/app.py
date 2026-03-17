import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'ex01'))

from flask import Flask, render_template, request, json
from cipher.caesar import CaesarCipher
from cipher.playfair.playfair_cipher import PlayFairCipher
from cipher.railfence.railfence_cipher import RailFenceCipher

app = Flask(__name__)

#router routes for home page
@app.route("/")
def home():
 return render_template('index.html')

#router routes for caesar cypher
@app.route("/caesar")
def caesar():
 return render_template('caesar.html')

@app.route("/encrypt", methods=['POST'])
def caesar_encrypt():
 text = request.form['inputPlainText']
 key = int(request.form['inputKeyPlain'])
 caesar = CaesarCipher()
 encrypted_text = caesar.encrypt_text(text, key)
 return f"text: {text}<br/>key: {key}<br/>encrypted text: {encrypted_text}"

@app.route("/decrypt", methods=['POST'])
def caesar_decrypt():
 text = request.form['inputCipherText']
 key = int(request.form['inputKeyCipher'])
 caesar = CaesarCipher()
 decrypted_text = caesar.decrypt_text(text, key)
 return f"text: {text}<br/>key: {key}<br/>decrypted text: {decrypted_text}"

#router routes for raile fence
@app.route("/railfence")
def railfence():
 return render_template('railfence.html')
@app.route("/encrypt", methods=['POST'])
def railfence_encrypt():
 text = request.form['inputPlainText']
 key = int(request.form['inputKeyPlain'])
 rf_cipher=RailFenceCipher()
 encrypted_text = rf_cipher.rail_fence(text, key)
 return f"text: {text}<br/>key: {key}<br/>encrypted text: {encrypted_text}"

@app.route("/decrypt", methods=['POST'])
def railfence_decrypt():
 text = request.form['inputCipherText']
 key = int(request.form['inputKeyCipher'])
 rf_cipher = RailFenceCipher()
 decrypted_text = rf_cipher.rail_fence_decrypt(text, key)
 return f"text: {text}<br/>key: {key}<br/>decrypted text: {decrypted_text}"

#router routes for playfair
@app.route("/playfair")
def playfair():
 return render_template('playfair.html')
@app.route("/playfair_encrypt", methods=['POST'])
def playfair_encrypt():
    text = request.form['inputPlainText']
    key = request.form['inputKeyPlain']
    pf_cipher = PlayFairCipher()
    matrix = pf_cipher.create_playfair_matrix(key)
    encrypted_text = pf_cipher.playfair_encrypt(text, matrix)
    return f"text: {text}<br/>key: {key}<br/>encrypted text: {encrypted_text}"


@app.route("/playfair_decrypt", methods=['POST'])
def playfair_decrypt():
    text = request.form['inputCipherText']
    key = request.form['inputKeyCipher']
    pf_cipher = PlayFairCipher()
    matrix = pf_cipher.create_playfair_matrix(key)
    decrypted_text = pf_cipher.playfair_decrypt(text, matrix)
    return f"text: {text}<br/>key: {key}<br/>decrypted text: {decrypted_text}"

#main function
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5050, debug=True)