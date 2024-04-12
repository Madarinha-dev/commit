from flask import Flask, request, render_template, jsonify, redirect
app = Flask(__name__)


@app.route('/dados.py', methods=['POST'])
def processar_formulario():
    sala = request.form['sala']
    senha = request.form['senha']
    if sala == 'adm':
        if senha == 3:
            return render_template('index.html')
        # eu quero levar pra tela index so pra teste
        else:
            print('senha errada (teste)')
    else:
        print('deu errado (teste)')

if __name__ == '__main__':
    app.run(debug=True)

