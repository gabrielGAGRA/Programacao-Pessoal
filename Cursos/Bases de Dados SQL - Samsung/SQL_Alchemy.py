from sqlalchemy import create_engine
from sqlalchemy import text

# Cria a engine para o banco de dados
eng_postgres = create_engine("postgresql://xancgsdk:1Nkv3myMasVKFvDvpBFBjXsysHkBevf3@isabelle.db.elephantsql.com/xancgsdk")
eng_sqlite = create_engine("sqlite:///pokemon.bd")

con_sqlite = eng_sqlite.connect()
con_postgres = eng_postgres.connect()

query = text("""
CREATE TABLE treinadores(
  id SERIAL PRIMARY KEY,
  nome VARCHAR(15),
  cidade VARCHAR(15),
  insignias SMALLINT
);
""")

query.text

con_sqlite.execute(query)

treinadores = [
    {
        'nome': 'Ash',
        'cidade': 'Pallet',
        'insignias': 0
    },
    {
        'nome': 'Feulo',
        'cidade': 'SP',
        'insignias': 5
    },
    {
        'nome': 'Brock',
        'cidade': 'Pewter',
        'insignias': 2
    }
  ]

for treinador in treinadores:
  con_sqlite.execute(text(f"INSERT INTO Treinadores(nome, cidade, insignias) VALUES ('{treinador['nome']}', '{treinador['cidade']}', '{treinador['insignias']}')"))
