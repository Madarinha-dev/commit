from flask import Flask, request, render_template, jsonify, redirect
app = Flask(__name__)

# print('testeee')
# print('testeee')
# print('testeee')
# print('testeee')

@app.route('/formulario', methods=['POST'])
def formulario():
    nome = request.form.get('nome')
    print(nome)
    print('testeee')
    print('testeee')
    print('testeee')
    print('testeee')


if __name__ == '__main__':
    app.run(debug=True)