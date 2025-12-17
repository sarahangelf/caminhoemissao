from flask import *
from dao.banco import *
from dao.usuarioDAO import UsuarioDAO
from dao.eventoDAO import  EventoDAO
from modelos.modelos import Usuario
from modelos.modelos import Evento

app = Flask(__name__)

app.secret_key = 'KJH#45K45JHQASs'



init_db()

@app.before_request
def pegar_sessao():
    g.session = Session()

@app.teardown_appcontext
def encerrar_sessao(exception=None):
    Session.remove()

@app.route('/')
def pagina_principal():
    return render_template('home/paginainicial.html')


#LEVAR PARA A PÁGINA DE CADASTRAR USUÁRIO
@app.route('/mostraradicionaru')
def mostrar_add_usuario():
    return render_template('home/login.html')




#ADICIONAR USUÁRIO
@app.route('/adicionarusuario', methods=['post'])
def adicionar_usuario():
    userdao = UsuarioDAO(g.session)

    email = request.form.get('email')
    senha = request.form.get('senha')
    tipo = request.form.get('tipo')
    pastoral = request.form.get('pastoral')

    novo_usuario = Usuario (email=email, senha=senha, tipo=tipo, pastoral=pastoral)
    userdao.criar(novo_usuario)

    print("FOI?")
    mensagem = 'Usuário adicionado com sucesso!'
    return render_template('home/paginainicial.html', msgc=mensagem)



#VERIFICAR SE O USUÁRIO ESTÁ LOGADO
@app.route('/verificarlogin', methods=['post'])
def verificar_logado():
    userdao = UsuarioDAO(g.session)

    email = request.form.get('email')
    senha = request.form.get('senha')

    usuario = userdao.autenticar(email, senha)

    if usuario:
        session['login'] = email
        return render_template('home/menu.html')
    else:
        mensagem = 'Usuário não encontrado, se cadastre!'
        return render_template('home/paginainicial.html', msgc=mensagem)

#LEVAR PARA MENU
@app.route('/menu')
def mostrar_menu():
    if 'login' in session:
        return render_template('home/menu.html')
    else:
        return render_template('home/paginainicial.html')


#LEVAR PARA O INICIO
@app.route('/paginainicial')
def mostrar_paginainicial():
        return render_template('home/paginainicial.html')

#LEVAR PARA BATISMO
@app.route('/batismo')
def mostrar_batismo():
    if 'login' in session:
            return render_template('batismo/batismo.html')
    else:
        return render_template('home/paginainicial.html')


#LEVAR PARA CATECUMENATO
@app.route('/catecumenato')
def mostrar_catecumenato():
    if 'login' in session:
            return render_template('catecumenato/catecumenato.html')
    else:
        return render_template('home/paginainicial.html')


#LEVAR PARA COROINHAS
@app.route('/coroinhas')
def mostrar_coroinhas():
    if 'login' in session:
            return render_template('coroinhas/coroinhas.html')

    else:
        return render_template('home/paginainicial.html')

#LEVAR PARA LITURGIA
@app.route('/liturgia')
def mostrar_liturgia():
    if 'login' in session:
            return render_template('liturgia/liturgia.html')

    else:
        return render_template('home/paginainicial.html')


#LEVAR PARA PASCOM
@app.route('/pascom')
def mostrar_pascom():
    if 'login' in session:
            return render_template('pascom/pascom.html')

    else:
        return render_template('home/paginainicial.html')


#LEVAR PARA TERÇO
@app.route('/terco')
def mostrar_terco():
    if 'login' in session:
            return render_template('terco/terco.html')

    else:
        return render_template('home/paginainicial.html')


#IFRAME QUE LEVA PARA A PÁGINA adicionarbatizado.html
@app.route('/mostraradicionarb')
def mostrar_add_batizado():
    if 'login' in session:
            return render_template('batismo/adicionarbatizado.html')
    else:
        return render_template('home/paginainicial.html')


#ADICIONAR BATIZADO
@app.route('/adicionarbatizado', methods=['post'])
def adicionar_batizado():
    if 'login' in session:
            eventodao = EventoDAO(g.session)

            nomeb = request.form.get('nome')
            tipob = request.form.get('tipo')
            datab = request.form.get('data')
            horab = request.form.get('hora')

            novo_evento = Evento (nome=nomeb,tipo=tipob, data=datab, hora=horab)

            mensagem = 'Seu batizado foi marcado com sucesso!'
            return render_template('batismo/adicionarbatizado.html', msg=mensagem)
    else:
        return render_template('home/paginainicial.html')

#LISTAR OS BATIZADOS
@app.route('/listarbatismos', methods=['get'])
def listar_batismo():
    if 'login' in session:
        eventodao = EventoDAO(g.session)

        batismos = eventodao.listar_eventos_por_tipo('batizado')
        return render_template('batismo/listarbatizados.html')
    else:
        return render_template('home/paginainicial.html')

#ADICIONAR CATECUMENO
@app.route('/adicionarcatecumeno', methods=['post'])
def adicionar_catecumeno():
    if 'login' in session:
            userdao = UsuarioDAO(g.session)

            email = request.form.get('email')
            datadenascimento = request.form.get('datadenascimento')
            bairro = request.form.get('bairro')

            usuario = userdao.autenticar(email, datadenascimento,bairro)
            mensagem = 'Catecúmeno adicionado com sucesso!'
            return render_template('catecumenato/adicionarcatecumeno.html', msg=mensagem)

    else:
        return render_template('home/paginainicial.html')


#LISTAR CATECUMENOS
@app.route('/listarcatecumeno', methods=['get'])
def listar_catecumeno():
    userdao = UsuarioDAO(g.session)

    usuario = userdao.listar_usuarios_por_pastoral('catecumenos')
    return render_template('catecumenato/listarcatecumeno.html')


#ADICIONAR ENCONTRO
@app.route('/adicionarencontro', methods=['post'])
def adicionar_encontro():
    if 'login' in session:
        eventodao = EventoDAO(g.session)

        nomec = request.form.get('nome')
        tipoc = request.form.get('tipo')
        datac = request.form.get('data')
        horac = request.form.get('hora')
    
        novo_evento = Evento(nome=nomec, tipo=tipoc, data=datac, hora=horac)

        mensagem2 = 'Encontro adicionado com sucesso!'
        return render_template('catecumenato/adicionarencontro.html', msg=mensagem2)


#IFRAME QUE LEVA PARA A PÁGINA adicionarencontro.html
@app.route('/mostraradicionare')
def mostrar_add_encontro():
    if 'login' in session:
         return render_template('catecumenato/adicionarencontro.html')

#IFRAME QUE LEVA PARA A PÁGINA adicionarcatecumeno.html
@app.route('/mostraradicionarc')
def mostrar_add_catecumeno():
    if 'login' in session:
            return render_template('catecumenato/adicionarcatecumeno.html')

#LISTAR ENCONTROS
@app.route('/listarencontros', methods=['get'])
def listar_encontros():
    if 'login' in session:
        eventodao = EventoDAO(g.session)

        encontro = eventodao.listar_eventos_por_tipo('encontro')
        return render_template('catecumenato/listare.html')

#LISTAR OS COROINHAS
@app.route('/mostrarlistarescala', methods=['get'])
def listar_coroinhas():
    if 'login' in session:
        userdao = UsuarioDAO(g.session)

        usuario = userdao.listar_usuarios_por_pastoral('coroinhas')
        return render_template('coroinhas/listarcoroinhas.html')

#LISTAR AS REUNIÕES COROINHAS
@app.route('/mostrarlistarreuniao', methods=['get'])
def listar_reunioescor():
    if 'login' in session:
        eventodao = EventoDAO(g.session)

        reunioescor = eventodao.listar_eventos_por_tipo('reunião')
        return render_template('coroinhas/listarreuniaocor.html')

#LISTAR SUBSTITUIÇÕES COROINHAS
@app.route('/mostrarlistarsubs', methods=['get'])
def listar_subscor():
    if 'login' in session:
        userdao = UsuarioDAO(g.session)

        usuario = userdao.listar_usuarios_por_pastoral('coroinhas')
        return render_template('coroinhas/listarsubscor.html')

#LISTAR OS PASCOM
@app.route('/mostrarlistarescalapas', methods=['get'])
def listar_pascom():
    if 'login' in session:
        userdao = UsuarioDAO(g.session)

        usuario = userdao.listar_usuarios_por_pastoral('pascom')
        return render_template('pascom/listarpascom.html')

#LISTAR AS REUNIÕES PASCOM
@app.route('/mostrarlistarreuniaopas', methods=['get'])
def listar_reunioespas():
    if 'login' in session:
        eventodao = EventoDAO(g.session)

        reunioespas = eventodao.listar_eventos_por_tipo('reunião')
        return render_template('pascom/listarreuniaopas.html')

#LISTAR SUBSTITUIÇÕES PASCOM
@app.route('/mostrarlistarsubspas', methods=['get'])
def listar_subspas():
    if 'login' in session:
        userdao = UsuarioDAO(g.session)

        usuario = userdao.listar_usuarios_por_pastoral('pascom')
        return render_template('pascom/listarsubspas.html')

#LISTAR OS LITURGIA
@app.route('/mostrarlistarescalali', methods=['get'])
def listar_liturgia():
    if 'login' in session:
        userdao = UsuarioDAO(g.session)

        usuario = userdao.listar_usuarios_por_pastoral('liturgia')
        return render_template('liturgia/listarliturgia.html')

#LISTAR AS REUNIÕES DA LITURGIA
@app.route('/mostrarlistarreuniaoli', methods=['get'])
def listar_reunioesli():
    if 'login' in session:
        eventodao = EventoDAO(g.session)

        reunioeslit = eventodao.listar_eventos_por_tipo('reunião')
        return render_template('liturgia/listarreuniaoli.html')

#LISTAR SUBSTITUIÇÕES LITURGIA
@app.route('/mostrarlistarsubsli', methods=['get'])
def listar_subsli():
    if 'login' in session:
        userdao = UsuarioDAO(g.session)

        usuario = userdao.listar_usuarios_por_pastoral('liturgia')
        return render_template('liturgia/listarsubli.html')

#LISTAR OS VOLUNTÁRIOS DO TERÇO
@app.route('/mostrarlistarescalaterco', methods=['get'])
def listar_voluntarios():
    if 'login' in session:
        userdao = UsuarioDAO(g.session)

        usuario = userdao.listar_usuarios_por_pastoral('voluntátios')
        return render_template('terco/listarescalasterco.html')

#LISTAR AS REUNIÕES DO TERÇO
@app.route('/mostrarlistarreuniaoterco', methods=['get'])
def listar_reunioesterco():
    if 'login' in session:
        eventodao = EventoDAO(g.session)

        reunioesterco = eventodao.listar_eventos_por_tipo('reunião')
        return render_template('terco/listarreuniaoterco.html')


if __name__ == '__main__':
    app.run()