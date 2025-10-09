from flask import *



app = Flask(__name__)

app.secret_key = 'KJH#45K45JHQASs'

usuarios = [['sarah','1',['batismo','catecumenato', 'coroinhas', 'liturgia', 'pascom', 'terco']], ['nicolly', '7', ['batismo','catecumenato', 'coroinhas', 'liturgia', 'pascom', 'terco']]] #nome, senha, pastoral
batismos = [['levi', '16/08', 'manhã'], ['maria', '24/08', 'noite']]
catecumeno= [['maria','23/09','boa vista'], ['jose','24/09','bela vista']]
encontro=[['29/08','manhã','salao'], ['30/08','tarde','igreja']]
coroinhas=[['alice', '04/09', 'microfone'], ['milena', '11/09', 'missal']] #NOME, DATA E FUNÇÃO
reuniaocor=[['13/09', '14:00', 'matriz']] #DATA, HORÁRIO E LOCAL
subscor=[['milena', '11/09', 'missal']] #SUBSTITUIÇÕES DE COROINHAS, NOME, DATA E FUNÇÃO
pascom=[['rafael', '04/09'], ['ana', '23/09']] #NOME, DATA
reuniaopas=[['17/09', '14:00', 'matriz']] #DATA, HORÁRIO E LOCAL
subspas=[['ana', '23/09']] #SUBSTITUIÇÕES DE PASCOM, NOME, DATA E FUNÇÃO
liturgianos=[['Helena','02/10','2 leitura'],['Cedilma','03/10','1 leitura']] #LITURGIANOS, NOME, DATA E FUNÇÃO
reuniaoli=[['matriz','26/10','manhã']] #LOCAL,DATA E HORÁRIO
subsli=[['Diene','02/10', '2 leitura']]#SUBSTITUIÇÕES DA LITURGIA, NOME, DATA E FUNÇÃO
voluntarios=[['Nicolly','25/10','coral'],['cleiton','25/10','misterio']]
reuniaoterco=[['20/10','19:00','matriz']]
musicasterco=[['acaso não sabeis','colo de Deus','3 mistério'],['ave maria','colo de Deus','entrada de Nossa Senhora']]

@app.route('/')
def pagina_principal():
    return render_template('paginainicial.html')

@app.route('/escolhapq', methods=['post'])
def escolhenp():
    op = request.form.get('escolha')
    login = request.form.get('login')
    senha = request.form.get('senha')

    for user in usuarios:
        if user[0] == login and user[1] == senha:
            session['login'] = login
            return render_template('menu.html')

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

#LEVAR PARA MENU
@app.route('/menu')
def mostrar_menu():
    return render_template('menu.html')

#LEVAR PARA BATISMO
@app.route('/batismo')
def mostrar_batismo():
    return render_template('batismo.html')

#LEVAR PARA CATECUMENATO
@app.route('/catecumenato')
def mostrar_catecumenato():
    return render_template('catecumenato.html')

#LEVAR PARA COROINHAS
@app.route('/coroinhas')
def mostrar_coroinhas():
    return render_template('coroinhas.html')

#LEVAR PARA LITURGIA
@app.route('/liturgia')
def mostrar_liturgia():
    return render_template('liturgia.html')

#LEVAR PARA PASCOM
@app.route('/pascom')
def mostrar_pascom():
    return render_template('pascom.html')

#LEVAR PARA TERÇO
@app.route('/terco')
def mostrar_terco():
    return render_template('terco.html')

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
    login = request.form.get('login')
    senha = request.form.get('senha')



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
    if 'login' in session:
        if len(batismos) > 0:
            return render_template('listarbatizados.html', lista=batismos)
    else:
        return render_template('paginainicial.html')

#ADICIONAR CATECUMENO
@app.route('/adicionarcatecumeno', methods=['post'])
def adicionar_catecumeno():
    global catecumeno
    nome = request.form.get('nome')
    datadenascimento = request.form.get('datadenascimento')
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

#IFRAME QUE LEVA PARA A PÁGINA adicionarcatecumeno.html
@app.route('/mostraradicionarc')
def mostrar_add_catecumeno():
    return render_template('adicionarcatecumeno.html')

#LISTAR ENCONTROS
@app.route('/listarencontros', methods=['get'])
def listar_encontros():
    if len(encontro) > 0:
        return render_template('listare.html', lista=encontro)

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
    if len(liturgianos) > 0:
        return render_template('listarliturgia.html', lista=liturgianos)

#LISTAR AS REUNIÕES DA LITURGIA
@app.route('/mostrarlistarreuniaoli', methods=['get'])
def listar_reunioesli():
    if len(reuniaoli) > 0:
        return render_template('listarreuniaoli.html', lista=reuniaoli)

#LISTAR SUBSTITUIÇÕES LITURGIA
@app.route('/mostrarlistarsubsli', methods=['get'])
def listar_subsli():
    if len(subsli) > 0:
        return render_template('listarsubli.html', lista=subsli)

#LISTAR OS VOLUNTÁRIOS DO TERÇO
@app.route('/mostrarlistarescalaterco', methods=['get'])
def listar_voluntarios():
    if len(voluntarios) > 0:
        return render_template('listarescalasterco.html', lista=voluntarios)

#LISTAR AS REUNIÕES DO TERÇO
@app.route('/mostrarlistarreuniaoterco', methods=['get'])
def listar_reunioesterco():
    if len(reuniaoterco) > 0:
        return render_template('listarreuniaoterco.html', lista=reuniaoterco)

#LISTAR MÚSICAS TERÇO
@app.route('/mostrarlistarmusicasterco', methods=['get'])
def listar_musicasterco():
    if len(musicasterco) > 0:
        return render_template('listarmusicasterco.html', lista=musicasterco)

if __name__ == '__main__':
    app.run()