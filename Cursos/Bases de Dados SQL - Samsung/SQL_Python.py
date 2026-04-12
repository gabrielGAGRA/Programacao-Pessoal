from sqlalchemy import create_engine
from sqlalchemy import Table, Column, Integer, String, MetaData

# Cria um ojeto de metadata. Metadatas são coleçoes de tabelas e sua infos
meta = MetaData()

eng_sqlite_3 = create_engine("sqlite:///pokemon_3.bd")
con_sqlite_3 = eng_sqlite_3.connect()

#Cria um objeto do tipo tabela que abstrai uma tabela no Banco de dados
treinadores = Table('treinadores', meta,
     Column('id', Integer, primary_key=True, autoincrement=True),
     Column('nome', String(25), unique=True, nullable=False),
     Column('cidade', String(25)),
     Column('insignias', Integer, default=0),
     extend_existing=True
)

print("The Name column:")
print(treinadores.columns.nome)
print(treinadores.c.nome)

print("Columns: ")
for col in treinadores.c:
    print(col)

print("Primary keys:")
for pk in treinadores.primary_key:
    print(pk)

print("The id column:")
print(treinadores.c.codigo.name)
print(treinadores.c.codigo.type)
print(treinadores.c.codigo.nullable)
print(treinadores.c.codigo.primary_key)

meta.reflect(bind=eng_sqlite_3)
for table in meta.tables:
    print(table)