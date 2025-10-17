import sqlite3

# 1️⃣ Conectar (ou criar) o banco de dados
conexao = sqlite3.connect("meu_banco.db")
cursor = conexao.cursor()

# 2️⃣ Criar tabela CLIENTES
cursor.execute("""
CREATE TABLE IF NOT EXISTS clientes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    cpf TEXT UNIQUE NOT NULL,
    email TEXT,
    telefone TEXT,
    endereco TEXT,
    cidade TEXT,
    estado TEXT
)
""")

# 3️⃣ Inserir dados de exemplo
cursor.execute("""
INSERT INTO clientes (nome, cpf, email, telefone, endereco, cidade, estado)
VALUES ('Ana Carolina', '123.456.789-00', 'ana@email.com', '21999999999', 'Rua A, 123', 'Niterói', 'RJ')
""")

cursor.execute("""
INSERT INTO clientes (nome, cpf, email, telefone, endereco, cidade, estado)
VALUES ('Leonardo Torres', '987.654.321-00', 'leo@email.com', '21988888888', 'Rua B, 456', 'Rio de Janeiro', 'RJ')
""")

conexao.commit()

# 4️⃣ Ler os dados
cursor.execute("SELECT * FROM clientes")
registros = cursor.fetchall()

print("📋 Clientes cadastrados:")
for r in registros:
    print(r)

# 5️⃣ Fechar conexão
conexao.close()

