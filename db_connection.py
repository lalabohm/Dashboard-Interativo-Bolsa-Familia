import mysql.connector

def connect_to_database(host, user, password, database=None):
    """
    Função para estabelecer conexão com o banco de dados MySQL.
    """
    try:
        print("Tentando conectar ao banco de dados...")
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="larissabohm",
            database="bolsa_familia_db"
        )
        print("Conexão estabelecida com sucesso!")
        return connection
    except mysql.connector.Error as err:
        print(f"Erro ao conectar ao banco de dados: {err}")
        return None

def close_connection(connection):
    """
    Função para fechar a conexão com o banco de dados.
    """
    if connection:
        connection.close()
        print("Conexão encerrada com sucesso.")

# Testar a conexão
if __name__ == "__main__":
    host = "localhost"
    user = "root"
    password = "larissabohm"
    database = "bolsa_familia_db"

    connection = connect_to_database(host, user, password, database)

    if connection:
        print("Conexão está ativa. Realizando teste...")
        # Testando com uma query simples
        try:
            cursor = connection.cursor()
            cursor.execute("SHOW TABLES;")
            tables = cursor.fetchall()
            if tables:
                print("Tabelas encontradas no banco:")
                for table in tables:
                    print(f"- {table[0]}")
            else:
                print("Nenhuma tabela encontrada no banco.")
        except mysql.connector.Error as err:
            print(f"Erro ao executar a query: {err}")
        finally:
            close_connection(connection)
    else:
        print("Falha ao estabelecer a conexão.")


