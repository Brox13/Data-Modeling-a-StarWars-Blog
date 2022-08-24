import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

class Usuario(Base):
    __tablename__ = 'usuario'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    usuario_id = Column(Integer)
    nombre = Column(String(200), nullable=False)
    apellido = Column(String(200), nullable=False)
    email = Column(String(200), nullable=False)
    favoritos_id = Column(Integer, ForeignKey(Favoritos.id))

class Personajes(Base):
    __tablename__ = 'personajes'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    personaje_id = Column(Integer)
    nombre = Column(String(200))
    genero = Column(String(1))
    color_pelo = Column(String(150))
    color_ojos = Column(String(150))

class Planetas(Base):
    __tablename__ = 'planetas'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    planetas_id = Column(Integer)
    nombre = Column(String(200))
    habitantes = Column(Integer)

class Vehiculos(Base):
    __tablename__ = 'vehiculos'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    vehiculo_id = Column(Integer)
    nombre = Column(String(200))
    modelo = Column(String(200))
    fabricante = Column(String(200))
    precio = Column(Integer)
  
class Favoritos(Base):
    __tablename__ = 'favoritos'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.

    id = Column(Integer, primary_key=True)
    favoritos_id = Column(Integer)
    usuario_id = Column(Integer, ForeignKey(Usuario.id))
    personaje_id = Column(Integer, ForeignKey(Personajes.id))
    vehiculo_id = Column(Integer, ForeignKey(Vehiculos.id))
    

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'midiagrama.png')