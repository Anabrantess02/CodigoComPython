import sqlite3

# Conectar (ou criar) o banco de dados
conexao = sqlite3.connect("meu_banco.db")
cursor = conexao.cursor()

# Criar a tabela (se ainda não existir)
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

# Inserir registros (com tratamento para evitar duplicatas)
dados_clientes = [
    ("Ana Carolina", "123.456.789-00", "ana@email.com", "21999999999", "Rua A, 123", "Niterói", "RJ"),
    ("Leonardo Torres", "987.654.321-00", "leo@email.com", "21988888888", "Rua B, 456", "Rio de Janeiro", "RJ")
]

for cliente in dados_clientes:
    try:
        cursor.execute("""
        INSERT INTO clientes (nome, cpf, email, telefone, endereco, cidade, estado)
        VALUES (?, ?, ?, ?, ?, ?, ?)
        """, cliente)
    except sqlite3.IntegrityError:
        pass  # Se o CPF já existir, ignora o erro

# Confirmar alterações
conexao.commit()

# Ler e exibir os dados
cursor.execute("SELECT * FROM clientes")
clientes = cursor.fetchall()

print("\n📋 Lista de clientes cadastrados:\n")
for cliente in clientes:
    print(cliente)

# Fechar conexão
conexao.close()
 