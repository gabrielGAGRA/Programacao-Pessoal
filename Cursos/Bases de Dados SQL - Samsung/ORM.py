from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import declarative_base, Session
from sqlalchemy import MetaData, Column, Integer, String
from sqlalchemy import create_engine
from sqlalchemy import text

# Cria a engine para o banco de dados
eng_postgres = create_engine("postgresql://xancgsdk:1Nkv3myMasVKFvDvpBFBjXsysHkBevf3@isabelle.db.elephantsql.com/xancgsdk")
eng_sqlite = create_engine("sqlite:///pokemon.bd")

# Classes Bases e Sessão
meta_orm = MetaData()
Base = declarative_base(metadata=meta_orm)

class Treinador(Base):
  __tablename__ = "treinadores"
  codigo = Column(Integer, primary_key=True, autoincrement=True)
  nome = Column(String(25), nullable=False, unique=True)
  cidade = Column(String(25))
  insignias = Column(Integer, default=0)

  def __repr__(self):
    return f"<Treinador({self.nome})>"

  def ganhar_insignia(self):
    self.insignias +=1
    
"""
sem conexao ao banco
t1= Treinador(nome="Ash", cidade="Pallet", insignias=8)

t1.ganhar_insignia()

print(t1.insignias)
"""

#conectando ao banco
Base.metadata.reflect(eng_postgres)
Base.metadata.create_all(bind=eng_postgres)

t1 = Treinador(nome="Ash", cidade="Pallet", insignias=8)
t2 = Treinador(nome="Misty", cidade="Cerulean", insignias=3)
t3 = Treinador(nome="Brock", cidade="Pewter", insignias=4)

ash = Treinador(nome="Ash", cidade="Pallet", insignias=8)
ash.ganhar_insignia()

with Session(eng_postgres) as sessao:
  sessao.add_all([t1, t2, t3])
  try:
      sessao.add(ash)
  except IntegrityError():
      print("Treinador já existe")