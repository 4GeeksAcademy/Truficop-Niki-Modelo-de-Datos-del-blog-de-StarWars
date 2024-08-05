import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class Usuario(Base):
    __tablename__ = 'usuario'
    id = Column(Integer, primary_key=True)
    email = Column(String(250),nullable=False, unique=True)
    password = Column(String(250),nullable=False)
    nombre = Column(String(250),nullable=False)
    apellido = Column(String(250),nullable=False)
    fecha_de_subscripcion = Column(DateTime, nullable=False)
    favoritos_planetas = relationship('FavoritoPlaneta', backref='usuario')
    favoritos_personajes = relationship('FavoritoPersonaje', backref='usuario')


class Planeta(Base):
    __tablename__ = 'planeta'
    id = Column(Integer, primary_key=True)
    nombre = Column(String(250), nullable=False)
    population = Column(Integer, nullable=False)
    rotation_period = Column(Integer, nullable=False)
    orbital_period = Column(Integer, nullable=False)
    diameter = Column(Integer, nullable=False)
    gravity = Column(String(250), nullable=False)
    terrain = Column(String(250), nullable=False)
    surface = Column(String(250), nullable=False)
    climate = Column(String(250), nullable=False)
    favoritos_planetas = relationship('FavoritoPlaneta', backref='planeta')


class Personaje(Base):
    __tablename__ = 'personaje'
    id = Column(Integer, primary_key=True)
    nombre = Column(String(250), nullable=False)
    birth_year = Column(Integer, nullable=False)
    species = Column(String(250), nullable=False)
    height = Column(Integer, nullable=False)
    mass = Column(Integer, nullable=False)
    gender = Column(String(250), nullable=False)
    hair_color = Column(String(250), nullable=False)
    skin_color = Column(String(250), nullable=False)
    homeworld = Column(String(250), ForeignKey('planeta.id'))
    favoritos_personajes = relationship('FavoritoPersonaje', backref='personaje')


class FavoritoPlaneta(Base):
    __tablename__ = 'favorito_planeta'
    id = Column(Integer, primary_key=True)
    usuario_id = Column(Integer, ForeignKey('usuario.id'))
    planeta_id = Column(Integer, ForeignKey('planeta.id'))
    fecha_de_favorito = Column(DateTime, nullable=False)
    usuario = relationship('Usuario', backref='favoritos_planetas')
    planeta = relationship('Planeta', backref='favoritos_planetas')


class FavoritoPersonaje(Base):
    __tablename__ = 'favorito_personaje'
    id = Column(Integer, primary_key=True)
    usuario_id = Column(Integer, ForeignKey('usuario.id'))
    personaje_id = Column(Integer, ForeignKey('personaje.id'))
    fecha_de_favorito = Column(DateTime, nullable=False)
    usuario = relationship('Usuario', backref='favoritos_personajes')
    personaje = relationship('Personaje', backref='favoritos_personajes')


    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e
