import pyodbc
import os
from tkinter import messagebox
from dotenv import load_dotenv

# Carrega as variáveis de ambiente do arquivo .env
load_dotenv()

DB_CONFIG = {
    'driver': os.getenv('DB_DRIVER'),
    'server': os.getenv('DB_SERVER'),
    'database': os.getenv('DB_DATABASE'),
    'uid': os.getenv('DB_UID'),
    'pwd': os.getenv('DB_PWD')
}

def conectar_bd():
    """Tenta estabelecer uma conexão com o banco de dados."""
    try:
        conn_str = (
            f"DRIVER={DB_CONFIG['driver']};"
            f"SERVER={DB_CONFIG['server']};"
            f"DATABASE={DB_CONFIG['database']};"
            f"UID={DB_CONFIG['uid']};"
            f"PWD={DB_CONFIG['pwd']}"
        )
        conn = pyodbc.connect(conn_str)
        return conn
    except pyodbc.Error as ex:
        # Captura o SQLSTATE para uma mensagem de erro mais específica
        sqlstate = ex.args[0]
        messagebox.showerror("Erro de Conexão", f"Não foi possível conectar ao banco de dados.\nErro: {sqlstate}")
        return None

def adicionar_usuario_pagou_db(nome_usuario):
    #Adiciona um novo usuário que pagou à tabela T_USUARIO_PAGOU no banco de dados.
    conn = conectar_bd()
    if conn:
        cursor = conn.cursor()
        try:
            cursor.execute("INSERT INTO T_USUARIO_PAGOU (NOME_USUARIO_PAGOU) VALUES (?)", (nome_usuario,))
            conn.commit() # Confirma a transação no banco de dados
            messagebox.showinfo("Sucesso", f"Usuário '{nome_usuario}' adicionado com sucesso!")
            return True
        except pyodbc.Error as ex:
            sqlstate = ex.args[0]
            messagebox.showerror("Erro ao Adicionar", f"Não foi possível adicionar o usuário.\nErro: {sqlstate}")
            return False
        finally:
            conn.close() # Sempre fecha a conexão
    return False

def adicionar_tipo_gasto(nome_tipo_gasto):
    conn = conectar_bd()
    if conn:
        cursor = conn.cursor()
        try:
            cursor.execute("INSERT INTO T_TIPO_GASTO (nome_tipo_gasto) VALUES (?)", (nome_tipo_gasto,))
            conn.commit() # Confirma a transação no banco de dados
            messagebox.showinfo("Sucesso", f"Tipo de gasto: '{nome_tipo_gasto}' adicionado com sucesso!")
            return True
        except pyodbc.Error as ex:
            sqlstate = ex.args[0]
            messagebox.showerror("Erro ao Adicionar", f"Não foi possível adicionar o tipo de gasto.\nErro: {sqlstate}")
            return False
        finally:
            conn.close() # Sempre fecha a conexão
    return False

def adicionar_local_gasto(nome_local_gasto):
    conn = conectar_bd()
    if conn:
        cursor = conn.cursor()
        try:
            cursor.execute("INSERT INTO T_LOCAL_GASTO (nome_local_gasto) VALUES (?)", (nome_local_gasto,))
            conn.commit() # Confirma a transação no banco de dados
            messagebox.showinfo("Sucesso", f"Local de compra: '{nome_local_gasto}' adicionado com sucesso!")
            return True
        except pyodbc.Error as ex:
            sqlstate = ex.args[0]
            messagebox.showerror("Erro ao Adicionar", f"Não foi possível adicionar o local de compra.\nErro: {sqlstate}")
            return False
        finally:
            conn.close() # Sempre fecha a conexão
    return False


def adicionar_tipo_pagamento(nome_tipo_pagamento):
    conn = conectar_bd()
    if conn:
        cursor = conn.cursor()
        try:
            cursor.execute("INSERT INTO T_TIPO_PAGAMENTO (nome_tipo_pagamento) VALUES (?)", (nome_tipo_pagamento,))
            conn.commit() # Confirma a transação no banco de dados
            messagebox.showinfo("Sucesso", f"Tipo de pagamento: '{nome_tipo_pagamento}' adicionado com sucesso!")
            return True
        except pyodbc.Error as ex:
            sqlstate = ex.args[0]
            messagebox.showerror("Erro ao Adicionar", f"Não foi possível adicionar o tipo de pagamento.\nErro: {sqlstate}")
            return False
        finally:
            conn.close() # Sempre fecha a conexão
    return False

def adicionar_metodo_pagamento(nome_metodo_pagamento):
    conn = conectar_bd()
    if conn:
        cursor = conn.cursor()
        try:
            cursor.execute("INSERT INTO T_METODO_PAGAMENTO (nome_metodo_pagamento) VALUES (?)", (nome_metodo_pagamento,))
            conn.commit() # Confirma a transação no banco de dados
            messagebox.showinfo("Sucesso", f"Metodo de pagamento: '{nome_metodo_pagamento}' adicionado com sucesso!")
            return True
        except pyodbc.Error as ex:
            sqlstate = ex.args[0]
            messagebox.showerror("Erro ao Adicionar", f"Não foi possível adicionar o metodo de pagamento.\nErro: {sqlstate}")
            return False
        finally:
            conn.close() # Sempre fecha a conexão
    return False

def adicionar_cartao(nome_cartao, bandeira_cartao):
    conn = conectar_bd()
    if conn:
        cursor = conn.cursor()
        try:
            cursor.execute("INSERT INTO T_CARTAO (nome_cartao, bandeira_cartao) VALUES (?, ?)", (nome_cartao, bandeira_cartao))
            conn.commit() # Confirma a transação no banco de dados
            messagebox.showinfo("Sucesso", f"Informações do cartão: '{nome_cartao, bandeira_cartao}' adicionadas com sucesso!")
            return True
        except pyodbc.Error as ex:
            sqlstate = ex.args[0]
            messagebox.showerror("Erro ao Adicionar", f"Não foi possível adicionar as informações do cartão.\nErro: {sqlstate}")
            return False
        finally:
            conn.close() # Sempre fecha a conexão
    return False

def get_usuarios_db():
    #Busca os usuários no BD
    conn = conectar_bd()
    usuarios = []
    if conn:
        cursor = conn.cursor()
        try:
            cursor.execute("SELECT ID_USUARIO_PAGOU, NOME_USUARIO_PAGOU FROM T_USUARIO_PAGOU ORDER BY NOME_USUARIO_PAGOU")
            for row in cursor.fetchall():
                usuarios.append(row) # row é uma tupla (ID, Nome)
        except pyodbc.Error as ex:
            sqlstate = ex.args[0]
            messagebox.showerror("Erro ao Carregar Usuários", f"Não foi possível carregar os usuários.\nErro: {sqlstate}")
        finally:
            conn.close()
    return usuarios

def get_tipo_gasto_db():
    #Busca os tipos de gasto na database
    conn = conectar_bd()
    tipo_gasto = []
    if conn:
        cursor = conn.cursor()
        try:
            cursor.execute("SELECT ID_TIPO_GASTO, NOME_TIPO_GASTO FROM T_TIPO_GASTO ORDER BY NOME_TIPO_GASTO")
            for row in cursor.fetchall():
                tipo_gasto.append(row) 
        except pyodbc.Error as ex:
            sqlstate = ex.args[0]
            messagebox.showerror("Erro ao Carregar tipos de gasto", f"Não foi possível carregar os tipos de gasto.\nErro: {sqlstate}")
        finally:
            conn.close()
    return tipo_gasto

def get_local_gasto_db():
    #Busca os locais de gasto na database
    conn = conectar_bd()
    local_gasto = []
    if conn:
        cursor = conn.cursor()
        try:
            cursor.execute("SELECT ID_LOCAL_GASTO, NOME_LOCAL_GASTO FROM T_LOCAL_GASTO ORDER BY NOME_LOCAL_GASTO")
            for row in cursor.fetchall():
                local_gasto.append(row) 
        except pyodbc.Error as ex:
            sqlstate = ex.args[0]
            messagebox.showerror("Erro ao Carregar locais de gasto", f"Não foi possível carregar os locais de gasto.\nErro: {sqlstate}")
        finally:
            conn.close()
    return local_gasto

def get_tipo_pagamento_db():
    #Busca os tipos de pagamento na database
    conn = conectar_bd()
    tipo_pagamento = []
    if conn:
        cursor = conn.cursor()
        try:
            cursor.execute("SELECT ID_TIPO_PAGAMENTO, NOME_TIPO_PAGAMENTO FROM T_TIPO_PAGAMENTO ORDER BY NOME_TIPO_PAGAMENTO")
            for row in cursor.fetchall():
                tipo_pagamento.append(row) 
        except pyodbc.Error as ex:
            sqlstate = ex.args[0]
            messagebox.showerror("Erro ao Carregar tipos de pagamento", f"Não foi possível carregar os tipos de pagamento.\nErro: {sqlstate}")
        finally:
            conn.close()
    return tipo_pagamento

def get_metodo_pagamento_db():
    #Busca os metodos de pagamento
    conn = conectar_bd()
    metodo_pagamento = []
    if conn:
        cursor = conn.cursor()
        try:
            cursor.execute("SELECT ID_METODO_PAGAMENTO, NOME_METODO_PAGAMENTO FROM T_METODO_PAGAMENTO ORDER BY NOME_METODO_PAGAMENTO")
            for row in cursor.fetchall():
                metodo_pagamento.append(row) 
        except pyodbc.Error as ex:
            sqlstate = ex.args[0]
            messagebox.showerror("Erro ao Carregar metodos de pagamento", f"Não foi possível carregar os metodos de pagamento.\nErro: {sqlstate}")
        finally:
            conn.close()
    return metodo_pagamento

def get_cartao_db():
    #Busca os cartões
    conn = conectar_bd()
    cartao = []
    if conn:
        cursor = conn.cursor()
        try:
            cursor.execute("SELECT ID_CARTAO, NOME_CARTAO FROM T_CARTAO ORDER BY NOME_CARTAO")
            for row in cursor.fetchall():
                cartao.append(row) 
        except pyodbc.Error as ex:
            sqlstate = ex.args[0]
            messagebox.showerror("Erro ao Carregar os cartões", f"Não foi possível carregar os cartões.\nErro: {sqlstate}")
        finally:
            conn.close()
    return cartao

def salvar_nova_compra_db(data_compra, valor, id_tipo_gasto, id_local_gasto, id_tipo_pagamento, id_usuario, id_metodo_pagamento, descricao, id_cartao):
    # realiza o insert das informações de compra
    conn = conectar_bd()
    if conn:
        cursor = conn.cursor()
        try:
            cursor.execute("INSERT INTO T_REGISTROS_GASTO (DATA_GASTO, VALOR_GASTO, ID_TIPO_GASTO, ID_LOCAL_GASTO, ID_TIPO_PAGAMENTO, ID_USUARIO_PAGOU, ID_METODO_PAGAMENTO, OBSERVACOES, ID_CARTAO) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)",
                           (data_compra, valor, id_tipo_gasto, id_local_gasto, id_tipo_pagamento, id_usuario, id_metodo_pagamento, descricao, id_cartao))
            conn.commit()
            messagebox.showinfo("Sucesso", "Compra registrada com sucesso!")
            return True
        except pyodbc.Error as ex:
            sqlstate = ex.args[0]
            messagebox.showerror("Erro ao Registrar Compra", f"Não foi possível registrar a compra.\nErro: {sqlstate}")
            return False
        finally:
            conn.close()
    return False

def alterar_compra_db(data_compra, valor, id_tipo_gasto, id_local_gasto, id_tipo_pagamento, id_usuario, id_metodo_pagamento, descricao, id_cartao, id_compra):
    # realiza o update das informações de compra
    conn = conectar_bd()
    if conn:
        cursor = conn.cursor()
        try:
            cursor.execute("UPDATE T_REGISTROS_GASTO SET DATA_GASTO = ?, VALOR_GASTO = ?, ID_TIPO_GASTO = ?, ID_LOCAL_GASTO = ?, ID_TIPO_PAGAMENTO = ?, ID_USUARIO_PAGOU = ?, ID_METODO_PAGAMENTO = ?, OBSERVACOES = ?, ID_CARTAO = ? WHERE ID = ?",
                           (data_compra, valor, id_tipo_gasto, id_local_gasto, id_tipo_pagamento, id_usuario, id_metodo_pagamento, descricao, id_cartao, id_compra))
            conn.commit()
            messagebox.showinfo("Sucesso", "Compra registrada com sucesso!")
            return True
        except pyodbc.Error as ex:
            sqlstate = ex.args[0]
            messagebox.showerror("Erro ao alterar Compra", f"Não foi possível alterar a compra.\nErro: {sqlstate}")
            return False
        finally:
            conn.close()
    return False

def deletar_compra_db(id_compra):
    # realiza o delet das informações de compra
    conn = conectar_bd()
    if conn:
        cursor = conn.cursor()
        try:
            cursor.execute("DELETE FROM T_REGISTROS_GASTO WHERE ID = ?",
                           (id_compra))
            conn.commit()
            messagebox.showinfo("Sucesso", "Compra deletada com sucesso!")
            return True
        except pyodbc.Error as ex:
            sqlstate = ex.args[0]
            messagebox.showerror("Erro ao deletar Compra", f"Não foi possível deletar a compra.\nErro: {sqlstate}")
            return False
        finally:
            conn.close()
    return False
