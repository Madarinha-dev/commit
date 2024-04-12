from flask import Flask, request, render_template, jsonify, redirect
app = Flask(__name__)

@app.route('/acesso', methods=['POST'])
def acessoaluno():
    sala = request.form.get('sala')
    senha = request.form.get('senha')

    print(f'A sala:',{sala})
    print(f'A senha:', {senha})

    return redirect('/desafios')

