from flask import *

app = Flask(__name__)
usuarios = [['sarah','12',['batismo', 'coroinhas', 'pascom']], ['nicolly', '7', ['catecumenato', 'liturgia', 'terco']]] #nome, senha, pastoral
batismos = [['levi', '16/08', 'manhã'], ['maria', '24/08', 'noite']]
catecumeno= [['maria','23/09',['boa vista']], ['jose','24/09',['bela vista']]]
encontro=[['29/08','manhã',['salao']], ['30/08','tarde',['igreja']]]
coroinhas=[['alice', '04/09', 'microfone'], ['milena', '11/09', 'missal']] #NOME, DATA E FUNÇÃO
reuniaocor=[['13/09', '14:00', 'matriz']] #DATA, HORÁRIO E LOCAL
subscor=[['milena', '11/09', 'missal']] #SUBSTITUIÇÕES DE COROINHAS, NOME, DATA E FUNÇÃO
pascom=[['rafael', '04/09'], ['ana', '23/09']] #NOME, DATA
reuniaopas=[['17/09', '14:00', 'matriz']] #DATA, HORÁRIO E LOCAL
subspas=[['ana', '23/09']] #SUBSTITUIÇÕES DE COROINHAS, NOME, DATA E FUNÇÃO
liturgianos=[['Helena','02/10','2 leitura'],['Cedilma','03/10','1 leitura']]
reuniaoli=[['matriz','26/10','manhã']]
subsli=[['Diene','02/10', '2 leitura']]

@app.route('/')
def pagina_principal():
    return render_template('paginainicial.html')

@app.route('/escolhapq', methods=['post'])
def escolhenp():
    op = request.form.get('escolha')
    login = request.form.get('login')
    senha = request.form.get('senha')

    logado = False
    for u in usuarios:
        if login == u[0] and senha == u[1] and op in u[2]:
            logado = True

    if logado:

        if op == 'batismo':
            return render_template('batismo.html')
        elif op == 'catecumenato':
            return render_template('catecumenato.html')
        elif op == 'coroinhas':
            return render_template('coroinhas.html')
        elif op == 'liturgia':
            return render_template('liturgia.html')
        elif op == 'pascom':
            return render_template('pascom.html')
        elif op == 'terco':
            return render_template('terco.html')

    else:
     msg = '*erro ao fazer login'
     msgc = 'Parece que você não tem login, se cadastre agora!'
     return render_template('paginainicial.html', erro = msg, msgcadas = msgc)

#LEVAR PARA A PÁGINA DE CADASTRAR USUÁRIO
@app.route('/mostraradicionaru')
def mostrar_add_usuario():
    return render_template('cadastraru.html')

#ADICIONAR USUÁRIO
@app.route('/adicionarusuario', methods=['post'])
def adicionar_usuario():
    global usuarios
    login = request.form.get('login')
    senha = request.form.get('senha')
    pastoral = request.form.get('pastoral')
    usuarios.append([login,senha,pastoral])
    print (usuarios)
    mensagem = 'Usuário adicionado com sucesso!'
    return render_template('paginainicial.html', msgc=mensagem)


@app.route('/verificarlogin', methods=['post'])
def verificar_logado():
    nome_pessoa = request.form.get('login')
    if nome_pessoa.lower() in usuarios:
        return render_template('login.html')
    else:
        return render_template('paginainicial.html')


#IFRAME QUE LEVA PARA A PÁGINA adicionarbatizado.html
@app.route('/mostraradicionarb')
def mostrar_add_batizado():
    return render_template('adicionarbatizado.html')


#ADICIONAR BATIZADO
@app.route('/adicionarbatizado', methods=['post'])
def adicionar_batizado():
    global batismos
    nomeb = request.form.get('nome')
    datab = request.form.get('data')
    turnob = request.form.get('turno')
    batismos.append([nomeb, datab, turnob])

    mensagem = 'Seu batizado foi marcado com sucesso!'
    return render_template('adicionarbatizado.html', msg=mensagem)

#LISTAR OS BATIZADOS
@app.route('/listarbatismos', methods=['get'])
def listar_batismo():
    if len(batismos) > 0:
        return render_template('listarbatizados.html', lista=batismos)


#ADICIONAR CATECUMENO
@app.route('/adicionarcatecumeno', methods=['post'])
def adicionar_catecumeno():
    global catecumeno
    nome = request.form.get('nome')
    datadenascimento = request.form.get('data de nascimento')
    bairro = request.form.get('bairro')
    catecumeno.append([nome,datadenascimento,bairro])
    mensagem = 'Catecúmeno adicionado com sucesso!'
    return render_template('adicionarcatecumeno.html', msg=mensagem)


#LISTAR CATECUMENOS
@app.route('/listarcatecumeno', methods=['get'])
def listar_catecumeno():
    if len(catecumeno) > 0:
        return render_template('listarcatecumeno.html', lista=catecumeno)


#ADICIONAR ENCONTRO
@app.route('/adicionarencontro', methods=['post'])
def adicionar_encontro():
    global encontro
    data = request.form.get('data')
    horario = request.form.get('horario')
    local = request.form.get ('local')
    encontro.append([data,horario,local])
    mensagem2 = 'Encontro adicionado com sucesso!'
    return render_template('adicionarencontro.html', msg=mensagem2)

#IFRAME QUE LEVA PARA A PÁGINA adicionarencontro.html
@app.route('/mostraradicionare')
def mostrar_add_encontro():
    return render_template('adicionarencontro.html')

#LISTAR ENCONTROS
@app.route('/listarencontros', methods=['get'])
def listar_encontros():
    if len(encontro) > 0:
        return render_template('listarencontro.html', lista=encontro)

#LISTAR OS COROINHAS
@app.route('/mostrarlistarescala', methods=['get'])
def listar_coroinhas():
    if len(coroinhas) > 0:
        return render_template('listarcoroinhas.html', lista=coroinhas)

#LISTAR AS REUNIÕES
@app.route('/mostrarlistarreuniao', methods=['get'])
def listar_reunioescor():
    if len(reuniaocor) > 0:
        return render_template('listarreuniaocor.html', lista=reuniaocor)

#LISTAR SUBSTITUIÇÕES
@app.route('/mostrarlistarsubs', methods=['get'])
def listar_subscor():
    if len(subscor) > 0:
        return render_template('listarsubscor.html', lista=subscor)

#LISTAR OS PASCOM
@app.route('/mostrarlistarescalapas', methods=['get'])
def listar_pascom():
    if len(pascom) > 0:
        return render_template('listarpascom.html', lista=pascom)

#LISTAR AS REUNIÕES PASCOM
@app.route('/mostrarlistarreuniaopas', methods=['get'])
def listar_reunioespas():
    if len(reuniaopas) > 0:
        return render_template('listarreuniaopas.html', lista=reuniaopas)

#LISTAR SUBSTITUIÇÕES PASCOM
@app.route('/mostrarlistarsubspas', methods=['get'])
def listar_subspas():
    if len(subspas) > 0:
        return render_template('listarsubspas.html', lista=subspas)

#LISTAR OS LITURGIANOS
@app.route('/mostrarlistarescalali', methods=['get'])
def listar_liturgianos():
    if len(liturgia) > 0:
        return render_template('listarliturgia.html', lista=liturgia)

#LISTAR AS REUNIÕES DA LITURGIA
@app.route('/mostrarlistarreuniaoli', methods=['get'])
def listar_reunioesli():
    if len(reuniaoli) > 0:
        return render_template('listarreuniaoli.html', lista=reuniaoli)

#LISTAR SUBSTITUIÇÕES LITURGIA
@app.route('/mostrarlistarsubsli', methods=['get'])
def listar_subsli():
    if len(subsli) > 0:
        return render_template('listarsubsli.html', lista=subsli)

if __name__ == '__main__':
    app.run()