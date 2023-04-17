# Numerologia através do Tarot 

from flask import Flask, render_template, request
import mysql.connector

app = Flask(__name__)

@app.route("/", methods=['GET','POST'])
def numerologia_nome():
    
    if request.method == "GET":
        return render_template("index.html")
    else:
        nome = request.form['nome'].replace(" ", "")
        num_letras = len(nome)
        soma_nome = 0
    
        if num_letras > 22:
            pi_str = str(num_letras)
            for i in pi_str:
                soma_nome += int(i)
        
        else:
            soma_nome = num_letras

        sobrenomes = request.form['sobrenome'].split(" ")
        soma_sobrenomes = request.form['sobrenome'].replace(" ", "")
        num_sobrenomes = len(soma_sobrenomes)
        somatoria_sobrenomes = 0
        
        if num_sobrenomes > 22:
            pi_str = str(num_sobrenomes)
            for i in pi_str:
                somatoria_sobrenomes += int(i)
        
        else:
            somatoria_sobrenomes = num_sobrenomes
                   
    
    conexao = mysql.connector.connect(
        host = 'localhost',
        user = 'root',
        password= 'admin',
        database= 'banco',
    )

    
    cursor = conexao.cursor()
        
    comando = f'SELECT arcano FROM banco.tarot WHERE numero = {soma_nome};'
    cursor.execute(comando)
    resultado = cursor.fetchall() 
    
    comando2 = f'SELECT personalidade FROM banco.tarot WHERE numero = {soma_nome};'
    cursor.execute(comando2)
    resultado2 = cursor.fetchall()

    comando_soma_sobrenome = f'SELECT aptidoes_profissionais FROM banco.tarot WHERE numero = {somatoria_sobrenomes};'
    cursor.execute(comando_soma_sobrenome)
    resultado_sobrenome = cursor.fetchall()

    comando_soma_sobrenome_1 = f'SELECT arcano FROM banco.tarot WHERE numero = {somatoria_sobrenomes};'
    cursor.execute(comando_soma_sobrenome_1)
    resultado_sobrenome_1 = cursor.fetchall()

    comando_soma_sobrenome_2 = f'SELECT karma_material FROM banco.tarot WHERE numero = {somatoria_sobrenomes};'
    cursor.execute(comando_soma_sobrenome_2)
    resultado_sobrenome_2 = cursor.fetchall()

    

    if len(sobrenomes) >= 1:
        sobrenome1 = len(sobrenomes[0])
        comando3 = f'SELECT aptidoes_profissionais FROM banco.tarot WHERE numero = {sobrenome1};'
        cursor.execute(comando3)
        resultado3 = cursor.fetchall()
        comando_3 = f'SELECT arcano FROM banco.tarot WHERE numero = {sobrenome1};'
        cursor.execute(comando_3)
        resultado_3 = cursor.fetchall()
        coluna_aptidoes = resultado3[0][0]
        arcano_sobrenome = resultado_3[0][0]
        imagem_sobrenome = str(sobrenome1)

    if len(sobrenomes) >= 2:
        sobrenome2 = len(sobrenomes[1])
        comando4 = f'SELECT aptidoes_profissionais FROM banco.tarot WHERE numero = {sobrenome2};'
        cursor.execute(comando4)
        resultado4 = cursor.fetchall()
        comando_4 = f'SELECT arcano FROM banco.tarot WHERE numero = {sobrenome2};'
        cursor.execute(comando_4)
        resultado_4 = cursor.fetchall()
        coluna_aptidoes = resultado3[0][0] + " " + resultado4[0][0] + " " + resultado_sobrenome[0][0]
        arcano_sobrenome = resultado_3[0][0] + ", " + resultado_4[0][0] + " e " + resultado_sobrenome_1[0][0]
        imagem_sobrenome = str(sobrenome1) + ", " + str(sobrenome2) + ", " + str(somatoria_sobrenomes)

    if len(sobrenomes) >= 3:
        sobrenome3 = len(sobrenomes[2])
        comando5 = f'SELECT aptidoes_profissionais FROM banco.tarot WHERE numero = {sobrenome3};'
        cursor.execute(comando5)
        resultado5 = cursor.fetchall()
        comando_5 = f'SELECT arcano FROM banco.tarot WHERE numero = {sobrenome3};'
        cursor.execute(comando_5)
        resultado_5 = cursor.fetchall()
        coluna_aptidoes = resultado3[0][0]  + " " + resultado4[0][0] + " " + resultado5[0][0] + " " + resultado_sobrenome[0][0]
        arcano_sobrenome = resultado_3[0][0] + ", " + resultado_4[0][0] + ", " + resultado_5[0][0] + " e "+ resultado_sobrenome_1[0][0]
        imagem_sobrenome = str(sobrenome1) + ", " + str(sobrenome2) + ", " + str(sobrenome3) + ", " + str(somatoria_sobrenomes)

    if len(sobrenomes) >= 4:
        sobrenome4 = len(sobrenomes[3])
        comando6 = f'SELECT aptidoes_profissionais FROM banco.tarot WHERE numero = {sobrenome4};'
        cursor.execute(comando6)
        resultado6 = cursor.fetchall()
        comando_6 = f'SELECT arcano FROM banco.tarot WHERE numero = {sobrenome4};'
        cursor.execute(comando_6)
        resultado_6 = cursor.fetchall()
        coluna_aptidoes = resultado3[0][0] + " " + resultado4[0][0] + " " + resultado5[0][0] + " " + resultado6[0][0] + " " + resultado_sobrenome[0][0]
        arcano_sobrenome = resultado_3[0][0] + ", " + resultado_4[0][0] + ", " + resultado_5[0][0] + ", " + resultado_6[0][0] + " e "+ resultado_sobrenome_1[0][0]
        imagem_sobrenome = str(sobrenome1) + ", " + str(sobrenome2) + ", " + str(sobrenome3) + ", " + str(sobrenome4) + ", " + str(somatoria_sobrenomes)

    if len(sobrenomes) >= 5:
        sobrenome5 = len(sobrenomes[4])
        comando7 = f'SELECT aptidoes_profissionais FROM banco.tarot WHERE numero = {sobrenome5};'
        cursor.execute(comando7)
        resultado7 = cursor.fetchall()
        comando_7 = f'SELECT arcano FROM banco.tarot WHERE numero = {sobrenome5};'
        cursor.execute(comando_7)
        resultado_7 = cursor.fetchall()
        coluna_aptidoes = resultado3[0][0] + " " + resultado4[0][0] + " " + resultado5[0][0] + " " + resultado6[0][0] + " " + resultado7[0][0] + " " + resultado_sobrenome[0][0]
        arcano_sobrenome = resultado_3[0][0] + ", " + resultado_4[0][0] + ", " + resultado_5[0][0] + ", " + resultado_6[0][0] + ", " + resultado_7[0][0] + " e "+ resultado_sobrenome_1[0][0]
        imagem_sobrenome = str(sobrenome1) + ", " + str(sobrenome2) + ", " + str(sobrenome3) + ", " + str(sobrenome4) + ", " + str(sobrenome5) + ", " + str(somatoria_sobrenomes)

    if len(sobrenomes) >= 6:
        sobrenome6 = len(sobrenomes[5])
        comando8 = f'SELECT aptidoes_profissionais FROM banco.tarot WHERE numero = {sobrenome6};'
        cursor.execute(comando8)
        resultado8 = cursor.fetchall()
        comando_8 = f'SELECT arcano FROM banco.tarot WHERE numero = {sobrenome6};'
        cursor.execute(comando_8)
        resultado_8 = cursor.fetchall()
        coluna_aptidoes = resultado3[0][0] + " " + resultado4[0][0] + " " + resultado5[0][0] + " " + resultado6[0][0] + " " + resultado7[0][0] + " " + resultado8[0][0] + " " + resultado_sobrenome[0][0]
        arcano_sobrenome = resultado_3[0][0] + ", " + resultado_4[0][0] + ", " + resultado_5[0][0] + ", " + resultado_6[0][0] + ", " + resultado_7[0][0] + ", " + resultado_8[0][0] + " e "+ resultado_sobrenome_1[0][0]
        imagem_sobrenome = str(sobrenome1) + ", " + str(sobrenome2) + ", " + str(sobrenome3) + ", " + str(sobrenome4) + ", " + str(sobrenome5) + ", " + str(sobrenome6) + ", " + str(somatoria_sobrenomes)

    if len(sobrenomes) >= 7:
        sobrenome7 = len(sobrenomes[6])
        comando9 = f'SELECT aptidoes_profissionais FROM banco.tarot WHERE numero = {sobrenome7};'
        cursor.execute(comando9)
        resultado9 = cursor.fetchall()
        comando_9 = f'SELECT arcano FROM banco.tarot WHERE numero = {sobrenome7};'
        cursor.execute(comando_9)
        resultado_9 = cursor.fetchall()
        coluna_aptidoes = resultado3[0][0] + " " + resultado4[0][0] + " " + resultado5[0][0] + " " + resultado6[0][0] + " " + resultado7[0][0] + " " + resultado8[0][0] + " " + resultado9[0][0] + " " + resultado_sobrenome[0][0]
        arcano_sobrenome = resultado_3[0][0] + ", " + resultado_4[0][0] + ", " + resultado_5[0][0] + ", " + resultado_6[0][0] + ", " + resultado_7[0][0] + ", " + resultado_8[0][0] + ", " + resultado_9[0][0] + " e "+ resultado_sobrenome_1[0][0]
        imagem_sobrenome = str(sobrenome1) + ", " + str(sobrenome2) + ", " + str(sobrenome3) + ", " + str(sobrenome4) + ", " + str(sobrenome5) + ", " + str(sobrenome6) + ", " + str(sobrenome7) + ", " + str(somatoria_sobrenomes)

    return render_template(
        "resultado.html",
        arcano = soma_nome,
        coluna_arcano = resultado[0][0],
        coluna_personalidade = resultado2[0][0],
        coluna_aptidoes_profissionais = coluna_aptidoes,
        desc_arcano_sobrenome = arcano_sobrenome,
        img_arcano = imagem_sobrenome,
        karma_material = resultado_sobrenome_2[0][0],
        img_karma = str(somatoria_sobrenomes),
        arcano_karma = resultado_sobrenome_1[0][0]
        )

