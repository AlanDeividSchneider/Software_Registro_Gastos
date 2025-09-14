import tkinter as tk
import pyodbc
import datetime
from func_bd import conectar_bd, get_usuarios_db, get_tipo_gasto_db, get_local_gasto_db
from func_bd import get_tipo_pagamento_db, get_metodo_pagamento_db, get_cartao_db
from func_bd import deletar_compra_db, salvar_nova_compra_db, alterar_compra_db
from app_screens.utils import clear_frame
from tkinter import messagebox, ttk
from tkcalendar import Calendar

def show_compras_screen(content_frame, back_command):
    #Exibe a tela do menu 'Compras' com suas sub-opções.
    clear_frame(content_frame) # Limpa o frame para o conteúdo de Compras
    
    label_title = tk.Label(content_frame, text="Compras", font=("Arial", 16, "bold"))
    label_title.pack(pady=10)

    # Sub-opções para nova compra
    btn_nova_compra = tk.Button(content_frame, text="Nova compra", command=lambda: show_nova_compra(content_frame, back_command), width=20, height=2)
    btn_nova_compra.pack(pady=10)

    # Sub-opções para nova compra
    btn_alterar_compra = tk.Button(content_frame, text="Alterar compra", command=lambda: show_alterar_compra(content_frame, back_command), width=20, height=2)
    btn_alterar_compra.pack(pady=10)

    # Botão para voltar ao menu principal
    btn_voltar = tk.Button(content_frame, text="Voltar", command=back_command, width=20, height=2)
    btn_voltar.pack(pady=10)

def show_alterar_compra(content_frame, back_command):
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
    btn_voltar = tk.Button(botoes_frame, text="Voltar", command=lambda: show_compras_screen(content_frame, back_command), width=20, height=2)
    btn_voltar.pack(side='left', padx=5)

def show_nova_compra(content_frame, back_command):
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
    btn_voltar = tk.Button(specific_compra5_frame, text="Voltar", command=lambda: show_compras_screen(content_frame, back_command), width=25, height=2)
    btn_voltar.pack(pady=10, padx=10, side="left")