from sqlalchemy.orm import scoped_session
from modelos.modelos import Usuario

class EventoDAO:
    #construtor da classe: instanciar um objeto, ele cria uma sessao
    def __init__(self, session: scoped_session):
        self.session = session

