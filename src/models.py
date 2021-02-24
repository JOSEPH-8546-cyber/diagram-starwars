import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Varchar, DateTime, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()


#clase del usuario
class UserName_Dates(Base):
    __tablename__ = 'UserName_Dates'
    id = Column(Integer, primary_key=True)
    username = Column(Varchar(20))
    email = Column(Varchar(25))
    password = Column(Varchar(6)) 
    bio = Column(Varchar(200))


#clase de los favoritos de los planetas
class FavList_Planets(Base):
    __tablename__ = 'FavList_Planets'
    id = Column(Integer, primary_key= True)
    uid = Column(Intiger, primary_key= True)
    user_id = Column(Varchar, ForeignKey ("UserName_Dates.id"))
    id_planets = Column(Integer())
    Comments = Column(Varchar(200))



#clase de los datos de los planetas
class Planets_Dates (Base):
    __tablename__ = 'Planets_Dates'
    id = Column(Integer, primary_key=True) 
    uid_planets = Column(Integer, ForeignKey ("FavList_Planets.uid")) 
    id_planets = Column(Integer, ForeignKey ("FavList_Planet.id_planets"))
    diameter = Column(Integer())
    rotation_period = Column(Integer())
    orbital_period = Column(Integer())
    gravity = Column(Integer())
    gravity_type = Column(Integer())
    population = Column(Integer())
    climate = Column(String())
    terrain = Column(String())
    surface_water = Column(String())



#clase de los personajes favoritos
class FavList_Charts(Base):
    __tablename__ = 'FavList_Charts'
    id = Column(Integer, primary_key=True)
    uid = Column(Intiger, primary_key = True)
    user_id = Column(Varchar, ForeignKey ("UserName_Dates.id"))
    id_charts = Column(Integer())
    Comments = Column(Varchar(200))


#clase de datos de los personajes
class Charts_Dates (Base):
    __tablename__ = 'Charts_Dates'
    id = Column(Integer, primary_key = True)
    uid_charts = Column(Integer, ForeignKey("FavList_Charts.uid"))
    id = Column(Integer, ForeignKey("FavList_Charts.id_charts"))
    name = Column(String())
    id_chart = Column()
    height = Column(Float())
    mass = Column(Float())
    hair_color = Column(String())
    skin_color = Column(String())
    eye_color = Column(String())
    birth_year = Column(DateTime())
    gender = Column(String())





#clase de la lista de favoritos de starships
class FavList_Starships(Base):
    __tablename__ = 'FavList_Starships'
    id = Column(Integer, primary_key=True)
    uid = Column(Integer, primary_key=True)
    user_id = Column(Varchar, ForeignKey ("UserName_Dates.id"))
    id_starships = Column(Integer())
    Comments = Column(Varchar(200)) 


#clase de datos de las starships
class Starships_Dates (Base):
    __tablename__ = 'Starships_Dates'
    id = Column(Integer, primary_key =True)
    uid_starships = Column(Integer, ForeignKey("FavList_Starships.uid"))
    id = Column(Integer, ForeignKey("FavList_Starships.id_starships") )
    name = Column(Varchar(15))
    model = Column(Varchar(25))
    starship_class =  Column(Varchar(25)) 
    manufacturer = Column(varchar(35)) 
    cost_in_credits = Column(Integer()) 
    length = Column(Integer()) 
    crew = Column( Float())
    passengers = Column(Float()) 
    max_atmosphering_speed = Column( String())
    hyperdrive_rating = Column(Float()) 
    MGLT = Column(Integer()) 
    cargo_capacity = Column(Integer()) 
    consumables = Column(Varchar(10)) 
    pilots = Column(Varchar(15)) 





    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')