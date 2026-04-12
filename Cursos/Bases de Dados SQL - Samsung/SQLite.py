import sqlite3

con = sqlite3.conect('base_dados.db')

con.execute("""
CREATE TABLE Treinadores (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  nome VARCHAR(30) NOT NULL UNIQUE,
  cidade VARCHAR(30),
  insignias INTEGER NOT NULL DEFAULT 0
);
""")

# Now, you can use the execute() method of the consor object to run SQL commands.
con.execute("""
CREATE TABLE Pokemon (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome VARCHAR(25) NOT NULL,
    tipo VARCHAR(12) NOT NULL,
    nivel INTEGER NOT NULL default 1,
    capturado_em DATE,
);
""")

con.execute("ALTER TABLE Pokemon ADD COLUMN treinador VARCHAR(25);")

con.execute("INSERT INTO Pokemon (nome, tipo, nivel, treinador) VALUES ('Pikachu', 'Elétrico', 5, 'Gabriel');")

con.execute("UPDATE Pokemon SET nivel=6 WHERE treinador = 'Gabriel' AND nome = 'Pikachu';")

con.execute("SELECT treinador, nome, nivel FROM Pokemon WHERE treinador = 'Gabriel';")

con.execute("SELECT * FROM Pokemon ORDER BY nivel DESC LIMIT 1;")

con.execute("SELECT treinador, AVG(nivel) AS media FROM pokemon GROUP BY treinador;")

#JOIN = junta colunas de tabelas, permutando elementos (cross, inner, outer)
#Ash com Ash, Ash com Gary, Gary com Ash, Gary com Gary.
#Cria tabela maior com todos os elementos que se correspondem

#Insignias INT CHECK (insignias >= 0)
#checa se o valor inputado é maior ou igual a 0

#ID NOT NULL PRIMARY KEY
#torna id nao nulo e declara como unico (chave principal)

#AUTO_INCREMENT 
#se nao for inputado, eh criado automaticamente

#REFERENCES
#cria chave estrangeira, que referencia coluna de outra tabela
#como treinador ID INTEGER FOREIGN KEY REFERENCES (Treinador.ID), ou seja referencia coluna ID da tabela Treinador


con.execute("""
CREATE TABLE Treinadores(
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  nome VARCHAR(30) NOT NULL UNIQUE,
  cidade VARCHAR(30),
  insignias INTEGER NOT NULL DEFAULT 0
);
            """)

con.execute("""
CREATE TABLE IF NOT EXISTS Pokemon(
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  nome VARCHAR(25) NOT NULL,
  tipo VARCHAR(20) NOT NULL,
  nivel INTEGER NOT NULL default 1,
  capturado_em DATE default CURRENT_DATE,
  id_treinador INTEGER NOT NULL REFERENCES Treinadores(id)
);
""")

treinadores = [
    {
        'nome': 'Ash',
        'cidade': 'Pallet'
    },
    {
        'nome': 'Feulo',
        'cidade': 'SP'
    },
    {
        'nome': 'Gary',
        'cidade': 'Pallet'
    }
  ]

for treinador in treinadores:
  con.execute(f"INSERT INTO treinadores(nome, cidade) VALUES ('{treinador['nome']}', '{treinador['cidade']}')")

rs = con.execute("SELECT * FROM Treinadores")

rs.arraysize

resultados = rs.fetchall()    # list[tuple[int, str, str, int]]

for treinador in rs.fetchall():
  if treinador[1] == 'Feulo':
    print(f"Campeão!! {treinador[1]}")
  else:
    print(f"Perdedor: {treinador[1]}")

con.execute("""INSERT INTO Pokemon (nome, tipo, nivel, capturado_em, id_treinador)
VALUES
('Bulbasaur', 'Grama', 5, CURRENT_DATE, (SELECT id FROM Treinadores ORDER BY RANDOM() LIMIT 1)),
('Charmander', 'Fogo', 6, CURRENT_DATE, (SELECT id FROM Treinadores ORDER BY RANDOM() LIMIT 1)),
('Squirtle', 'Água', 5, CURRENT_DATE, (SELECT id FROM Treinadores ORDER BY RANDOM() LIMIT 1)),
('Pikachu', 'Elétrico', 7, CURRENT_DATE, (SELECT id FROM Treinadores ORDER BY RANDOM() LIMIT 1)),
('Jigglypuff', 'Fada', 4, CURRENT_DATE, (SELECT id FROM Treinadores ORDER BY RANDOM() LIMIT 1)),
('Psyduck', 'Água', 5, CURRENT_DATE, (SELECT id FROM Treinadores ORDER BY RANDOM() LIMIT 1)),
('Geodude', 'Pedra', 6, CURRENT_DATE, (SELECT id FROM Treinadores ORDER BY RANDOM() LIMIT 1)),
('Snorlax', 'Normal', 8, CURRENT_DATE, (SELECT id FROM Treinadores ORDER BY RANDOM() LIMIT 1)),
('Magikarp', 'Água', 3, CURRENT_DATE, (SELECT id FROM Treinadores ORDER BY RANDOM() LIMIT 1)),
('Gengar', 'Fantasma', 9, CURRENT_DATE, (SELECT id FROM Treinadores ORDER BY RANDOM() LIMIT 1)),
-- Insira mais Pokémons aqui usando a mesma estrutura, ajustando os valores de nome, tipo, nível, capturado_em e id_treinador conforme necessário.
('Zubat', 'Venenoso', 4, CURRENT_DATE, (SELECT id FROM Treinadores ORDER BY RANDOM() LIMIT 1)),
('Golbat', 'Venenoso', 7, CURRENT_DATE, (SELECT id FROM Treinadores ORDER BY RANDOM() LIMIT 1)),
('Oddish', 'Grama', 5, CURRENT_DATE, (SELECT id FROM Treinadores ORDER BY RANDOM() LIMIT 1)),
('Gloom', 'Grama', 8, CURRENT_DATE, (SELECT id FROM Treinadores ORDER BY RANDOM() LIMIT 1)),
('Vileplume', 'Grama', 10, CURRENT_DATE, (SELECT id FROM Treinadores ORDER BY RANDOM() LIMIT 1)),
('Paras', 'Inseto', 3, CURRENT_DATE, (SELECT id FROM Treinadores ORDER BY RANDOM() LIMIT 1)),
('Parasect', 'Inseto', 6, CURRENT_DATE, (SELECT id FROM Treinadores ORDER BY RANDOM() LIMIT 1)),
('Venonat', 'Inseto', 4, CURRENT_DATE, (SELECT id FROM Treinadores ORDER BY RANDOM() LIMIT 1)),
('Venomoth', 'Inseto', 7, CURRENT_DATE, (SELECT id FROM Treinadores ORDER BY RANDOM() LIMIT 1)),
('Diglett', 'Terra', 5, CURRENT_DATE, (SELECT id FROM Treinadores ORDER BY RANDOM() LIMIT 1)),
('Dugtrio', 'Terra', 8, CURRENT_DATE, (SELECT id FROM Treinadores ORDER BY RANDOM() LIMIT 1)),
('Meowth', 'Normal', 4, CURRENT_DATE, (SELECT id FROM Treinadores ORDER BY RANDOM() LIMIT 1)),
('Persian', 'Normal', 7, CURRENT_DATE, (SELECT id FROM Treinadores ORDER BY RANDOM() LIMIT 1)),
('Psyduck', 'Água', 5, CURRENT_DATE, (SELECT id FROM Treinadores ORDER BY RANDOM() LIMIT 1)),
('Golduck', 'Água', 8, CURRENT_DATE, (SELECT id FROM Treinadores ORDER BY RANDOM() LIMIT 1)),
('Mankey', 'Lutador', 5, CURRENT_DATE, (SELECT id FROM Treinadores ORDER BY RANDOM() LIMIT 1)),
('Primeape', 'Lutador', 8, CURRENT_DATE, (SELECT id FROM Treinadores ORDER BY RANDOM() LIMIT 1)),
('Growlithe', 'Fogo', 5, CURRENT_DATE, (SELECT id FROM Treinadores ORDER BY RANDOM() LIMIT 1)),
('Arcanine', 'Fogo', 8, CURRENT_DATE, (SELECT id FROM Treinadores ORDER BY RANDOM() LIMIT 1)),
('Poliwag', 'Água', 4, CURRENT_DATE, (SELECT id FROM Treinadores ORDER BY RANDOM() LIMIT 1)),
('Poliwhirl', 'Água', 6, CURRENT_DATE, (SELECT id FROM Treinadores ORDER BY RANDOM() LIMIT 1)),
('Poliwrath', 'Água', 9, CURRENT_DATE, (SELECT id FROM Treinadores ORDER BY RANDOM() LIMIT 1)),
('Abra', 'Psíquico', 5, CURRENT_DATE, (SELECT id FROM Treinadores ORDER BY RANDOM() LIMIT 1)),
('Kadabra', 'Psíquico', 7, CURRENT_DATE, (SELECT id FROM Treinadores ORDER BY RANDOM() LIMIT 1)),
('Alakazam', 'Psíquico', 10, CURRENT_DATE, (SELECT id FROM Treinadores ORDER BY RANDOM() LIMIT 1)),
('Machop', 'Lutador', 6, CURRENT_DATE, (SELECT id FROM Treinadores ORDER BY RANDOM() LIMIT 1)),
('Machoke', 'Lutador', 8, CURRENT_DATE, (SELECT id FROM Treinadores ORDER BY RANDOM() LIMIT 1)),
('Machamp', 'Lutador', 10, CURRENT_DATE, (SELECT id FROM Treinadores ORDER BY RANDOM() LIMIT 1)),
('Bellsprout', 'Grama', 4, CURRENT_DATE, (SELECT id FROM Treinadores ORDER BY RANDOM() LIMIT 1)),
('Weepinbell', 'Grama', 6, CURRENT_DATE, (SELECT id FROM Treinadores ORDER BY RANDOM() LIMIT 1)),
('Victreebel', 'Grama', 9, CURRENT_DATE, (SELECT id FROM Treinadores ORDER BY RANDOM() LIMIT 1)),
('Tentacool', 'Água', 4, CURRENT_DATE, (SELECT id FROM Treinadores ORDER BY RANDOM() LIMIT 1)),
('Tentacruel', 'Água', 7, CURRENT_DATE, (SELECT id FROM Treinadores ORDER BY RANDOM() LIMIT 1)),
('Geodude', 'Pedra', 5, CURRENT_DATE, (SELECT id FROM Treinadores ORDER BY RANDOM() LIMIT 1));""")

con.commit()
# Then, close the conection to the database.
con.close()