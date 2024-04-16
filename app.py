from flask import Flask, render_template, request, session, redirect
import sqlite3

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/login')
def login():
    return render_template('login.html')


@app.route('/login', methods=['post'])
def direcao():
    direcao = request.form['sala']
    senha = request.form['senha']

    if direcao == "dono" and senha == "fhellype":
        return render_template('administrador.html')
    
    elif direcao == "1aadm" and senha == "1aadm":
        return render_template('desafios.html')
    
    elif direcao == "1badm" and senha == "1badm":
        return render_template('desafios.html')
    
    elif direcao == "1ads" and senha == "1ads":
        return render_template('desafios.html')
    
    elif direcao == "1bds" and senha == "1bds":
        return render_template('desafios.html')
    
    elif direcao == "2aadm" and senha == "2aadm":
        return render_template('desafios.html')
    
    elif direcao == "2badm" and senha == "2badm":
        return render_template('desafios.html')
    
    elif direcao == "2ads" and senha == "2ads":
        return render_template('desafios.html')
    
    elif direcao == "2bds" and senha == "2bds":
        return render_template('desafios.html')
    
    elif direcao == "3aadm" and senha == "3aadm":
        return render_template('desafios.html')
    
    elif direcao == "3badm" and senha == "3badm":
        return render_template('desafios.html')
    
    elif direcao == "3ads" and senha == "3ads":
        return render_template('desafios.html')
    
    elif direcao == "3bds" and senha == "3bds":
        return render_template('desafios.html')
    
    else:
        return redirect('/login')
    
@app.route('/processamento', methods=['post'])
def processamento():
    conexao = sqlite3.connect('banco.db')
    cursor = conexao.cursor()

    cod = request.form['sala']
    evento01 = request.form['evento_01']
    evento02 = request.form['evento_02']
    evento03 = request.form['evento_03']
    evento04 = request.form['evento_04']
    evento05 = request.form['evento_05']
    evento06 = request.form['evento_06']

    if cod == "1aadm":
        cod = 1
        comando = 'update pontuacao set mp =?, ld =?, tn =?, qua =?, x1 =?, fn =? where cod =?'
        cursor.execute(comando,[evento01, evento02, evento03, evento04, evento05, evento06, cod])
        conexao.commit()
        return render_template('administrador.html')
    
    elif cod == "1badm":
        cod = 2
        comando = 'update pontuacao set mp =?, ld =?, tn =?, qua =?, x1 =?, fn =? where cod =?'
        cursor.execute(comando,[evento01, evento02, evento03, evento04, evento05, evento06, cod])
        conexao.commit()
        return render_template('administrador.html')
    
    elif cod == "1ads":
        cod = 3
        comando = 'update pontuacao set mp =?, ld =?, tn =?, qua =?, x1 =?, fn =? where cod =?'
        cursor.execute(comando,[evento01, evento02, evento03, evento04, evento05, evento06, cod])
        conexao.commit()
        return render_template('administrador.html')
    
    elif cod == "1bds":
        cod = 4
        comando = 'update pontuacao set mp =?, ld =?, tn =?, qua =?, x1 =?, fn =? where cod =?'
        cursor.execute(comando,[evento01, evento02, evento03, evento04, evento05, evento06, cod])
        conexao.commit()
        return render_template('administrador.html')
    
    elif cod == "2aadm":
        cod = 5
        comando = 'update pontuacao set mp =?, ld =?, tn =?, qua =?, x1 =?, fn =? where cod =?'
        cursor.execute(comando,[evento01, evento02, evento03, evento04, evento05, evento06, cod])
        conexao.commit()
        return render_template('administrador.html')
    
    elif cod == "2badm":
        cod = 6
        comando = 'update pontuacao set mp =?, ld =?, tn =?, qua =?, x1 =?, fn =? where cod =?'
        cursor.execute(comando,[evento01, evento02, evento03, evento04, evento05, evento06, cod])
        conexao.commit()
        return render_template('administrador.html')
    
    elif cod == "2ads":
        cod = 7
        comando = 'update pontuacao set mp =?, ld =?, tn =?, qua =?, x1 =?, fn =? where cod =?'
        cursor.execute(comando,[evento01, evento02, evento03, evento04, evento05, evento06, cod])
        conexao.commit()
        return render_template('administrador.html')
    
    elif cod == "2bds":
        cod = 8
        comando = 'update pontuacao set mp =?, ld =?, tn =?, qua =?, x1 =?, fn =? where cod =?'
        cursor.execute(comando,[evento01, evento02, evento03, evento04, evento05, evento06, cod])
        conexao.commit()
        return render_template('administrador.html')
    
    elif cod == "3aadm":
        cod = 9
        comando = 'update pontuacao set mp =?, ld =?, tn =?, qua =?, x1 =?, fn =? where cod =?'
        cursor.execute(comando,[evento01, evento02, evento03, evento04, evento05, evento06, cod])
        conexao.commit()
        return render_template('administrador.html')
    
    elif cod == "3badm":
        cod = 10
        comando = 'update pontuacao set mp =?, ld =?, tn =?, qua =?, x1 =?, fn =? where cod =?'
        cursor.execute(comando,[evento01, evento02, evento03, evento04, evento05, evento06, cod])
        conexao.commit()
        return render_template('administrador.html')
    
    elif cod == "3ads":
        cod = 11
        comando = 'update pontuacao set mp =?, ld =?, tn =?, qua =?, x1 =?, fn =? where cod =?'
        cursor.execute(comando,[evento01, evento02, evento03, evento04, evento05, evento06, cod])
        conexao.commit()
        return render_template('administrador.html')
    
    elif cod == "3bds":
        cod = 12
        comando = 'update pontuacao set mp =?, ld =?, tn =?, qua =?, x1 =?, fn =? where cod =?'
        cursor.execute(comando,[evento01, evento02, evento03, evento04, evento05, evento06, cod])
        conexao.commit()
        return render_template('administrador.html')


    
        
app.run(debug=False)