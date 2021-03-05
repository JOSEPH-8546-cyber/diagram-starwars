import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()


#clase del usuario
class UserName_Dates(Base):
    __tablename__ = 'UserName_Dates'
    id = Column(Integer, primary_key=True)
    username = Column(String(20))
    email = Column(String(25))
    password = Column(String(6)) 
    bio = Column(String(200))
   

#clase de los favoritos de los planetas
class FavList_Planets(Base):
    __tablename__ = 'FavList_Planets'
    id = Column(Integer, primary_key= True)
    id_planet = Column(Intiger, ForeignKey("Planets_Dates.id"))
    user_id = Column(String, ForeignKey ("UserName_Dates.id"))
    Comments = Column(String(200))



#clase de los datos de los planetas
class Planets_Dates (Base):
    __tablename__ = 'Planets_Dates'
    id = Column(Integer, primary_key=True) 
    name_planet = Column(String(200), nullable=False)
    diameter = Column(String(60))
    rotation_period = Column(String(60))
    orbital_period = Column(String(60))
    gravity = Column(String(60))
    gravity_type = Column(String(60))
    population = Column(String(60))
    climate = Column(String(60))
    terrain = Column(String(60))
    surface_water = Column(String(60))



#clase de los personajes favoritos
class FavList_Charts(Base):
    __tablename__ = 'FavList_Charts'
    id = Column(Integer, primary_key=True)
    id_charts = Column(Integer(), ForeignKey("Charts_Dates.id"))
    user_id = Column(Integer, ForeignKey ("UserName_Dates.id"))
    Comments = Column(String(200))


#clase de datos de los personajes
class Charts_Dates (Base):
    __tablename__ = 'Charts_Dates'
    id = Column(Integer, primary_key = True)
    name_chart = Column(String(200), nullable=False)
    height = Column(String(60))
    mass = Column(String(60))
    hair_color = Column(String(60))
    skin_color = Column(String(60))
    eye_color = Column(String(60))
    birth_year = Column(DateTime(60))
    gender = Column(String(60))





#clase de la lista de favoritos de starships
class FavList_Starships(Base):
    __tablename__ = 'FavList_Starships'
    id = Column(Integer, primary_key=True)
    id_starships = Column(Integer,ForeignKey("Starships_Dates"))
    user_id = Column(String, ForeignKey ("UserName_Dates.id"))
    Comments = Column(String(200)) 


#clase de datos de las starships
class Starships_Dates (Base):
    __tablename__ = 'Starships_Dates'
    id = Column(Integer, primary_key =True)
    name_starship = Column(String(200), nullable=False)
    model = Column(String(25))
    starship_class =  Column(String(25)) 
    manufacturer = Column(String(35)) 
    cost_in_credits = Column(String(60)) 
    length = Column(String(60)) 
    crew = Column( String(60))
    passengers = Column(String(60)) 
    max_atmosphering_speed = Column( String(60))
    hyperdrive_rating = Column(String(60)) 
    MGLT = Column(String(60)) 
    cargo_capacity = Column(String(60)) 
    consumables = Column(String(10)) 
    pilots = Column(String(15)) 





    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')