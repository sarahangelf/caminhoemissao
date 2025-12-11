from sqlalchemy import Column, String, Integer, Boolean, DateTime, Float
from sqlalchemy.ext.declarative import declarative_base

#é um modelo que vai  representar uma tabela no BD
Base = declarative_base()
class Usuario(Base):
    __tablename__ = 'usuarios'

    email = Column(String, primary_key=True)
    nome = Column(String)
    tipo = Column(String)
    senha = Column(String)
    pastoral = Column(String)
    dataServir = Column(String)

    def __repr__(self):
        return f"<Usuario(email='{self.email}', nome='{self.nome}')>"

class Evento(Base):
    __tablename__ = 'eventos'

    id = Column(Integer, primary_key=True)
    nome = Column(String)
    tipo = Column(String)
    data = Column(String)
    hora = Column(String)
    local = Column(String)

    def __repr__(self):
        return f"<Evento(id='{self.id}', nome='{self.nome}')>"