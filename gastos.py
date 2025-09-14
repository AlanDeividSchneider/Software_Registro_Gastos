
import tkinter as tk
from tkinter import messagebox, ttk
import pyodbc
import datetime
from tkcalendar import Calendar

# --- Configurações do Banco de Dados ---
DB_CONFIG = {
    'driver': '{ODBC Driver 17 for SQL Server}', # Pode variar dependendo da sua instalação
    'server': '127.0.0.1',                       # Ex: 'localhost\\SQLEXPRESS' ou 'MEU_SERVIDOR'
    'database': 'GASTOS',                        # Ex: 'MinhaEmpresaDB'
    'uid': 'sa',                                 # Ex: 'sa'
    'pwd': '12345678'                            # Ex: 'MinhaSenhaForte123'
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

# --- Funções de Operação do Banco de Dados ---
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

# --- Funções para Gerenciar as Telas (Frames) ---

def clear_frame(frame):
    #Remove todos os widgets de um frame para preparar para um novo conteúdo.
    for widget in frame.winfo_children():
        widget.destroy()

def show_main_menu(app_instance):
    #Exibe o menu principal da aplicação com os botões para as telas principais.    
    clear_frame(app_instance.content_frame) # Limpa o frame de conteúdo atual

    # Título de boas-vindas
    label_welcome = tk.Label(app_instance.content_frame, text="Bem-vindo ao Sistema de Gastos", font=("Arial", 18, "bold"))
    label_welcome.pack(pady=20)

    # configurações do menu compras
    btn_compras = tk.Button(app_instance.content_frame, text="Compras", command=lambda: show_compras_screen(app_instance.content_frame), width=20, height=2)
    btn_compras.pack(pady=10)

    # configurações do menu configurações
    btn_configuracoes = tk.Button(app_instance.content_frame, text="Cadastros", command=lambda: show_cadastros_screen(app_instance.content_frame), width=20, height=2)
    btn_configuracoes.pack(pady=10)

    # configurações do menu relatórios
    btn_relatorios = tk.Button(app_instance.content_frame, text="Relatórios", command=lambda: show_relatorios_screen(app_instance.content_frame), width=20, height=2)
    btn_relatorios.pack(pady=10)

def show_compras_screen(content_frame):
    #Exibe a tela do menu 'Compras' com suas sub-opções.
    clear_frame(content_frame) # Limpa o frame para o conteúdo de Compras
    
    label_title = tk.Label(content_frame, text="Compras", font=("Arial", 16, "bold"))
    label_title.pack(pady=10)

    # Sub-opções para nova compra
    btn_nova_compra = tk.Button(content_frame, text="Nova compra", command=lambda: show_nova_compra(content_frame), width=20, height=2)
    btn_nova_compra.pack(pady=10)

    # Sub-opções para nova compra
    btn_alterar_compra = tk.Button(content_frame, text="Alterar compra", command=lambda: show_alterar_compra(content_frame), width=20, height=2)
    btn_alterar_compra.pack(pady=10)

    # Botão para voltar ao menu principal
    btn_voltar = tk.Button(content_frame, text="Voltar", command=lambda: show_main_menu(content_frame.master), width=20, height=2)
    btn_voltar.pack(pady=10)

def show_alterar_compra(content_frame):
    clear_frame(content_frame)

    label_title = tk.Label(content_frame, text="Alterar Compra", font=("Arial", 16, "bold"))
    label_title.pack(pady=10)

    label_id_entrada= tk.Label(content_frame, text="ID da compra:")
    label_id_entrada.pack(pady=5)
    entry_id_entrada = tk.Entry(content_frame, width=40)
    entry_id_entrada.pack(pady=5)    

    edicao_frame_existente = None
    specific_compra5_frame = None
    specific_compra6_frame = None

    def buscar_dados_id_bd(ID):
        conn = conectar_bd()
        rel_compra_id = []
        if conn:
            cursor = conn.cursor()
            try:
                cursor.execute("SELECT RGA.ID, RGA.DATA_GASTO, RGA.VALOR_GASTO, TGA.NOME_TIPO_GASTO, LGA.NOME_LOCAL_GASTO, TPA.NOME_TIPO_PAGAMENTO, USU.NOME_USUARIO_PAGOU, MPA.NOME_METODO_PAGAMENTO, CAR.NOME_CARTAO, RGA.OBSERVACOES " \
                               "FROM T_REGISTROS_GASTO RGA " \
                               "INNER JOIN T_TIPO_GASTO TGA ON RGA.ID_TIPO_GASTO = TGA.ID_TIPO_GASTO " \
                               "INNER JOIN T_LOCAL_GASTO LGA ON RGA.ID_LOCAL_GASTO = LGA.ID_LOCAL_GASTO " \
                               "INNER JOIN T_TIPO_PAGAMENTO TPA ON RGA.ID_TIPO_PAGAMENTO = TPA.ID_TIPO_PAGAMENTO " \
                               "INNER JOIN T_USUARIO_PAGOU USU ON RGA.ID_USUARIO_PAGOU = USU.ID_USUARIO_PAGOU " \
                               "INNER JOIN T_METODO_PAGAMENTO MPA ON RGA.ID_METODO_PAGAMENTO = MPA.ID_METODO_PAGAMENTO " \
                               "INNER JOIN T_CARTAO CAR ON RGA.ID_CARTAO = CAR.ID_CARTAO " \
                               "WHERE RGA.ID = (?);", (ID))
                for row in cursor.fetchall():
                    rel_compra_id.append(row) 
            except pyodbc.Error as ex:
                sqlstate = ex.args[0]
                messagebox.showerror("Erro ao Carregar a compra pelo ID", f"Não foi possível carregar a compra!.\nErro: {sqlstate}")
            finally:
                conn.close()
        return rel_compra_id

    def on_buscar_dados_id():

        nonlocal edicao_frame_existente
        nonlocal specific_compra5_frame
        nonlocal specific_compra6_frame

        if edicao_frame_existente and edicao_frame_existente.winfo_exists():
            edicao_frame_existente.destroy()

        if specific_compra5_frame and specific_compra5_frame.winfo_exists():
            specific_compra5_frame.destroy()
        
        if specific_compra6_frame and specific_compra6_frame.winfo_exists():
            specific_compra6_frame.destroy()

        id_digitado = entry_id_entrada.get()
        id_inteiro = 0

        try:
            id_inteiro = int(id_digitado)
            retorno_compra = buscar_dados_id_bd(id_inteiro)
            dados = retorno_compra[0]
            id_retorno = tk.StringVar()
            id_retorno.set(dados[0])

            edicao_frame_existente = tk.Frame(content_frame)
            edicao_frame_existente.pack(pady=25, padx=50, anchor="n")

            data_retorno = dados[1]

            valor_retorno = tk.StringVar()
            valor_retorno.set(dados[2])

            tipo_gasto_retorno = tk.StringVar()
            tipo_gasto_retorno.set(dados[3])

            local_gasto_retorno = tk.StringVar()
            local_gasto_retorno.set(dados[4])

            tipo_pagamento_retorno = tk.StringVar()
            tipo_pagamento_retorno.set(dados[5])
            
            usuario_pagou_retorno = tk.StringVar()
            usuario_pagou_retorno.set(dados[6])

            metodo_pagamento_retorno = tk.StringVar()
            metodo_pagamento_retorno.set(dados[7])

            cartao_retorno = tk.StringVar()
            cartao_retorno.set(dados[8])

            observacao_retorno = tk.StringVar()
            observacao_retorno.set(dados[9])

            specific_tela_total_frame = tk.Frame(edicao_frame_existente)
            specific_tela_total_frame.pack(pady=5, padx=50, anchor="n") 

            specific_compra1_frame = tk.Frame(specific_tela_total_frame)
            specific_compra1_frame.pack(pady=5, padx=50, side="left") 

            specific_compra2_frame = tk.Frame(specific_tela_total_frame)
            specific_compra2_frame.pack(pady=5, padx=50, side="left") 

            specific_compra3_frame = tk.Frame(specific_tela_total_frame)
            specific_compra3_frame.pack(pady=5, padx=50, side="left") 

            specific_compra4_frame = tk.Frame(specific_tela_total_frame)
            specific_compra4_frame.pack(pady=5, padx=50, side="left") 

            specific_compra6_frame = tk.Frame(content_frame)
            specific_compra6_frame.pack(pady=5, padx=50, side="top") 

            # --- Seleção de Usuário ---
            label_usuario = tk.Label(specific_compra1_frame, text="Usuário:")
            label_usuario.pack(pady=5)
            # Carrega os usuários do banco de dados
            usuarios_data = get_usuarios_db() # Lista de (ID, NOME)
            # Cria uma lista apenas com os nomes para o Combobox
            usuarios_nomes = [user[1] for user in usuarios_data]    
            # Variável para armazenar o nome selecionado no Combobox
            selected_usuario_name = tk.StringVar()    
            # Combobox para selecionar o usuário
            combobox_usuario = ttk.Combobox(specific_compra1_frame, textvariable=selected_usuario_name, values=usuarios_nomes, state="readonly")
            combobox_usuario.pack(pady=5)
            combobox_usuario.set(usuario_pagou_retorno.get()) # Texto padrão

            # --- Seleção do tipo de gasto ---
            label_tipo_gasto = tk.Label(specific_compra1_frame, text="Tipo de gasto:")
            label_tipo_gasto.pack(pady=5)
            # Carrega os tipos de gasto do banco de dados
            tipo_gasto_data = get_tipo_gasto_db()
            # Cria uma lista apenas com os nomes para o Combobox
            tipo_gasto_nomes = [item[1] for item in tipo_gasto_data]
            # Variável para armazenar o nome selecionado no Combobox
            selected_tipo_gasto_nome = tk.StringVar()
            # Combobox para selecionar o tipo de gasto
            combobox_tipo_gasto = ttk.Combobox(specific_compra1_frame, textvariable=selected_tipo_gasto_nome, values=tipo_gasto_nomes, state="readonly")
            combobox_tipo_gasto.pack(pady=5)
            combobox_tipo_gasto.set(tipo_gasto_retorno.get()) # Texto padrão

            # --- Seleção do local de gasto ---
            label_local_gasto = tk.Label(specific_compra2_frame, text="Local:")
            label_local_gasto.pack(pady=5,)
            # Carrega os locais de gasto do banco de dados
            local_gasto_data = get_local_gasto_db()
            # Cria uma lista apenas com os nomes para o Combobox
            local_gasto_nomes = [local[1] for local in local_gasto_data]
            # Variável para armazenar o nome selecionado no Combobox
            selected_local_gasto_nome = tk.StringVar()
            # Combobox para selecionar o local de gasto
            combobox_local_gasto = ttk.Combobox(specific_compra2_frame, textvariable=selected_local_gasto_nome, values=local_gasto_nomes, state="readonly")
            combobox_local_gasto.pack(pady=5)
            combobox_local_gasto.set(local_gasto_retorno.get()) # Texto padrão

            # --- Seleção do tipo de gasto ---
            label_tipo_pagamento = tk.Label(specific_compra2_frame, text="Tipo de pagamento:")
            label_tipo_pagamento.pack(pady=5)
            # Carrega os tipos de pagamento do banco de dados
            tipo_pagamento_data = get_tipo_pagamento_db()
            # Cria uma lista apenas com os nomes para o Combobox
            tipo_pagamento_nomes = [pay[1] for pay in tipo_pagamento_data]
            # Variável para armazenar o nome selecionado no Combobox
            selected_tipo_pagamento_nome = tk.StringVar()
            # Combobox para selecionar o tipo de pagamento
            combobox_tipo_pagamento = ttk.Combobox(specific_compra2_frame, textvariable=selected_tipo_pagamento_nome, values=tipo_pagamento_nomes, state="readonly")
            combobox_tipo_pagamento.pack(pady=5)
            combobox_tipo_pagamento.set(tipo_pagamento_retorno.get()) # Texto padrão

            # --- Seleção do tipo de gasto ---
            label_metodo_pagamento = tk.Label(specific_compra3_frame, text="Metodo de pagamento:")
            label_metodo_pagamento.pack(pady=5)
            # Carrega os metodos de pagamento do banco de dados
            metodo_pagamento_data = get_metodo_pagamento_db()
            # Cria uma lista apenas com os nomes para o Combobox
            metodo_pagamento_nomes = [met_pay[1] for met_pay in metodo_pagamento_data]
            # Variável para armazenar o nome selecionado no Combobox
            selected_metodo_pagamento_nome = tk.StringVar()
            # Combobox para selecionar o metodo de pagamento
            combobox_metodo_pagamento = ttk.Combobox(specific_compra3_frame, textvariable=selected_metodo_pagamento_nome, values=metodo_pagamento_nomes, state="readonly")
            combobox_metodo_pagamento.pack(pady=5)
            combobox_metodo_pagamento.set(metodo_pagamento_retorno.get()) # Texto padrão

            # --- Seleção do tipo de gasto ---
            label_cartao = tk.Label(specific_compra3_frame, text="Cartão:")
            label_cartao.pack(pady=5)
            # Carrega os cartões do banco de dados
            cartao_data = get_cartao_db()
            # Cria uma lista apenas com os nomes para o Combobox
            cartao_nomes = [card[1] for card in cartao_data]
            # Variável para armazenar o nome selecionado no Combobox
            selected_cartao_nome = tk.StringVar()
            # Combobox para selecionar o cartão
            combobox_cartao = ttk.Combobox(specific_compra3_frame, textvariable=selected_cartao_nome, values=cartao_nomes, state="readonly")
            combobox_cartao.pack(pady=5)
            combobox_cartao.set(cartao_retorno.get()) # Texto padrão

            # --- Entrada de Valor ---
            label_valor = tk.Label(specific_compra4_frame, text="Valor:")
            label_valor.pack(pady=5)
            entry_valor = tk.Entry(specific_compra4_frame, width=40, textvariable=valor_retorno)
            entry_valor.pack(pady=5)

            # --- Entrada de Descrição ---
            label_descricao = tk.Label(specific_compra4_frame, text="Descrição:")
            label_descricao.pack(pady=5)
            entry_descricao = tk.Entry(specific_compra4_frame, width=40, textvariable=observacao_retorno)
            entry_descricao.pack(pady=5)

            # --- Calendário para Data da Compra ---
            label_data = tk.Label(specific_compra6_frame, text="Data:")
            label_data.pack(pady=5)
            
            # Cria o widget de calendário
            data = Calendar(specific_compra6_frame, selectmode='day', date_pattern='dd/mm/yyyy') # Define o formato de exibição
            data.pack(pady=5)

            data.selection_set(data_retorno)

            def on_alterar_compra():
                #Função interna para lidar com o clique do botão "Alterar Compra".
                nome_selecionado = selected_usuario_name.get()
                valor_str = entry_valor.get()
                descricao = entry_descricao.get()
                tipo_gasto_selecionado = selected_tipo_gasto_nome.get()
                local_gasto_selecionado = selected_local_gasto_nome.get()
                tipo_pagamento_selecionado = selected_tipo_pagamento_nome.get()
                metodo_pagamento_selecionado = selected_metodo_pagamento_nome.get()
                cartao_selecionado = selected_cartao_nome.get()
                data_str = data.get_date()

                if nome_selecionado == "Selecione":
                    messagebox.showwarning("Seleção Inválida", "Por favor, selecione um usuário.")
                    return
                if tipo_gasto_selecionado == "Selecione":
                    messagebox.showwarning("Seleção Inválida", "Por favor, selecione um tipo de gasto.")
                    return
                if local_gasto_selecionado == "Selecione":
                    messagebox.showwarning("Seleção Inválida", "Por favor, selecione um local de compra.")
                    return
                if tipo_pagamento_selecionado == "Selecione":
                    messagebox.showwarning("Seleção Inválida", "Por favor, selecione um tipo de pagamento.")
                    return
                if metodo_pagamento_selecionado == "Selecione":
                    messagebox.showwarning("Seleção Inválida", "Por favor, selecione um metodo de pagamento.")
                    return
                if cartao_selecionado == "Selecione":
                    messagebox.showwarning("Seleção Inválida", "Por favor, selecione um cartão.")
                    return
                if not valor_str:
                    messagebox.showwarning("Campo Vazio", "Por favor, insira o valor da compra.")
                    return
                if not data_str:
                    messagebox.showwarning("Campo Vazio", "Por favor, insira a data da compra.")
                    return 
                
                try:
                    valor_float = float(valor_str.replace(',', '.')) # Permite vírgula como separador decimal
                except ValueError:
                    messagebox.showwarning("Valor Inválido", "Por favor, digite um número válido para o valor.")
                    return
                
                try:
                    # Tenta converter a string da data para um objeto datetime
                    data_compra_obj = datetime.datetime.strptime(data_str, "%d/%m/%Y").date() # .date() para pegar apenas a data
                except ValueError:
                    messagebox.showwarning("Data Inválida", "Formato de data incorreto. Use DD/MM/AAAA.")
                    return

                # Encontra o ID do usuário selecionado
                id_usuario_selecionado = None
                for user_id, user_name in usuarios_data:
                    if user_name == nome_selecionado:
                        id_usuario_selecionado = user_id
                        break
                
                if id_usuario_selecionado is None:
                    messagebox.showerror("Erro Interno", "Não foi possível encontrar o ID do usuário selecionado.")
                    return
                
                # Encontra o ID do tipo de gasto selecionado
                id_tipo_gasto_selecionado = None
                for tipo_gasto_id, tipo_gasto_name in tipo_gasto_data:
                    if tipo_gasto_name == tipo_gasto_selecionado:
                        id_tipo_gasto_selecionado = tipo_gasto_id
                        break

                if id_tipo_gasto_selecionado is None:
                    messagebox.showerror("Erro Interno", "Não foi possível encontrar o tipo de gasto selecionado.")
                    return
                
                # Encontra o ID do local de gasto selecionado
                id_local_gasto_selecionado = None
                for local_gasto_id, local_gasto_name in local_gasto_data:
                    if local_gasto_name == local_gasto_selecionado:
                        id_local_gasto_selecionado = local_gasto_id
                        break

                if id_local_gasto_selecionado is None:
                    messagebox.showerror("Erro Interno", "Não foi possível encontrar o local da compra selecionado.")
                    return
                
                # Encontra o ID do tipo de pagamento selecionado
                id_tipo_pagamento_selecionado = None
                for tipo_pagamento_id, tipo_pagamento_name in tipo_pagamento_data:
                    if tipo_pagamento_name == tipo_pagamento_selecionado:
                        id_tipo_pagamento_selecionado = tipo_pagamento_id
                        break

                if id_tipo_pagamento_selecionado is None:
                    messagebox.showerror("Erro Interno", "Não foi possível encontrar o tipo de pagamento selecionado.")
                    return
                
                # Encontra o ID do metodo de pagamento selecionado
                id_metodo_pagamento_selecionado = None
                for metodo_pagamento_id, metodo_pagamento_name in metodo_pagamento_data:
                    if metodo_pagamento_name == metodo_pagamento_selecionado:
                        id_metodo_pagamento_selecionado = metodo_pagamento_id
                        break

                if id_metodo_pagamento_selecionado is None:
                    messagebox.showerror("Erro Interno", "Não foi possível encontrar o metodo de pagamento selecionado.")
                    return
                
                # Encontra o ID cartão selecionado
                id_cartao_selecionado = None
                for cartao_id, cartao_name in cartao_data:
                    if cartao_name == cartao_selecionado:
                        id_cartao_selecionado = cartao_id
                        break

                if id_cartao_selecionado is None:
                    messagebox.showerror("Erro Interno", "Não foi possível encontrar o cartão selecionado.")
                    return
                
                # Salva a compra no banco de dados
                if alterar_compra_db(data_compra_obj, valor_float, id_tipo_gasto_selecionado, id_local_gasto_selecionado, id_tipo_pagamento_selecionado, id_usuario_selecionado, id_metodo_pagamento_selecionado, descricao, id_cartao_selecionado, id_inteiro):
                    # Limpa os campos após o sucesso
                    selected_usuario_name.set(usuario_pagou_retorno.get())
                    selected_tipo_gasto_nome.set(tipo_gasto_retorno.get())
                    selected_local_gasto_nome.set(local_gasto_retorno.get())
                    selected_tipo_pagamento_nome.set(tipo_pagamento_retorno.get())
                    selected_metodo_pagamento_nome.set(metodo_pagamento_retorno.get())
                    selected_cartao_nome.set(cartao_retorno.get())
                    entry_valor.delete(0, tk.END)
                    entry_descricao.delete(0, tk.END)
                    if edicao_frame_existente:
                        edicao_frame_existente.destroy()
                        specific_compra6_frame.destroy()
                        specific_compra5_frame.destroy()

            def on_deletar_compra():
                if deletar_compra_db(id_inteiro):
                    # Limpa os campos após o sucesso
                    selected_usuario_name.set(usuario_pagou_retorno.get())
                    selected_tipo_gasto_nome.set(tipo_gasto_retorno.get())
                    selected_local_gasto_nome.set(local_gasto_retorno.get())
                    selected_tipo_pagamento_nome.set(tipo_pagamento_retorno.get())
                    selected_metodo_pagamento_nome.set(metodo_pagamento_retorno.get())
                    selected_cartao_nome.set(cartao_retorno.get())
                    entry_valor.delete(0, tk.END)
                    entry_descricao.delete(0, tk.END)
                    if edicao_frame_existente:
                        edicao_frame_existente.destroy()
                        specific_compra6_frame.destroy()
                        specific_compra5_frame.destroy()

            specific_compra5_frame = tk.Frame(content_frame)
            specific_compra5_frame.pack(padx=50) 

            # Botão para alterar
            btn_alterar = tk.Button(specific_compra5_frame, text="Alterar", command=on_alterar_compra, width=25, height=2)
            btn_alterar.pack(pady=10, padx=10, side="left")
            # botão para deletar
            btn_deletar = tk.Button(specific_compra5_frame, text="Deletar", command=on_deletar_compra, width=25, height=2)
            btn_deletar.pack(pady=10, padx=10, side="left")
   
        except ValueError:
            messagebox.showwarning("ID inválido", "Por favor, digite um número inteiro válido.")
        except IndexError:
            messagebox.showwarning("ID não encontrado", "Nenhuma compra encontrada com o ID informado.")

    botoes_frame = tk.Frame(content_frame)
    botoes_frame.pack(pady=10)    

    btn_buscar_alteracao = tk.Button(botoes_frame, text="Buscar", command=on_buscar_dados_id, width=20, height=2)
    btn_buscar_alteracao.pack(side='left', padx=5)

    # Botão para voltar ao menu de compras
    btn_voltar = tk.Button(botoes_frame, text="Voltar", command=lambda: show_compras_screen(content_frame), width=20, height=2)
    btn_voltar.pack(side='left', padx=5)

def show_nova_compra(content_frame):
    #Exibe a tela para registrar uma nova compra.
    clear_frame(content_frame)

    label_title = tk.Label(content_frame, text="Registrar Nova Compra", font=("Arial", 16, "bold"))
    label_title.pack(pady=10)

    specific_tela_total_frame = tk.Frame(content_frame)
    specific_tela_total_frame.pack(pady=25, padx=50, anchor="n") 

    specific_compra1_frame = tk.Frame(specific_tela_total_frame)
    specific_compra1_frame.pack(pady=25, padx=50, side="left") 

    specific_compra2_frame = tk.Frame(specific_tela_total_frame)
    specific_compra2_frame.pack(pady=25, padx=50, side="left") 

    specific_compra3_frame = tk.Frame(specific_tela_total_frame)
    specific_compra3_frame.pack(pady=25, padx=50, side="left") 

    specific_compra4_frame = tk.Frame(specific_tela_total_frame)
    specific_compra4_frame.pack(pady=25, padx=50, side="left") 

    specific_compra6_frame = tk.Frame(content_frame)
    specific_compra6_frame.pack(pady=25, padx=50, side="top") 

    # --- Seleção de Usuário ---
    label_usuario = tk.Label(specific_compra1_frame, text="Usuário:")
    label_usuario.pack(pady=5)
    # Carrega os usuários do banco de dados
    usuarios_data = get_usuarios_db() # Lista de (ID, NOME)
    # Cria uma lista apenas com os nomes para o Combobox
    usuarios_nomes = [user[1] for user in usuarios_data]    
    # Variável para armazenar o nome selecionado no Combobox
    selected_usuario_name = tk.StringVar()    
    # Combobox para selecionar o usuário
    combobox_usuario = ttk.Combobox(specific_compra1_frame, textvariable=selected_usuario_name, values=usuarios_nomes, state="readonly")
    combobox_usuario.pack(pady=5)
    combobox_usuario.set("Selecione") # Texto padrão

    # --- Seleção do tipo de gasto ---
    label_tipo_gasto = tk.Label(specific_compra1_frame, text="Tipo de gasto:")
    label_tipo_gasto.pack(pady=5)
    # Carrega os tipos de gasto do banco de dados
    tipo_gasto_data = get_tipo_gasto_db()
    # Cria uma lista apenas com os nomes para o Combobox
    tipo_gasto_nomes = [item[1] for item in tipo_gasto_data]
    # Variável para armazenar o nome selecionado no Combobox
    selected_tipo_gasto_nome = tk.StringVar()
    # Combobox para selecionar o tipo de gasto
    combobox_tipo_gasto = ttk.Combobox(specific_compra1_frame, textvariable=selected_tipo_gasto_nome, values=tipo_gasto_nomes, state="readonly")
    combobox_tipo_gasto.pack(pady=5)
    combobox_tipo_gasto.set("Selecione") # Texto padrão

    # --- Seleção do local de gasto ---
    label_local_gasto = tk.Label(specific_compra2_frame, text="Local:")
    label_local_gasto.pack(pady=5,)
    # Carrega os locais de gasto do banco de dados
    local_gasto_data = get_local_gasto_db()
    # Cria uma lista apenas com os nomes para o Combobox
    local_gasto_nomes = [local[1] for local in local_gasto_data]
    # Variável para armazenar o nome selecionado no Combobox
    selected_local_gasto_nome = tk.StringVar()
    # Combobox para selecionar o local de gasto
    combobox_local_gasto = ttk.Combobox(specific_compra2_frame, textvariable=selected_local_gasto_nome, values=local_gasto_nomes, state="readonly")
    combobox_local_gasto.pack(pady=5)
    combobox_local_gasto.set("Selecione") # Texto padrão

    # --- Seleção do tipo de gasto ---
    label_tipo_pagamento = tk.Label(specific_compra2_frame, text="Tipo de pagamento:")
    label_tipo_pagamento.pack(pady=5)
    # Carrega os tipos de pagamento do banco de dados
    tipo_pagamento_data = get_tipo_pagamento_db()
    # Cria uma lista apenas com os nomes para o Combobox
    tipo_pagamento_nomes = [pay[1] for pay in tipo_pagamento_data]
    # Variável para armazenar o nome selecionado no Combobox
    selected_tipo_pagamento_nome = tk.StringVar()
    # Combobox para selecionar o tipo de pagamento
    combobox_tipo_pagamento = ttk.Combobox(specific_compra2_frame, textvariable=selected_tipo_pagamento_nome, values=tipo_pagamento_nomes, state="readonly")
    combobox_tipo_pagamento.pack(pady=5)
    combobox_tipo_pagamento.set("Selecione") # Texto padrão

    # --- Seleção do tipo de gasto ---
    label_metodo_pagamento = tk.Label(specific_compra3_frame, text="Metodo de pagamento:")
    label_metodo_pagamento.pack(pady=5)
    # Carrega os metodos de pagamento do banco de dados
    metodo_pagamento_data = get_metodo_pagamento_db()
    # Cria uma lista apenas com os nomes para o Combobox
    metodo_pagamento_nomes = [met_pay[1] for met_pay in metodo_pagamento_data]
    # Variável para armazenar o nome selecionado no Combobox
    selected_metodo_pagamento_nome = tk.StringVar()
    # Combobox para selecionar o metodo de pagamento
    combobox_metodo_pagamento = ttk.Combobox(specific_compra3_frame, textvariable=selected_metodo_pagamento_nome, values=metodo_pagamento_nomes, state="readonly")
    combobox_metodo_pagamento.pack(pady=5)
    combobox_metodo_pagamento.set("Selecione") # Texto padrão

    # --- Seleção do tipo de gasto ---
    label_cartao = tk.Label(specific_compra3_frame, text="Cartão:")
    label_cartao.pack(pady=5)
    # Carrega os cartões do banco de dados
    cartao_data = get_cartao_db()
    # Cria uma lista apenas com os nomes para o Combobox
    cartao_nomes = [card[1] for card in cartao_data]
    # Variável para armazenar o nome selecionado no Combobox
    selected_cartao_nome = tk.StringVar()
    # Combobox para selecionar o cartão
    combobox_cartao = ttk.Combobox(specific_compra3_frame, textvariable=selected_cartao_nome, values=cartao_nomes, state="readonly")
    combobox_cartao.pack(pady=5)
    combobox_cartao.set("Selecione") # Texto padrão

    # --- Entrada de Valor ---
    label_valor = tk.Label(specific_compra4_frame, text="Valor:")
    label_valor.pack(pady=5)
    entry_valor = tk.Entry(specific_compra4_frame, width=40)
    entry_valor.pack(pady=5)

    # --- Entrada de Descrição ---
    label_descricao = tk.Label(specific_compra4_frame, text="Descrição:")
    label_descricao.pack(pady=5)
    entry_descricao = tk.Entry(specific_compra4_frame, width=40)
    entry_descricao.pack(pady=5)

    # --- Calendário para Data da Compra ---
    label_data = tk.Label(specific_compra6_frame, text="Data:")
    label_data.pack(pady=5)
    
    # Cria o widget de calendário
    data = Calendar(specific_compra6_frame, selectmode='day',
                   year=datetime.datetime.now().year, month=datetime.datetime.now().month,
                   day=datetime.datetime.now().day,
                   date_pattern='dd/mm/yyyy') # Define o formato de exibição
    data.pack(pady=5)

    def on_salvar_compra():
        #Função interna para lidar com o clique do botão "Salvar Compra".
        nome_selecionado = selected_usuario_name.get()
        valor_str = entry_valor.get()
        descricao = entry_descricao.get()
        tipo_gasto_selecionado = selected_tipo_gasto_nome.get()
        local_gasto_selecionado = selected_local_gasto_nome.get()
        tipo_pagamento_selecionado = selected_tipo_pagamento_nome.get()
        metodo_pagamento_selecionado = selected_metodo_pagamento_nome.get()
        cartao_selecionado = selected_cartao_nome.get()
        data_str = data.get_date()

        if nome_selecionado == "Selecione":
            messagebox.showwarning("Seleção Inválida", "Por favor, selecione um usuário.")
            return
        if tipo_gasto_selecionado == "Selecione":
            messagebox.showwarning("Seleção Inválida", "Por favor, selecione um tipo de gasto.")
            return
        if local_gasto_selecionado == "Selecione":
            messagebox.showwarning("Seleção Inválida", "Por favor, selecione um local de compra.")
            return
        if tipo_pagamento_selecionado == "Selecione":
            messagebox.showwarning("Seleção Inválida", "Por favor, selecione um tipo de pagamento.")
            return
        if metodo_pagamento_selecionado == "Selecione":
            messagebox.showwarning("Seleção Inválida", "Por favor, selecione um metodo de pagamento.")
            return
        if cartao_selecionado == "Selecione":
            messagebox.showwarning("Seleção Inválida", "Por favor, selecione um cartão.")
            return
        if not valor_str:
            messagebox.showwarning("Campo Vazio", "Por favor, insira o valor da compra.")
            return
        if not data_str:
            messagebox.showwarning("Campo Vazio", "Por favor, insira a data da compra.")
            return 
        
        try:
            valor_float = float(valor_str.replace(',', '.')) # Permite vírgula como separador decimal
        except ValueError:
            messagebox.showwarning("Valor Inválido", "Por favor, digite um número válido para o valor.")
            return
        
        try:
            # Tenta converter a string da data para um objeto datetime
            data_compra_obj = datetime.datetime.strptime(data_str, "%d/%m/%Y").date() # .date() para pegar apenas a data
        except ValueError:
            messagebox.showwarning("Data Inválida", "Formato de data incorreto. Use DD/MM/AAAA.")
            return

        # Encontra o ID do usuário selecionado
        id_usuario_selecionado = None
        for user_id, user_name in usuarios_data:
            if user_name == nome_selecionado:
                id_usuario_selecionado = user_id
                break
        
        if id_usuario_selecionado is None:
            messagebox.showerror("Erro Interno", "Não foi possível encontrar o ID do usuário selecionado.")
            return
        
        # Encontra o ID do tipo de gasto selecionado
        id_tipo_gasto_selecionado = None
        for tipo_gasto_id, tipo_gasto_name in tipo_gasto_data:
            if tipo_gasto_name == tipo_gasto_selecionado:
                id_tipo_gasto_selecionado = tipo_gasto_id
                break

        if id_tipo_gasto_selecionado is None:
            messagebox.showerror("Erro Interno", "Não foi possível encontrar o tipo de gasto selecionado.")
            return
        
        # Encontra o ID do local de gasto selecionado
        id_local_gasto_selecionado = None
        for local_gasto_id, local_gasto_name in local_gasto_data:
            if local_gasto_name == local_gasto_selecionado:
                id_local_gasto_selecionado = local_gasto_id
                break

        if id_local_gasto_selecionado is None:
            messagebox.showerror("Erro Interno", "Não foi possível encontrar o local da compra selecionado.")
            return
        
        # Encontra o ID do tipo de pagamento selecionado
        id_tipo_pagamento_selecionado = None
        for tipo_pagamento_id, tipo_pagamento_name in tipo_pagamento_data:
            if tipo_pagamento_name == tipo_pagamento_selecionado:
                id_tipo_pagamento_selecionado = tipo_pagamento_id
                break

        if id_tipo_pagamento_selecionado is None:
            messagebox.showerror("Erro Interno", "Não foi possível encontrar o tipo de pagamento selecionado.")
            return
        
        # Encontra o ID do metodo de pagamento selecionado
        id_metodo_pagamento_selecionado = None
        for metodo_pagamento_id, metodo_pagamento_name in metodo_pagamento_data:
            if metodo_pagamento_name == metodo_pagamento_selecionado:
                id_metodo_pagamento_selecionado = metodo_pagamento_id
                break

        if id_metodo_pagamento_selecionado is None:
            messagebox.showerror("Erro Interno", "Não foi possível encontrar o metodo de pagamento selecionado.")
            return
        
        # Encontra o ID cartão selecionado
        id_cartao_selecionado = None
        for cartao_id, cartao_name in cartao_data:
            if cartao_name == cartao_selecionado:
                id_cartao_selecionado = cartao_id
                break

        if id_cartao_selecionado is None:
            messagebox.showerror("Erro Interno", "Não foi possível encontrar o cartão selecionado.")
            return
        
        # Salva a compra no banco de dados
        if salvar_nova_compra_db(data_compra_obj, valor_float, id_tipo_gasto_selecionado, id_local_gasto_selecionado, id_tipo_pagamento_selecionado, id_usuario_selecionado, id_metodo_pagamento_selecionado, descricao, id_cartao_selecionado,):
            # Limpa os campos após o sucesso
            selected_usuario_name.set("Selecione")
            selected_tipo_gasto_nome.set("Selecione")
            selected_local_gasto_nome.set("Selecione")
            selected_tipo_pagamento_nome.set("Selecione")
            selected_metodo_pagamento_nome.set("Selecione")
            selected_cartao_nome.set("Selecione")
            entry_valor.delete(0, tk.END)
            entry_descricao.delete(0, tk.END)

    specific_compra5_frame = tk.Frame(content_frame)
    specific_compra5_frame.pack(pady=5, padx=50) 

    # Botão para salvar
    btn_salvar = tk.Button(specific_compra5_frame, text="Salvar", command=on_salvar_compra, width=25, height=2)
    btn_salvar.pack(pady=10, padx=10, side="left")
    # Botão para voltar ao menu de compras
    btn_voltar = tk.Button(specific_compra5_frame, text="Voltar", command=lambda: show_compras_screen(content_frame), width=25, height=2)
    btn_voltar.pack(pady=10, padx=10, side="left")
   
def show_cadastros_screen(content_frame):
    #Exibe a tela do menu 'Configurações'.
    clear_frame(content_frame)
    label_title = tk.Label(content_frame, text="Cadastros", font=("Arial", 16, "bold"))
    label_title.pack(pady=20)

    # Sub-opções para cadastro de usuário
    btn_cadastro_usuario = tk.Button(content_frame, text="Usuário", command=lambda: show_cadastrar_usuario(content_frame), width=25, height=2)
    btn_cadastro_usuario.pack(pady=5)

    # Sub-opções para cadastro de tipo de gasto
    btn_cadastro_tipo_gasto = tk.Button(content_frame, text="Tipo de gasto", command=lambda: show_cadastrar_tipo_gasto(content_frame), width=25, height=2)
    btn_cadastro_tipo_gasto.pack(pady=5)

    # Sub-opções para cadastro de local de gasto
    btn_cadastro_local_gasto = tk.Button(content_frame, text="Local", command=lambda: show_cadastrar_local_gasto(content_frame), width=25, height=2)
    btn_cadastro_local_gasto.pack(pady=5)

    # Sub-opções para cadastro de tipo de pagamento
    btn_cadastro_tipo_pagamento = tk.Button(content_frame, text="Tipo de pagamento", command=lambda: show_cadastrar_tipo_pagamento(content_frame), width=25, height=2)
    btn_cadastro_tipo_pagamento.pack(pady=5)

    # Sub-opções para cadastro de metodo de pagamento
    btn_cadastro_metodo_pagamento = tk.Button(content_frame, text="Metodo de pagamento", command=lambda: show_cadastrar_metodo_pagamento(content_frame), width=25, height=2)
    btn_cadastro_metodo_pagamento.pack(pady=5)

    # Sub-opções para cadastro de cartão
    btn_cadastro_cartao = tk.Button(content_frame, text="Cartão", command=lambda: show_cadastrar_cartao(content_frame), width=25, height=2)
    btn_cadastro_cartao.pack(pady=5)

    # Botão para voltar ao menu principal
    btn_voltar = tk.Button(content_frame, text="Voltar", command=lambda: show_main_menu(content_frame.master), width=25, height=2)
    btn_voltar.pack(pady=25)

def show_cadastrar_usuario(content_frame):
    #Exibe o formulário para registrar um novo usuário que pagou sub-opção de Configurações.
    clear_frame(content_frame) # Limpa o frame para o formulário

    label_title = tk.Label(content_frame, text="Cadastrar Usuário", font=("Arial", 14, "bold"))
    label_title.pack(pady=10)
    # Dados de entrada do usuário
    label_nome = tk.Label(content_frame, text="Nome:")
    label_nome.pack(pady=5)
    entry_nome = tk.Entry(content_frame, width=40)
    entry_nome.pack(pady=5)

    def on_adicionar_usuario():
        #Função interna para lidar com o clique do botão "Adicionar Usuário" no formulário.
        nome = entry_nome.get()
        if not nome:
            messagebox.showwarning("Campos Vazios", "Por favor, preencha o nome do usuário.")
            return
        # Chama a função de banco de dados e limpa o campo se for sucesso
        if adicionar_usuario_pagou_db(nome):
            entry_nome.delete(0, tk.END) 

    # Botão para adicionar usuário
    btn_adicionar = tk.Button(content_frame, text="Salvar", command=on_adicionar_usuario, width=25, height=2)
    btn_adicionar.pack(pady=10)

    # Botão para voltar para a tela de Compras
    btn_voltar = tk.Button(content_frame, text="Voltar", command=lambda: show_cadastros_screen(content_frame), width=25, height=2)
    btn_voltar.pack(pady=5)

def show_cadastrar_tipo_gasto(content_frame):
    #Exibe o formulário para registrar um novo tipo de gasto sub-opção de Configurações.
    clear_frame(content_frame) # Limpa o frame para o formulário

    label_title = tk.Label(content_frame, text="Cadastrar Tipo De Gasto", font=("Arial", 14, "bold"))
    label_title.pack(pady=10)
    # Dados de entrada do tipo de gasto
    label_nome_tipo_gasto = tk.Label(content_frame, text="Tipo de gasto:")
    label_nome_tipo_gasto.pack(pady=5)
    entry_nome_tipo_gasto = tk.Entry(content_frame, width=40)
    entry_nome_tipo_gasto.pack(pady=5)

    def on_adicionar_tipo_gasto():
        #Função interna para lidar com o clique do botão "Adicionar" no formulário.
        nome_tipo_gasto = entry_nome_tipo_gasto.get()
        if not nome_tipo_gasto:
            messagebox.showwarning("Campos Vazios", "Por favor, preencha o tipo de gasto.")
            return
        # Chama a função de banco de dados e limpa o campo se for sucesso
        if adicionar_tipo_gasto(nome_tipo_gasto):
            entry_nome_tipo_gasto.delete(0, tk.END) 

    # Botão para adicionar o tipo de gasto
    btn_adicionar = tk.Button(content_frame, text="Salvar", command=on_adicionar_tipo_gasto, width=25, height=2)
    btn_adicionar.pack(pady=10)

    # Botão para voltar para a tela de Compras
    btn_voltar = tk.Button(content_frame, text="Voltar", command=lambda: show_cadastros_screen(content_frame), width=25, height=2)
    btn_voltar.pack(pady=5)

def show_cadastrar_local_gasto(content_frame):
    #Exibe o formulário para registrar um novo local de gasto sub-opção de Configurações.
    clear_frame(content_frame) # Limpa o frame para o formulário

    label_title = tk.Label(content_frame, text="Cadastrar Local De Compra", font=("Arial", 14, "bold"))
    label_title.pack(pady=10)
    # Dados de entrada do local de gasto
    label_nome_local_gasto = tk.Label(content_frame, text="Local:")
    label_nome_local_gasto.pack(pady=5)
    entry_nome_local_gasto = tk.Entry(content_frame, width=40)
    entry_nome_local_gasto.pack(pady=5)

    def on_adicionar_local_gasto():
        #Função interna para lidar com o clique do botão "Adicionar" no formulário.
        nome_local_gasto = entry_nome_local_gasto.get()
        if not nome_local_gasto:
            messagebox.showwarning("Campos Vazios", "Por favor, preencha o local de compra.")
            return
        # Chama a função de banco de dados e limpa o campo se for sucesso
        if adicionar_local_gasto(nome_local_gasto):
            entry_nome_local_gasto.delete(0, tk.END) 

    # Botão para adicionar Local de gasto
    btn_adicionar = tk.Button(content_frame, text="Salvar", command=on_adicionar_local_gasto, width=25, height=2)
    btn_adicionar.pack(pady=10)

    # Botão para voltar para a tela de Compras
    btn_voltar = tk.Button(content_frame, text="Voltar", command=lambda: show_cadastros_screen(content_frame), width=25, height=2)
    btn_voltar.pack(pady=5)

def show_cadastrar_tipo_pagamento(content_frame):
    #Exibe o formulário para registrar um novo tipo de pagamento sub-opção de Configurações.
    clear_frame(content_frame) # Limpa o frame para o formulário

    label_title = tk.Label(content_frame, text="Cadastrar Tipo De Pagamento", font=("Arial", 14, "bold"))
    label_title.pack(pady=10)
    # Dados de entrada do tipo de pagamento
    label_nome_tipo_pagamento = tk.Label(content_frame, text="Tipo de pagamento:")
    label_nome_tipo_pagamento.pack(pady=5)
    entry_nome_tipo_pagamento = tk.Entry(content_frame, width=40)
    entry_nome_tipo_pagamento.pack(pady=5)

    def on_adicionar_tipo_pagamento():
        #Função interna para lidar com o clique do botão "Adicionar" no formulário.

        nome_tipo_pagamento = entry_nome_tipo_pagamento.get()
        if not nome_tipo_pagamento:
            messagebox.showwarning("Campos Vazios", "Por favor, preencha o tipo de pagamento.")
            return
        # Chama a função de banco de dados e limpa o campo se for sucesso
        if adicionar_tipo_pagamento(nome_tipo_pagamento):
            entry_nome_tipo_pagamento.delete(0, tk.END) 

    # Botão para adicionar tipo de pagamento
    btn_adicionar = tk.Button(content_frame, text="Salvar", command=on_adicionar_tipo_pagamento, width=25, height=2)
    btn_adicionar.pack(pady=10)

    # Botão para voltar para a tela de Compras
    btn_voltar = tk.Button(content_frame, text="Voltar", command=lambda: show_cadastros_screen(content_frame), width=25, height=2)
    btn_voltar.pack(pady=5)

def show_cadastrar_metodo_pagamento(content_frame):
    #Exibe o formulário para registrar um novo metodo de pagamento sub-opção de Configurações.
    clear_frame(content_frame) # Limpa o frame para o formulário

    label_title = tk.Label(content_frame, text="Cadastrar Metodo De Pagamento", font=("Arial", 14, "bold"))
    label_title.pack(pady=10)
    # Dados de entrada do metodo de pagamento
    label_nome_metodo_pagamento = tk.Label(content_frame, text="Metodo de pagamento:")
    label_nome_metodo_pagamento.pack(pady=5)
    entry_nome_metodo_pagamento = tk.Entry(content_frame, width=40)
    entry_nome_metodo_pagamento.pack(pady=5)

    def on_adicionar_metodo_pagamento():
        #Função interna para lidar com o clique do botão "Adicionar" no formulário.
        nome_metodo_pagamento = entry_nome_metodo_pagamento.get()
        if not nome_metodo_pagamento:
            messagebox.showwarning("Campos Vazios", "Por favor, preencha o metodo de pagamento.")
            return
        # Chama a função de banco de dados e limpa o campo se for sucesso
        if adicionar_metodo_pagamento(nome_metodo_pagamento):
            entry_nome_metodo_pagamento.delete(0, tk.END) 

    # Botão adicionar metodos de pagamento
    btn_adicionar = tk.Button(content_frame, text="Salvar", command=on_adicionar_metodo_pagamento, width=25, height=2)
    btn_adicionar.pack(pady=10)

    # Botão para voltar para a tela de Compras
    btn_voltar = tk.Button(content_frame, text="Voltar", command=lambda: show_cadastros_screen(content_frame), width=25, height=2)
    btn_voltar.pack(pady=5)

def show_cadastrar_cartao(content_frame):
    #Exibe o formulário para registrar um novo cartão sub-opção de Configurações.
    clear_frame(content_frame) # Limpa o frame para o formulário

    label_title = tk.Label(content_frame, text="Cadastrar Cartão", font=("Arial", 14, "bold"))
    label_title.pack(pady=10)
    # Dados de entrada do cartão
    label_nome_cartao = tk.Label(content_frame, text="Nome:")
    label_nome_cartao.pack(pady=5)
    entry_nome_cartao = tk.Entry(content_frame, width=40)
    entry_nome_cartao.pack(pady=5)
    label_bandeira_cartao = tk.Label(content_frame, text="Bandeira:")
    label_bandeira_cartao.pack(pady=5)
    entry_bandeira_cartao = tk.Entry(content_frame, width=40)
    entry_bandeira_cartao.pack(pady=5)

    def on_adicionar_cartao():
        #Função interna para lidar com o clique do botão "Adicionar" no formulário.
        nome_cartao = entry_nome_cartao.get()
        bandeira_cartao = entry_bandeira_cartao.get()
        if not nome_cartao or not bandeira_cartao:
            messagebox.showwarning("Campos Vazios", "Por favor, preencha os dados do cartão.")
            return
        # Chama a função de banco de dados e limpa o campo se for sucesso
        if adicionar_cartao(nome_cartao, bandeira_cartao):
            entry_nome_cartao.delete(0, tk.END) 
            entry_bandeira_cartao.delete(0, tk.END) 

    # Botão adicionar cartão
    btn_adicionar = tk.Button(content_frame, text="Salvar", command=on_adicionar_cartao, width=25, height=2)
    btn_adicionar.pack(pady=10)

    # Botão para voltar para a tela de Compras
    btn_voltar = tk.Button(content_frame, text="Voltar", command=lambda: show_cadastros_screen(content_frame), width=25, height=2)
    btn_voltar.pack(pady=5)

def show_relatorios_screen(content_frame):
    #Exibe a tela do menu 'Relatórios'.
    clear_frame(content_frame)
    label_title = tk.Label(content_frame, text="Relatórios", font=("Arial", 16, "bold"))
    label_title.pack(pady=20)
    
    # Sub-opções relatório completo por data e usuário
    btn_completo_data = tk.Button(content_frame, text="Data e usuário", command=lambda: show_completo_data_usuario(content_frame), width=25, height=2)
    btn_completo_data.pack(pady=5)

    # Sub-opções relatório completo por data
    btn_completo_data = tk.Button(content_frame, text="Data", command=lambda: show_completo_data(content_frame), width=25, height=2)
    btn_completo_data.pack(pady=5)

    # Botão para voltar ao menu principal
    btn_voltar = tk.Button(content_frame, text="Voltar", command=lambda: show_main_menu(content_frame.master), width=25, height=2)
    btn_voltar.pack(pady=20)

def show_completo_data_usuario(content_frame):
    clear_frame(content_frame)

    label_title = tk.Label(content_frame, text="Relatório Por Data e Usuário", font=("Arial", 16, "bold"))
    label_title.pack(pady=10)

    specific_dat_frame = tk.Frame(content_frame)
    specific_dat_frame.pack(pady=5, anchor='w', padx=50) 

    # --- Seleção de Usuário ---
    label_usuario = tk.Label(specific_dat_frame, text="Usuário:")
    label_usuario.pack(pady=5, side="left", padx=10)
    usuarios_data = get_usuarios_db()
    usuarios_nomes = [user[1] for user in usuarios_data]
    selected_usuario_name = tk.StringVar()
    combobox_usuario = ttk.Combobox(specific_dat_frame, textvariable=selected_usuario_name, values=usuarios_nomes, state="readonly")
    combobox_usuario.pack(pady=5, side="left", padx=10)
    combobox_usuario.set("Selecione")

    # --- Entrada de Data da Compra (Manual) ---
    label_data_inicio = tk.Label(specific_dat_frame, text="Data início:")
    label_data_inicio.pack(pady=5, side="left", padx=10)
    entry_data_inicio = tk.Entry(specific_dat_frame, width=40)
    entry_data_inicio.pack(pady=5, side="left", padx=10)
    entry_data_inicio.insert(0, datetime.datetime.now().strftime("%d/%m/%Y"))

    label_data_fim = tk.Label(specific_dat_frame, text="Data fim:")
    label_data_fim.pack(pady=5, side="left", padx=10)
    entry_data_fim = tk.Entry(specific_dat_frame, width=40)
    entry_data_fim.pack(pady=5, side="left", padx=10)
    entry_data_fim.insert(0, datetime.datetime.now().strftime("%d/%m/%Y"))

    specific_value_frame = tk.Frame(content_frame)
    specific_value_frame.pack(pady=5, anchor='w', padx=50) 

    # --- Seleção do tipo de gasto ---
    label_tipo_gasto = tk.Label(specific_value_frame, text="Total gasto 01:")
    label_tipo_gasto.pack(pady=5, side="left", padx=10)
    # Carrega os tipos de gasto do banco de dados
    tipo_gasto_data = get_tipo_gasto_db()
    # Cria uma lista apenas com os nomes para o Combobox
    tipo_gasto_nomes = [item[1] for item in tipo_gasto_data]
    # Variável para armazenar o nome selecionado no Combobox
    selected_tipo_gasto_nome = tk.StringVar()
    # Combobox para selecionar o tipo de gasto
    combobox_tipo_gasto = ttk.Combobox(specific_value_frame, textvariable=selected_tipo_gasto_nome, values=tipo_gasto_nomes, state="readonly")
    combobox_tipo_gasto.pack(pady=5, side="left", padx=10)
    combobox_tipo_gasto.set("Selecione") # Texto padrão

    # --- Seleção do tipo de gasto ---
    label_tipo_gasto2 = tk.Label(specific_value_frame, text="Total gasto 02:")
    label_tipo_gasto2.pack(pady=5, side="left", padx=10)
    # Carrega os tipos de gasto do banco de dados
    tipo_gasto_data2 = get_tipo_gasto_db()
    # Cria uma lista apenas com os nomes para o Combobox
    tipo_gasto_nomes2 = [item[1] for item in tipo_gasto_data2]
    # Variável para armazenar o nome selecionado no Combobox
    selected_tipo_gasto_nome2 = tk.StringVar()
    # Combobox para selecionar o tipo de gasto
    combobox_tipo_gasto2 = ttk.Combobox(specific_value_frame, textvariable=selected_tipo_gasto_nome2, values=tipo_gasto_nomes2, state="readonly")
    combobox_tipo_gasto2.pack(pady=5, side="left", padx=10)
    combobox_tipo_gasto2.set("Selecione") # Texto padrão

    # --- Seleção do tipo de gasto ---
    label_tipo_gasto3 = tk.Label(specific_value_frame, text="Total gasto 03:")
    label_tipo_gasto3.pack(pady=5, side="left", padx=10)
    # Carrega os tipos de gasto do banco de dados
    tipo_gasto_data3 = get_tipo_gasto_db()
    # Cria uma lista apenas com os nomes para o Combobox
    tipo_gasto_nomes3 = [item[1] for item in tipo_gasto_data3]
    # Variável para armazenar o nome selecionado no Combobox
    selected_tipo_gasto_nome3 = tk.StringVar()
    # Combobox para selecionar o tipo de gasto
    combobox_tipo_gasto3 = ttk.Combobox(specific_value_frame, textvariable=selected_tipo_gasto_nome3, values=tipo_gasto_nomes3, state="readonly")
    combobox_tipo_gasto3.pack(pady=5, side="left", padx=10)
    combobox_tipo_gasto3.set("Selecione") # Texto padrão

    # --- Seleção do tipo de gasto ---
    label_tipo_gasto4 = tk.Label(specific_value_frame, text="Total gasto 04:")
    label_tipo_gasto4.pack(pady=5, side="left", padx=10)
    # Carrega os tipos de gasto do banco de dados
    tipo_gasto_data4 = get_tipo_gasto_db()
    # Cria uma lista apenas com os nomes para o Combobox
    tipo_gasto_nomes4 = [item[1] for item in tipo_gasto_data4]
    # Variável para armazenar o nome selecionado no Combobox
    selected_tipo_gasto_nome4 = tk.StringVar()
    # Combobox para selecionar o tipo de gasto
    combobox_tipo_gasto4 = ttk.Combobox(specific_value_frame, textvariable=selected_tipo_gasto_nome4, values=tipo_gasto_nomes4, state="readonly")
    combobox_tipo_gasto4.pack(pady=5, side="left", padx=10)
    combobox_tipo_gasto4.set("Selecione") # Texto padrão

    # --- Frame para o relatório Treeview ---
    report_frame = ttk.Frame(content_frame)
    report_frame.pack(pady=10, fill=tk.BOTH, expand=True)

    # Definir colunas da Treeview
    columns = ("ID", "Data", "Valor", "Tipo de gasto", "Local", "Tipo pagamento", "Usuário", "Método pagamento", "Cartão", "Descrição")
    tree = ttk.Treeview(report_frame, columns=columns, show="headings")

    # Configurar cabeçalhos das colunas
    for col in columns:
        tree.heading(col, text=col, anchor=tk.W)
        tree.column(col, width=100) # Largura padrão, pode ajustar conforme necessário

    # Adicionar scrollbar
    scrollbar_y = ttk.Scrollbar(report_frame, orient="vertical", command=tree.yview)
    tree.configure(yscrollcommand=scrollbar_y.set)
    scrollbar_y.pack(side="right", fill="y")
    tree.pack(side="left", fill="both", expand=True)

    specific_totals_frame = tk.Frame(content_frame)
    specific_totals_frame.pack(pady=5, anchor='w', padx=50) 

    # Label para exibir o Valor Total Gasto 
    label_total_gasto = tk.Label(content_frame, text="", font=("Arial", 11, "bold"))
    label_total_gasto.pack(pady=5)

    # Label para o total de filtro01
    label_total_filtro01 = tk.Label(specific_totals_frame, text=f'', font=("Arial", 11, "bold"))
    label_total_filtro01.pack(pady=5, anchor='w', padx=30, side="left")

    # Label para o total de Lanche
    label_total_filtro02 = tk.Label(specific_totals_frame, text="", font=("Arial", 11, "bold"))
    label_total_filtro02.pack(pady=5, anchor='w', padx=30, side= "left")

    # Label para o total de happy hour
    label_total_filtro03 = tk.Label(specific_totals_frame, text="", font=("Arial", 11, "bold"))
    label_total_filtro03.pack(pady=5, anchor='w', padx=30, side= "left")

    # Label para o total de residencia
    label_total_filtro04 = tk.Label(specific_totals_frame, text="", font=("Arial", 11, "bold"))
    label_total_filtro04.pack(pady=5, anchor='w', padx=30, side= "left")

    def cons_completo_data_usu(data_inicio, data_fim, usuario):
        conn = conectar_bd()
        rel_completo_data_usuario = []
        if conn:
            cursor = conn.cursor()
            try:
                cursor.execute("SELECT RGA.ID, RGA.DATA_GASTO, RGA.VALOR_GASTO, TGA.NOME_TIPO_GASTO, LGA.NOME_LOCAL_GASTO, TPA.NOME_TIPO_PAGAMENTO, USU.NOME_USUARIO_PAGOU, MPA.NOME_METODO_PAGAMENTO, CAR.NOME_CARTAO, RGA.OBSERVACOES " \
                               "FROM T_REGISTROS_GASTO RGA " \
                               "INNER JOIN T_TIPO_GASTO TGA ON RGA.ID_TIPO_GASTO = TGA.ID_TIPO_GASTO " \
                               "INNER JOIN T_LOCAL_GASTO LGA ON RGA.ID_LOCAL_GASTO = LGA.ID_LOCAL_GASTO " \
                               "INNER JOIN T_TIPO_PAGAMENTO TPA ON RGA.ID_TIPO_PAGAMENTO = TPA.ID_TIPO_PAGAMENTO " \
                               "INNER JOIN T_USUARIO_PAGOU USU ON RGA.ID_USUARIO_PAGOU = USU.ID_USUARIO_PAGOU " \
                               "INNER JOIN T_METODO_PAGAMENTO MPA ON RGA.ID_METODO_PAGAMENTO = MPA.ID_METODO_PAGAMENTO " \
                               "INNER JOIN T_CARTAO CAR ON RGA.ID_CARTAO = CAR.ID_CARTAO " \
                               "WHERE RGA.DATA_GASTO BETWEEN (?) AND (?) AND USU.ID_USUARIO_PAGOU = (?);", (data_inicio, data_fim, usuario))
                for row in cursor.fetchall():
                    rel_completo_data_usuario.append(row)
            except pyodbc.Error as ex:
                sqlstate = ex.args[0]
                messagebox.showerror("Erro ao Consultar Dados", f"Não foi possível consultar os dados.\nErro: {sqlstate}")
            finally:
                conn.close()
        return rel_completo_data_usuario

    def on_consulta_usu_data():
        nome_selecionado = selected_usuario_name.get()
        data_inicio_str = entry_data_inicio.get()
        data_fim_str = entry_data_fim.get()
        tipo_gasto_filtro1 = selected_tipo_gasto_nome.get()
        tipo_gasto_filtro2 = selected_tipo_gasto_nome2.get()
        tipo_gasto_filtro3 = selected_tipo_gasto_nome3.get()
        tipo_gasto_filtro4 = selected_tipo_gasto_nome4.get()

        if nome_selecionado == "Selecione":
            messagebox.showwarning("Seleção Inválida", "Por favor, selecione um usuário.")
            return
        
        if tipo_gasto_filtro1 == "Selecione":
            messagebox.showwarning("Seleção Inválida", "Por favor, selecione um total gasto 01.")
            return
        
        if tipo_gasto_filtro2 == "Selecione":
            messagebox.showwarning("Seleção Inválida", "Por favor, selecione um total gasto 02.")
            return
        
        if tipo_gasto_filtro3 == "Selecione":
            messagebox.showwarning("Seleção Inválida", "Por favor, selecione um total gasto 03.")
            return
        
        if tipo_gasto_filtro4 == "Selecione":
            messagebox.showwarning("Seleção Inválida", "Por favor, selecione um total gasto 04.")
            return

        id_usuario_selecionado = None
        for user_id, user_name in usuarios_data:
            if user_name == nome_selecionado:
                id_usuario_selecionado = user_id
                break

        if id_usuario_selecionado is None:
            messagebox.showerror("Erro Interno", "Não foi possível encontrar o ID do usuário selecionado.")
            return


        try:
            data_inicio_bd = datetime.datetime.strptime(data_inicio_str, "%d/%m/%Y").date()
        except ValueError:
            messagebox.showwarning("Data Inicial Inválida", "Formato de data incorreto. Use DD/MM/AAAA.")
            return

        try:
            data_fim_bd = datetime.datetime.strptime(data_fim_str, "%d/%m/%Y").date()
        except ValueError:
            messagebox.showwarning("Data Final Inválida", "Formato de data incorreto. Use DD/MM/AAAA.")
            return

        # Limpar a Treeview antes de inserir novos dados
        for item in tree.get_children():
            tree.delete(item)

        # Obter os dados do relatório
        dados_relatorio = cons_completo_data_usu(data_inicio_bd, data_fim_bd, id_usuario_selecionado)

        if dados_relatorio:
            for row_data in dados_relatorio:
                # Formatar a data para exibição (se necessário)
                formatted_row_data = list(row_data)
                if isinstance(formatted_row_data[1], datetime.date): # Supondo que a data está na segunda coluna (índice 1)
                    formatted_row_data[1] = formatted_row_data[1].strftime("%d/%m/%Y")
                tree.insert("", tk.END, values=formatted_row_data)
        else:
            messagebox.showinfo("Nenhum Registro", "Nenhum registro encontrado para os critérios selecionados.")
        
        total_gasto = 0.0 # Inicializa o contador do total
        total_filtro1_saida = 0.0
        total_filtro2_saida = 0.0
        total_filtro3_saida = 0.0
        total_filtro4_saida = 0.0  
        if dados_relatorio:
            for row_data in dados_relatorio:
                formatted_row_data = list(row_data)                    
                try:
                    valor_atual = float(formatted_row_data[2])
                    total_gasto += valor_atual
                    # Formatar o valor para exibição na Treeview (ex: R$ 123,45)
                    formatted_row_data[2] = f"R$ {valor_atual:.2f}".replace('.', ',')
                    tipo_gasto_01 = formatted_row_data[3]
                    if tipo_gasto_01 == tipo_gasto_filtro1:
                        total_filtro1_saida += valor_atual
                    tipo_gasto_02 = formatted_row_data[3] # Tipo Gasto está no índice 3
                    if tipo_gasto_02 == tipo_gasto_filtro2: # Verifique se o nome do tipo de gasto é "Mercado"
                        total_filtro2_saida += valor_atual # Somar ao total gasto (Valor Gasto está na coluna de índice 2)
                    tipo_gasto_03 = formatted_row_data[3]
                    if tipo_gasto_03 == tipo_gasto_filtro3:
                        total_filtro3_saida += valor_atual
                    tipo_gasto_04 = formatted_row_data[3]
                    if tipo_gasto_04 == tipo_gasto_filtro4:
                        total_filtro4_saida += valor_atual
                    
                    
                except ValueError:
                    # Lida com casos onde o valor não é um número válido
                    formatted_row_data[2] = "N/A"
                    messagebox.showwarning("Erro de Valor", f"Valor inválido encontrado: {formatted_row_data[2]}. Ignorando para o total.")
            
            # Atualiza o Label com o valor total formatado
            label_total_gasto.config(text=f"Total: R$ {total_gasto:.2f}".replace('.', ','))
            label_total_filtro01.config(text=f"Total gasto em {tipo_gasto_filtro1.lower()}: R$ {total_filtro1_saida:.2f}".replace('.', ','))
            label_total_filtro02.config(text=f"Total gasto em {tipo_gasto_filtro2.lower()}: R$ {total_filtro2_saida:.2f}".replace('.', ','))
            label_total_filtro03.config(text=f"Total gasto em {tipo_gasto_filtro3.lower()}: R$ {total_filtro3_saida:.2f}".replace('.', ','))
            label_total_filtro04.config(text=f"Total gasto em {tipo_gasto_filtro4.lower()}: R$ {total_filtro4_saida:.2f}".replace('.', ','))

    btn_salvar = tk.Button(specific_dat_frame, text="Buscar", command=on_consulta_usu_data, width=25, height=2)
    btn_salvar.pack(pady=10, side="left", padx=10)
    btn_voltar = tk.Button(specific_dat_frame, text="Voltar", command=lambda: show_relatorios_screen(content_frame), width=25, height=2)
    btn_voltar.pack(pady=10, side="left", padx=10)

def show_completo_data(content_frame):
    clear_frame(content_frame)

    label_title = tk.Label(content_frame, text="Relatório Por Data", font=("Arial", 16, "bold"))
    label_title.pack(pady=10)

    specific_dat_frame = tk.Frame(content_frame)
    specific_dat_frame.pack(pady=5, anchor='w', padx=50) 

    # --- Entrada de Data da Compra (Manual) ---
    label_data_inicio = tk.Label(specific_dat_frame, text="Data início:")
    label_data_inicio.pack(pady=5, side="left", padx=10)
    entry_data_inicio = tk.Entry(specific_dat_frame, width=40)
    entry_data_inicio.pack(pady=5, side="left", padx=10)
    entry_data_inicio.insert(0, datetime.datetime.now().strftime("%d/%m/%Y"))

    label_data_fim = tk.Label(specific_dat_frame, text="Data fim:")
    label_data_fim.pack(pady=5, side="left", padx=10)
    entry_data_fim = tk.Entry(specific_dat_frame, width=40)
    entry_data_fim.pack(pady=5, side="left", padx=10)
    entry_data_fim.insert(0, datetime.datetime.now().strftime("%d/%m/%Y"))

    specific_value_frame = tk.Frame(content_frame)
    specific_value_frame.pack(pady=5, anchor='w', padx=50) 

    # --- Seleção do tipo de gasto ---
    label_tipo_gasto = tk.Label(specific_value_frame, text="Total gasto 01:")
    label_tipo_gasto.pack(pady=5, side="left", padx=10)
    # Carrega os tipos de gasto do banco de dados
    tipo_gasto_data = get_tipo_gasto_db()
    # Cria uma lista apenas com os nomes para o Combobox
    tipo_gasto_nomes = [item[1] for item in tipo_gasto_data]
    # Variável para armazenar o nome selecionado no Combobox
    selected_tipo_gasto_nome = tk.StringVar()
    # Combobox para selecionar o tipo de gasto
    combobox_tipo_gasto = ttk.Combobox(specific_value_frame, textvariable=selected_tipo_gasto_nome, values=tipo_gasto_nomes, state="readonly")
    combobox_tipo_gasto.pack(pady=5, side="left", padx=10)
    combobox_tipo_gasto.set("Selecione") # Texto padrão

    # --- Seleção do tipo de gasto ---
    label_tipo_gasto2 = tk.Label(specific_value_frame, text="Total gasto 02:")
    label_tipo_gasto2.pack(pady=5, side="left", padx=10)
    # Carrega os tipos de gasto do banco de dados
    tipo_gasto_data2 = get_tipo_gasto_db()
    # Cria uma lista apenas com os nomes para o Combobox
    tipo_gasto_nomes2 = [item[1] for item in tipo_gasto_data2]
    # Variável para armazenar o nome selecionado no Combobox
    selected_tipo_gasto_nome2 = tk.StringVar()
    # Combobox para selecionar o tipo de gasto
    combobox_tipo_gasto2 = ttk.Combobox(specific_value_frame, textvariable=selected_tipo_gasto_nome2, values=tipo_gasto_nomes2, state="readonly")
    combobox_tipo_gasto2.pack(pady=5, side="left", padx=10)
    combobox_tipo_gasto2.set("Selecione") # Texto padrão

    # --- Seleção do tipo de gasto ---
    label_tipo_gasto3 = tk.Label(specific_value_frame, text="Total gasto 03:")
    label_tipo_gasto3.pack(pady=5, side="left", padx=10)
    # Carrega os tipos de gasto do banco de dados
    tipo_gasto_data3 = get_tipo_gasto_db()
    # Cria uma lista apenas com os nomes para o Combobox
    tipo_gasto_nomes3 = [item[1] for item in tipo_gasto_data3]
    # Variável para armazenar o nome selecionado no Combobox
    selected_tipo_gasto_nome3 = tk.StringVar()
    # Combobox para selecionar o tipo de gasto
    combobox_tipo_gasto3 = ttk.Combobox(specific_value_frame, textvariable=selected_tipo_gasto_nome3, values=tipo_gasto_nomes3, state="readonly")
    combobox_tipo_gasto3.pack(pady=5, side="left", padx=10)
    combobox_tipo_gasto3.set("Selecione") # Texto padrão

    # --- Seleção do tipo de gasto ---
    label_tipo_gasto4 = tk.Label(specific_value_frame, text="Total gasto 04:")
    label_tipo_gasto4.pack(pady=5, side="left", padx=10)
    # Carrega os tipos de gasto do banco de dados
    tipo_gasto_data4 = get_tipo_gasto_db()
    # Cria uma lista apenas com os nomes para o Combobox
    tipo_gasto_nomes4 = [item[1] for item in tipo_gasto_data4]
    # Variável para armazenar o nome selecionado no Combobox
    selected_tipo_gasto_nome4 = tk.StringVar()
    # Combobox para selecionar o tipo de gasto
    combobox_tipo_gasto4 = ttk.Combobox(specific_value_frame, textvariable=selected_tipo_gasto_nome4, values=tipo_gasto_nomes4, state="readonly")
    combobox_tipo_gasto4.pack(pady=5, side="left", padx=10)
    combobox_tipo_gasto4.set("Selecione") # Texto padrão

    # --- Frame para o relatório Treeview ---
    report_frame = ttk.Frame(content_frame)
    report_frame.pack(pady=10, fill=tk.BOTH, expand=True)

    # Definir colunas da Treeview
    columns = ("ID", "Data", "Valor", "Tipo de gasto", "Local", "Tipo pagamento", "Usuário pagou", "Método pagamento", "Cartão", "Descrição")
    tree = ttk.Treeview(report_frame, columns=columns, show="headings")

    # Configurar cabeçalhos das colunas
    for col in columns:
        tree.heading(col, text=col, anchor=tk.W)
        tree.column(col, width=100) # Largura padrão, pode ajustar conforme necessário

    # Adicionar scrollbar
    scrollbar_y = ttk.Scrollbar(report_frame, orient="vertical", command=tree.yview)
    tree.configure(yscrollcommand=scrollbar_y.set)
    scrollbar_y.pack(side="right", fill="y")
    tree.pack(side="left", fill="both", expand=True)

    specific_totals_frame = tk.Frame(content_frame)
    specific_totals_frame.pack(pady=5, anchor='w', padx=50) 

    # Label para exibir o Valor Total Gasto 
    label_total_gasto = tk.Label(content_frame, text="", font=("Arial", 11, "bold"))
    label_total_gasto.pack(pady=5)

    # Label para o total de filtro01
    label_total_filtro01 = tk.Label(specific_totals_frame, text=f'', font=("Arial", 11, "bold"))
    label_total_filtro01.pack(pady=5, anchor='w', padx=30, side="left")

    # Label para o total de Lanche
    label_total_filtro02 = tk.Label(specific_totals_frame, text="", font=("Arial", 11, "bold"))
    label_total_filtro02.pack(pady=5, anchor='w', padx=30, side= "left")

    # Label para o total de happy hour
    label_total_filtro03 = tk.Label(specific_totals_frame, text="", font=("Arial", 11, "bold"))
    label_total_filtro03.pack(pady=5, anchor='w', padx=30, side= "left")

    # Label para o total de residencia
    label_total_filtro04 = tk.Label(specific_totals_frame, text="", font=("Arial", 11, "bold"))
    label_total_filtro04.pack(pady=5, anchor='w', padx=30, side= "left")

    def cons_completo_data(data_inicio, data_fim):
        conn = conectar_bd()
        rel_completo_data_usuario = []
        if conn:
            cursor = conn.cursor()
            try:
                cursor.execute("SELECT RGA.ID, RGA.DATA_GASTO, RGA.VALOR_GASTO, TGA.NOME_TIPO_GASTO, LGA.NOME_LOCAL_GASTO, TPA.NOME_TIPO_PAGAMENTO, USU.NOME_USUARIO_PAGOU, MPA.NOME_METODO_PAGAMENTO, CAR.NOME_CARTAO, RGA.OBSERVACOES " \
                               "FROM T_REGISTROS_GASTO RGA " \
                               "INNER JOIN T_TIPO_GASTO TGA ON RGA.ID_TIPO_GASTO = TGA.ID_TIPO_GASTO " \
                               "INNER JOIN T_LOCAL_GASTO LGA ON RGA.ID_LOCAL_GASTO = LGA.ID_LOCAL_GASTO " \
                               "INNER JOIN T_TIPO_PAGAMENTO TPA ON RGA.ID_TIPO_PAGAMENTO = TPA.ID_TIPO_PAGAMENTO " \
                               "INNER JOIN T_USUARIO_PAGOU USU ON RGA.ID_USUARIO_PAGOU = USU.ID_USUARIO_PAGOU " \
                               "INNER JOIN T_METODO_PAGAMENTO MPA ON RGA.ID_METODO_PAGAMENTO = MPA.ID_METODO_PAGAMENTO " \
                               "INNER JOIN T_CARTAO CAR ON RGA.ID_CARTAO = CAR.ID_CARTAO " \
                               "WHERE RGA.DATA_GASTO BETWEEN (?) AND (?);", (data_inicio, data_fim))
                for row in cursor.fetchall():
                    rel_completo_data_usuario.append(row)
            except pyodbc.Error as ex:
                sqlstate = ex.args[0]
                messagebox.showerror("Erro ao Consultar Dados", f"Não foi possível consultar os dados.\nErro: {sqlstate}")
            finally:
                conn.close()
        return rel_completo_data_usuario

    def on_consulta_data():
        data_inicio_str = entry_data_inicio.get()
        data_fim_str = entry_data_fim.get()
        tipo_gasto_filtro1 = selected_tipo_gasto_nome.get()
        tipo_gasto_filtro2 = selected_tipo_gasto_nome2.get()
        tipo_gasto_filtro3 = selected_tipo_gasto_nome3.get()
        tipo_gasto_filtro4 = selected_tipo_gasto_nome4.get()

        if tipo_gasto_filtro1 == "Selecione":
            messagebox.showwarning("Seleção Inválida", "Por favor, selecione um total gasto 01.")
            return
        
        if tipo_gasto_filtro2 == "Selecione":
            messagebox.showwarning("Seleção Inválida", "Por favor, selecione um total gasto 02.")
            return
        
        if tipo_gasto_filtro3 == "Selecione":
            messagebox.showwarning("Seleção Inválida", "Por favor, selecione um total gasto 03.")
            return
        
        if tipo_gasto_filtro4 == "Selecione":
            messagebox.showwarning("Seleção Inválida", "Por favor, selecione um total gasto 04.")
            return

        try:
            data_inicio_bd = datetime.datetime.strptime(data_inicio_str, "%d/%m/%Y").date()
        except ValueError:
            messagebox.showwarning("Data Inicial Inválida", "Formato de data incorreto. Use DD/MM/AAAA.")
            return

        try:
            data_fim_bd = datetime.datetime.strptime(data_fim_str, "%d/%m/%Y").date()
        except ValueError:
            messagebox.showwarning("Data Final Inválida", "Formato de data incorreto. Use DD/MM/AAAA.")
            return

        # Limpar a Treeview antes de inserir novos dados
        for item in tree.get_children():
            tree.delete(item)

        # Obter os dados do relatório
        dados_relatorio = cons_completo_data(data_inicio_bd, data_fim_bd)

        if dados_relatorio:
            for row_data in dados_relatorio:
                # Formatar a data para exibição (se necessário)
                formatted_row_data = list(row_data)
                if isinstance(formatted_row_data[1], datetime.date): # Supondo que a data está na segunda coluna (índice 1)
                    formatted_row_data[1] = formatted_row_data[1].strftime("%d/%m/%Y")
                tree.insert("", tk.END, values=formatted_row_data)
        else:
            messagebox.showinfo("Nenhum Registro", "Nenhum registro encontrado para os critérios selecionados.")
        
        total_gasto = 0.0 # Inicializa o contador do total
        total_filtro1_saida = 0.0
        total_filtro2_saida = 0.0
        total_filtro3_saida = 0.0
        total_filtro4_saida = 0.0  
        if dados_relatorio:
            for row_data in dados_relatorio:
                formatted_row_data = list(row_data)                    
                try:
                    valor_atual = float(formatted_row_data[2])
                    total_gasto += valor_atual
                    # Formatar o valor para exibição na Treeview (ex: R$ 123,45)
                    formatted_row_data[2] = f"R$ {valor_atual:.2f}".replace('.', ',')
                    tipo_gasto_01 = formatted_row_data[3]
                    if tipo_gasto_01 == tipo_gasto_filtro1:
                        total_filtro1_saida += valor_atual
                    tipo_gasto_02 = formatted_row_data[3] # Tipo Gasto está no índice 3
                    if tipo_gasto_02 == tipo_gasto_filtro2: # Verifique se o nome do tipo de gasto é "Mercado"
                        total_filtro2_saida += valor_atual # Somar ao total gasto (Valor Gasto está na coluna de índice 2)
                    tipo_gasto_03 = formatted_row_data[3]
                    if tipo_gasto_03 == tipo_gasto_filtro3:
                        total_filtro3_saida += valor_atual
                    tipo_gasto_04 = formatted_row_data[3]
                    if tipo_gasto_04 == tipo_gasto_filtro4:
                        total_filtro4_saida += valor_atual
                    
                    
                except ValueError:
                    # Lida com casos onde o valor não é um número válido
                    formatted_row_data[2] = "N/A"
                    messagebox.showwarning("Erro de Valor", f"Valor inválido encontrado: {formatted_row_data[2]}. Ignorando para o total.")
            
            # Atualiza o Label com o valor total formatado
            label_total_gasto.config(text=f"Total: R$ {total_gasto:.2f}".replace('.', ','))
            label_total_filtro01.config(text=f"Total gasto em {tipo_gasto_filtro1.lower()}: R$ {total_filtro1_saida:.2f}".replace('.', ','))
            label_total_filtro02.config(text=f"Total gasto em {tipo_gasto_filtro2.lower()}: R$ {total_filtro2_saida:.2f}".replace('.', ','))
            label_total_filtro03.config(text=f"Total gasto em {tipo_gasto_filtro3.lower()}: R$ {total_filtro3_saida:.2f}".replace('.', ','))
            label_total_filtro04.config(text=f"Total gasto em {tipo_gasto_filtro4.lower()}: R$ {total_filtro4_saida:.2f}".replace('.', ','))

    btn_salvar = tk.Button(specific_dat_frame, text="Buscar", command=on_consulta_data, width=25, height=2)
    btn_salvar.pack(pady=10, side="left", padx=10)
    btn_voltar = tk.Button(specific_dat_frame, text="Voltar", command=lambda: show_relatorios_screen(content_frame), width=25, height=2)
    btn_voltar.pack(pady=10, side="left", padx=10)

# --- Classe Principal da Aplicação Tkinter ---
class MainApplication(tk.Tk):
    #Define a janela principal da aplicação e gerencia o frame de conteúdo.
    def __init__(self):
        super().__init__()
        self.title("Sistema de Gastos")
        self.geometry("600x1000") # Define um tamanho maior para a janela principal
        self.state('zoomed') # denife que a janela irá iniciar maximizada
        # Cria um frame que irá conter todo o conteúdo dinâmico da aplicação.
        # Este frame será limpo e preenchido novamente conforme o usuário navega pelos menus.
        self.content_frame = tk.Frame(self)
        self.content_frame.pack(fill="both", expand=True, padx=10, pady=10) # Preenche e expande na janela
        
        # Exibe o menu principal assim que a aplicação é iniciada
        show_main_menu(self)

# --- Ponto de Entrada da Aplicação ---
if __name__ == "__main__":
    app = MainApplication() # Cria uma instância da nossa aplicação principal
    app.mainloop()          # Inicia o loop principal do Tkinter, que mantém a janela aberta e interativa
    