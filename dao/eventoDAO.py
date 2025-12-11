from sqlalchemy.orm import scoped_session
from modelos.modelos import Evento

class EventoDAO:
    #construtor da classe: instanciar um objeto, ele cria uma sessao
    def __init__(self, session: scoped_session):
        self.session = session

    def criar(self, evento):
        #adiciona um objeto/modelo no banco de dados
        self.session.add(evento)
        #autorizando modificações no banco/ gravando a alteração
        self.session.commit()

    def listar_usuarios(self):
        return self.session.query(Evento).all()

    def listar_eventos_por_tipo(self, tipo_evento):
        return self.session.query(Evento).filter_by(tipo=tipo_evento).all()

