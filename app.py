from flask import Flask, render_template, request, session, redirect
import sqlite3

app = Flask(__name__)
app.secret_key="123"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/rank')
def rank():
    return render_template('rank.html')


@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/adm')
def adm():
    return render_template('administrador.html')

@app.route('/ranke')
def ranke():
    conexao = sqlite3.connect('banco.db')
    cursor = conexao.cursor()

    # sql = """
    # SELECT sala, total FROM pontuacao ORDER BY total ;
    # """

    sql = """
    SELECT * FROM pontuacao ORDER BY total DESC;
    """
    cursor.execute(sql)

    resultado = cursor.fetchall()
    conexao.commit()
    conexao.close()
    pagina = '''
    <!DOCTYPE html>
    <html lang="en">
    <head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Rank</title>
    <style>
        * {
            padding: 0px;
            margin: 0px;
        }

        body {
            background-image: url(/static/img/imagens/fundo\ 05.jpeg);
            padding: 10px;
            display: flex;
            justify-content: center;
            color: white;
            margin-top: 100px;

        }

        h1 {
            color: white;
            font-family: Georgia, 'Times New Roman', Times, serif;
            text-align: center;
            /* background-color: aqua; */
            position: absolute;
            margin-top: -90px;
            padding-bottom: 100px;

        }

        div.casa {
            background-color: rgba(255, 0, 0, 0.317);
            margin-top:60px;
            width: 80dvw;
            max-width: 400px;
            height: 200px;
            /* altura a definir dependendo da situação */

            display: flex;
            justify-content: center;
        }

        div.tabela {
            background-color: aqua;
        }

        .botao {
        transition: 0.6s;
        }

        .botao:hover {
        background-color: rgb(255, 86, 86);
        color: white;
        transition: 0.6s;
        /* padding: 2px; */
        padding-top:5px ;
        padding-bottom: 5px;
        margin: 5px;
        }


    </style>
    </head>
    <body>
    <h1>Rank </h1>

    <a href="adm" class=""><button style="
        width: 70px;
        max-width: 350px;
        border-radius: 10px;
        height: 25px;
        position: absolute;
        top: 20px;
        left: 10px;" type="" class="botao">Voltar</button></a>


    <!-- <div class="casa"> -->
        <!-- <div class="tabela"> -->
            <!-- a tabela [ rank ]  exibir em ordem crescente, pode ser a tabela completa-->
        <!-- </div> -->
    <!-- </div> -->


    </body>
    </html>
    '''
    for r in resultado:
        pagina = pagina + f'SALA:__________ {r[1]} <br> PONTOS:__________{r[10]} <br> <br>'
    return pagina

@app.route("/troca_de_senha", methods=['post'])
def trocar():
    #  sala_senha e nova_senha
    if "adm" in session:
        sala = request.form["sala_senha"]
        senha = request.form["nova_senha"]

        conexao = sqlite3.connect("banco.db")
        cursor = conexao.cursor()

        comando = 'update senhaa set senha=? where sala=?'
        cursor.execute(comando,[senha, sala])
        conexao.commit()
        conexao.close()
        return render_template('administrador.html')
        



@app.route('/login', methods=['post'])
def direcao():
    direcao = request.form['sala']
    senha = request.form['senha']

    dono = "fhe"
    zaadm = "1aadm"
    zbadm = "1badm"
    zads = "1ads"
    zbds = "1bds"
    xaadm = "2aadm"
    xbadm = "2badm"
    xads = "2ads"
    xbds = "2bds"
    caadm = "3aadm"
    cbadm = "3badm"
    cads = "3ads"
    cbds = "3bds"

    conexao = sqlite3.connect('banco.db')
    cursor = conexao.cursor()

    comando = "SELECT * FROM senhaa WHERE sala=? and senha=?"
    cursor.execute(comando,[direcao,senha])
    lista = cursor.fetchall()
    conexao.commit()
    lista = str(lista)
    lista=lista.replace("[","").replace("]","").replace("(","").replace(")","")
    lista = list(lista)
    print(lista)

    if direcao=="administrador":
        cursor.execute(comando,[direcao,senha])
        lista = cursor.fetchall()
        if len(lista)>0:
            session["adm"]=direcao
            return render_template("administrador.html")
        else:
            return redirect("/login")
        

    elif direcao != "admnistrador":
        cursor.execute(comando,[direcao,senha])
        lista = cursor.fetchall()
        if len(lista)>0:
            session["aluno"]=direcao
            return render_template("desafios.html")
        else:
            return redirect("/login")
    else:
        return redirect('/login') 
    # if direcao == "ad" and senha == dono:
    # if lista[0] == "administrador":
    #     return render_template('administrador.html')
    
    
    # elif direcao == "1aadm" and senha == zaadm:
    #     return render_template('desafios.html')
    
    
    # elif direcao == "1badm" and senha == zbadm:
    #     return render_template('desafios.html')
    
    
    # elif direcao == "1ads" and senha == zads:
    #     return render_template('desafios.html')
    
    
    # elif direcao == "1bds" and senha == zbds:
    #     return render_template('desafios.html')
    
    
    # elif direcao == "2aadm" and senha == xaadm:
    #     return render_template('desafios.html')
    
    
    # elif direcao == "2badm" and senha == xbadm:
    #     return render_template('desafios.html')
    
    
    # elif direcao == "2ads" and senha == xads:
    #     return render_template('desafios.html')
    
    
    # elif direcao == "2bds" and senha == xbds:
    #     return render_template('desafios.html')
    
    
    # elif direcao == "3aadm" and senha == caadm:
    #     return render_template('desafios.html')
    
    
    # elif direcao == "3badm" and senha == cbadm:
    #     return render_template('desafios.html')
    
    
    # elif direcao == "3ads" and senha == cads:
    #     return render_template('desafios.html')
    
    
    # elif direcao == "3bds" and senha == cbds:
    #     return render_template('desafios.html')
    
    
  
    
    
@app.route('/processamento', methods=['post'])
def processamento():
    conexao = sqlite3.connect('banco.db')
    cursor = conexao.cursor()

    cod = request.form['sala']
    evento01: int = request.form['evento_01']
    evento02: int = request.form['evento_02']
    evento03: int = request.form['evento_03']
    evento04: int = request.form['evento_04']
    evento05: int = request.form['evento_05']
    evento06: int = request.form['evento_06']
    evento07: int = request.form['evento_07']
    punicoes: int = request.form['punicoes']
    positivo: int = int(request.form['evento_01']) + int(request.form['evento_02']) + int(request.form['evento_03']) + int(request.form['evento_04']) + int(request.form['evento_05']) + int(request.form['evento_06']) + int(request.form['evento_07'])
    negativo: int = int(request.form['punicoes'])
    total: int = int(positivo) - int(negativo)

    if cod == "1aadm":
        cod = 1
        sala = "1°A ADM"
        comando = 'update pontuacao set sala =?, mp =?, ld =?, tn =?, qua =?, x1 =?, fn =?, ex =?, punicoes =?, total =? where cod =?'
        cursor.execute(comando,[sala, evento01, evento02, evento03, evento04, evento05, evento06, evento07, punicoes, total, cod])
        conexao.commit()
        return render_template('administrador.html')
    
    elif cod == "1badm":
        cod = 2
        sala = "1°B ADM"
        comando = 'update pontuacao set sala =?, mp =?, ld =?, tn =?, qua =?, x1 =?, fn =?, ex =?, punicoes =?, total =? where cod =?'
        cursor.execute(comando,[sala, evento01, evento02, evento03, evento04, evento05, evento06, evento07, punicoes, total, cod])
        conexao.commit()
        return render_template('administrador.html')
    
    elif cod == "1ads":
        cod = 3      
        sala = "1°A DS"  
        comando = 'update pontuacao set sala =?, mp =?, ld =?, tn =?, qua =?, x1 =?, fn =?, ex =?, punicoes =?, total =? where cod =?'
        cursor.execute(comando,[sala, evento01, evento02, evento03, evento04, evento05, evento06, evento07, punicoes, total, cod])
        conexao.commit()
        return render_template('administrador.html')
    
    elif cod == "1bds":
        cod = 4
        sala = "1°B DS"
        comando = 'update pontuacao set sala =?, mp =?, ld =?, tn =?, qua =?, x1 =?, fn =?, ex =?, punicoes =?, total =? where cod =?'
        cursor.execute(comando,[sala, evento01, evento02, evento03, evento04, evento05, evento06, evento07, punicoes, total, cod])
        conexao.commit()
        return render_template('administrador.html')
    
    elif cod == "2aadm":
        cod = 5
        sala = "2°A ADM"
        comando = 'update pontuacao set sala =?, mp =?, ld =?, tn =?, qua =?, x1 =?, fn =?, ex =?, punicoes =?, total =? where cod =?'
        cursor.execute(comando,[sala, evento01, evento02, evento03, evento04, evento05, evento06, evento07, punicoes, total, cod])
        conexao.commit()
        return render_template('administrador.html')
    
    elif cod == "2badm":
        cod = 6
        sala = "2°B ADM"
        comando = 'update pontuacao set sala =?, mp =?, ld =?, tn =?, qua =?, x1 =?, fn =?, ex =?, punicoes =?, total =? where cod =?'
        cursor.execute(comando,[sala, evento01, evento02, evento03, evento04, evento05, evento06, evento07, punicoes, total, cod])
        conexao.commit()
        return render_template('administrador.html')
    
    elif cod == "2ads":
        cod = 7
        sala = "2°A DS"
        comando = 'update pontuacao set sala =?, mp =?, ld =?, tn =?, qua =?, x1 =?, fn =?, ex =?, punicoes =?, total =? where cod =?'
        cursor.execute(comando,[sala, evento01, evento02, evento03, evento04, evento05, evento06, evento07, punicoes, total, cod])
        conexao.commit()
        return render_template('administrador.html')
    
    elif cod == "2bds":
        cod = 8
        sala = "2°B DS"
        comando = 'update pontuacao set sala =?, mp =?, ld =?, tn =?, qua =?, x1 =?, fn =?, ex =?, punicoes =?, total =? where cod =?'
        cursor.execute(comando,[sala, evento01, evento02, evento03, evento04, evento05, evento06, evento07, punicoes, total, cod])
        conexao.commit()
        return render_template('administrador.html')
    
    elif cod == "3aadm":
        cod = 9
        sala = "3°A ADM"
        comando = 'update pontuacao set sala =?, mp =?, ld =?, tn =?, qua =?, x1 =?, fn =?, ex =?, punicoes =?, total =? where cod =?'
        cursor.execute(comando,[sala, evento01, evento02, evento03, evento04, evento05, evento06, evento07, punicoes, total, cod])
        conexao.commit()
        return render_template('administrador.html')
    
    elif cod == "3badm":
        cod = 10
        sala = "3°B ADM"
        comando = 'update pontuacao set sala =?, mp =?, ld =?, tn =?, qua =?, x1 =?, fn =?, ex =?, punicoes =?, total =? where cod =?'
        cursor.execute(comando,[sala, evento01, evento02, evento03, evento04, evento05, evento06, evento07, punicoes, total, cod])
        conexao.commit()
        return render_template('administrador.html')
    
    elif cod == "3ads":
        cod = 11
        sala = "3°A DS"
        comando = 'update pontuacao set sala =?, mp =?, ld =?, tn =?, qua =?, x1 =?, fn =?, ex =?, punicoes =?, total =? where cod =?'
        cursor.execute(comando,[sala, evento01, evento02, evento03, evento04, evento05, evento06, evento07, punicoes, total, cod])
        conexao.commit()
        return render_template('administrador.html')
    
    elif cod == "3bds":
        cod = 12
        sala = "3°B DS"
        comando = 'update pontuacao set sala =?, mp =?, ld =?, tn =?, qua =?, x1 =?, fn =?, ex =?, punicoes =?, total =? where cod =?'
        cursor.execute(comando,[sala, evento01, evento02, evento03, evento04, evento05, evento06, evento07, punicoes, total, cod])
        conexao.commit()
        return render_template('administrador.html')


    
        
app.run(debug=False)