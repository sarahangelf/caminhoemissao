from flask import *

app = Flask(__name__)

app.secret_key = 'KJH#45K45JHQASs'

usuarios = [['sarah','1',['batismo','catecumenato', 'coroinhas', 'liturgia', 'pascom', 'terco']], ['nicolly', '7', ['batismo','catecumenato', 'coroinhas', 'liturgia', 'pascom', 'terco']]] #nome, senha, pastoral
batismos = [['levi', '16/08', 'manhã'], ['maria', '24/08', 'noite']] #LISTA DE BATIZADOS
catecumeno= [['maria','23/09','boa vista'], ['jose','24/09','bela vista']] #LISTA DE CATECUMENOS
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
voluntarios=[['Nicolly','25/10','coral'],['cleiton','25/10','misterio']] #LISTA DE VOLUNTÁRIOS
reuniaoterco=[['20/10','19:00','matriz']] #LISTA DE REUNIÕES DO TERÇO
musicasterco=[['acaso não sabeis','colo de Deus','3 mistério'],['ave maria','colo de Deus','entrada de Nossa Senhora']] #LISTA DE MÚSICAS DO TERÇO

@app.route('/')
def pagina_principal():
    return render_template('home/paginainicial.html')



@app.route('/escolhapq', methods=['post'])
def escolhenp():
    op = request.form.get('escolha')
    login = request.form.get('login')
    senha = request.form.get('senha')

    for user in usuarios:
        if user[0] == login and user[1] == senha:
            session['login'] = login
            return render_template('home/menu.html')

    '''logado = False
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
     msg = '*ERRO! O login ou a senha está errado!'
     return render_template('home/paginainicial.html', erro = msg)'''


#LEVAR PARA MENU
@app.route('/menu')
def mostrar_menu():
    if 'login' in session:
        if len(batismos) > 0:
            return render_template('home/menu.html')
    else:
        return render_template('home/paginainicial.html')


#LEVAR PARA BATISMO
@app.route('/batismo')
def mostrar_batismo():
    if 'login' in session:
        if len(batismos) > 0:
            return render_template('batismo/batismo.html')
    else:
        return render_template('home/paginainicial.html')


#LEVAR PARA CATECUMENATO
@app.route('/catecumenato')
def mostrar_catecumenato():
    if 'login' in session:
        if len(catecumeno) > 0:
            return render_template('catecumenato/catecumenato.html')
    else:
        return render_template('home/paginainicial.html')


#LEVAR PARA COROINHAS
@app.route('/coroinhas')
def mostrar_coroinhas():
    if 'login' in session:
        if len(coroinhas) > 0:
            return render_template('coroinhas/coroinhas.html')

    else:
        return render_template('home/paginainicial.html')

#LEVAR PARA LITURGIA
@app.route('/liturgia')
def mostrar_liturgia():
    if 'login' in session:
        if len(liturgianos) > 0:
            return render_template('liturgia/liturgia.html')

    else:
        return render_template('home/paginainicial.html')


#LEVAR PARA PASCOM
@app.route('/pascom')
def mostrar_pascom():
    if 'login' in session:
        if len(pascom) > 0:
            return render_template('pascom/pascom.html')

    else:
        return render_template('home/paginainicial.html')


#LEVAR PARA TERÇO
@app.route('/terco')
def mostrar_terco():
    if 'login' in session:
        if len(voluntarios) > 0:
            return render_template('terco/terco.html')

    else:
        return render_template('home/paginainicial.html')


#LEVAR PARA A PÁGINA DE CADASTRAR USUÁRIO
@app.route('/mostraradicionaru')
def mostrar_add_usuario():
    if 'login' in session:
        if len(usuarios) > 0:
            return render_template('home/cadastraru.html')

    else:
        return render_template('home/paginainicial.html')


#ADICIONAR USUÁRIO
@app.route('/adicionarusuario', methods=['post'])
def adicionar_usuario():
    if 'login' in session:
        global usuarios
        if len(usuarios) > 0:
            login = request.form.get('login')
            senha = request.form.get('senha')
            pastoral = request.form.get('pastoral')
            usuarios.append([login,senha,pastoral])
            print (usuarios)
            mensagem = 'Usuário adicionado com sucesso!'
            return render_template('home/paginainicial.html', msgc=mensagem)

    else:
        return render_template('home/paginainicial.html')



@app.route('/verificarlogin', methods=['post'])
def verificar_logado():
    if 'login' in session:
        if len(usuarios) > 0:
            login = request.form.get('login')
            senha = request.form.get('senha')

            return render_template('home/paginainicial.html')

    else:
        return render_template('home/paginainicial.html')


#IFRAME QUE LEVA PARA A PÁGINA adicionarbatizado.html
@app.route('/mostraradicionarb')
def mostrar_add_batizado():
    if 'login' in session:
        if len(batismos) > 0:
            return render_template('batismo/adicionarbatizado.html')
    else:
        return render_template('home/paginainicial.html')



#ADICIONAR BATIZADO
@app.route('/adicionarbatizado', methods=['post'])
def adicionar_batizado():
    if 'login' in session:
        global batismos
        if len(batismos) > 0:
            nomeb = request.form.get('nome')
            datab = request.form.get('data')
            turnob = request.form.get('turno')
            batismos.append([nomeb, datab, turnob])

            mensagem = 'Seu batizado foi marcado com sucesso!'
            return render_template('batismo/adicionarbatizado.html', msg=mensagem)
    else:
        return render_template('home/paginainicial.html')

#LISTAR OS BATIZADOS
@app.route('/listarbatismos', methods=['get'])
def listar_batismo():
    if 'login' in session:
        if len(batismos) > 0:
            return render_template('batismo/listarbatizados.html', lista=batismos)
    else:
        return render_template('home/paginainicial.html')

#ADICIONAR CATECUMENO
@app.route('/adicionarcatecumeno', methods=['post'])
def adicionar_catecumeno():
    if 'login' in session:
        global catecumeno
        if len(catecumeno) > 0:
            nome = request.form.get('nome')
            datadenascimento = request.form.get('datadenascimento')
            bairro = request.form.get('bairro')
            catecumeno.append([nome,datadenascimento,bairro])
            mensagem = 'Catecúmeno adicionado com sucesso!'
            return render_template('catecumenato/adicionarcatecumeno.html', msg=mensagem)

    else:
        return render_template('home/paginainicial.html')


#LISTAR CATECUMENOS
@app.route('/listarcatecumeno', methods=['get'])
def listar_catecumeno():
    if len(catecumeno) > 0:
        return render_template('catecumenato/listarcatecumeno.html', lista=catecumeno)


#ADICIONAR ENCONTRO
@app.route('/adicionarencontro', methods=['post'])
def adicionar_encontro():
    if 'login' in session:
        global encontro
        if len(encontro) > 0:
            data = request.form.get('data')
            horario = request.form.get('horario')
            local = request.form.get ('local')
            encontro.append([data,horario,local])
            mensagem2 = 'Encontro adicionado com sucesso!'
            return render_template('catecumenato/adicionarencontro.html', msg=mensagem2)


#IFRAME QUE LEVA PARA A PÁGINA adicionarencontro.html
@app.route('/mostraradicionare')
def mostrar_add_encontro():
    if 'login' in session:
        if len(encontro) > 0:
         return render_template('catecumenato/adicionarencontro.html')

#IFRAME QUE LEVA PARA A PÁGINA adicionarcatecumeno.html
@app.route('/mostraradicionarc')
def mostrar_add_catecumeno():
    if 'login' in session:
        if len(catecumeno) > 0:
            return render_template('catecumenato/adicionarcatecumeno.html')

#LISTAR ENCONTROS
@app.route('/listarencontros', methods=['get'])
def listar_encontros():
    if 'login' in session:
         if len(encontro) > 0:
            return render_template('catecumenato/listare.html', lista=encontro)

#LISTAR OS COROINHAS
@app.route('/mostrarlistarescala', methods=['get'])
def listar_coroinhas():
    if 'login' in session:
         if len(coroinhas) > 0:
            return render_template('coroinhas/listarcoroinhas.html', lista=coroinhas)

#LISTAR AS REUNIÕES
@app.route('/mostrarlistarreuniao', methods=['get'])
def listar_reunioescor():
    if 'login' in session:
        if len(reuniaocor) > 0:
            return render_template('coroinhas/listarreuniaocor.html', lista=reuniaocor)

#LISTAR SUBSTITUIÇÕES
@app.route('/mostrarlistarsubs', methods=['get'])
def listar_subscor():
    if 'login' in session:
         if len(subscor) > 0:
            return render_template('coroinhas/listarsubscor.html', lista=subscor)

#LISTAR OS PASCOM
@app.route('/mostrarlistarescalapas', methods=['get'])
def listar_pascom():
    if 'login' in session:
        if len(pascom) > 0:
            return render_template('pascom/listarpascom.html', lista=pascom)

#LISTAR AS REUNIÕES PASCOM
@app.route('/mostrarlistarreuniaopas', methods=['get'])
def listar_reunioespas():
    if 'login' in session:
        if len(reuniaopas) > 0:
            return render_template('pascom/listarreuniaopas.html', lista=reuniaopas)

#LISTAR SUBSTITUIÇÕES PASCOM
@app.route('/mostrarlistarsubspas', methods=['get'])
def listar_subspas():
    if 'login' in session:
        if len(subspas) > 0:
            return render_template('pascom/listarsubspas.html', lista=subspas)

#LISTAR OS LITURGIANOS
@app.route('/mostrarlistarescalali', methods=['get'])
def listar_liturgianos():
    if 'login' in session:
        if len(liturgianos) > 0:
            return render_template('liturgia/listarliturgia.html', lista=liturgianos)

#LISTAR AS REUNIÕES DA LITURGIA
@app.route('/mostrarlistarreuniaoli', methods=['get'])
def listar_reunioesli():
    if 'login' in session:
        if len(reuniaoli) > 0:
            return render_template('liturgia/listarreuniaoli.html', lista=reuniaoli)

#LISTAR SUBSTITUIÇÕES LITURGIA
@app.route('/mostrarlistarsubsli', methods=['get'])
def listar_subsli():
    if 'login' in session:
        if len(subsli) > 0:
            return render_template('liturgia/listarsubli.html', lista=subsli)

#LISTAR OS VOLUNTÁRIOS DO TERÇO
@app.route('/mostrarlistarescalaterco', methods=['get'])
def listar_voluntarios():
    if 'login' in session:
        if len(voluntarios) > 0:
            return render_template('terco/listarescalasterco.html', lista=voluntarios)

#LISTAR AS REUNIÕES DO TERÇO
@app.route('/mostrarlistarreuniaoterco', methods=['get'])
def listar_reunioesterco():
    if 'login' in session:
        if len(reuniaoterco) > 0:
            return render_template('terco/listarreuniaoterco.html', lista=reuniaoterco)

#LISTAR MÚSICAS TERÇO
@app.route('/mostrarlistarmusicasterco', methods=['get'])
def listar_musicasterco():
    if 'login' in session:
        if len(musicasterco) > 0:
            return render_template('terco/listarmusicasterco.html', lista=musicasterco)

if __name__ == '__main__':
    app.run()