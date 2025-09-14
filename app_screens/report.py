import tkinter as tk
import pyodbc
import datetime
from func_bd import conectar_bd, get_usuarios_db, get_tipo_gasto_db
from tkinter import messagebox, ttk
from app_screens.utils import clear_frame

def show_relatorios_screen(content_frame, back_command):
    #Exibe a tela do menu 'Relatórios'.
    clear_frame(content_frame)
    label_title = tk.Label(content_frame, text="Relatórios", font=("Arial", 16, "bold"))
    label_title.pack(pady=20)
    
    # Sub-opções relatório completo por data e usuário
    btn_completo_data = tk.Button(content_frame, text="Data e usuário", command=lambda: show_completo_data_usuario(content_frame, back_command), width=25, height=2)
    btn_completo_data.pack(pady=5)

    # Sub-opções relatório completo por data
    btn_completo_data = tk.Button(content_frame, text="Data", command=lambda: show_completo_data(content_frame, back_command), width=25, height=2)
    btn_completo_data.pack(pady=5)

    # Botão para voltar ao menu principal
    btn_voltar = tk.Button(content_frame, text="Voltar", command=back_command, width=25, height=2)
    btn_voltar.pack(pady=20)

def show_completo_data_usuario(content_frame, back_command):
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
    btn_voltar = tk.Button(specific_dat_frame, text="Voltar", command=lambda: show_relatorios_screen(content_frame, back_command), width=25, height=2)
    btn_voltar.pack(pady=10, side="left", padx=10)

def show_completo_data(content_frame, back_command):
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
    btn_voltar = tk.Button(specific_dat_frame, text="Voltar", command=lambda: show_relatorios_screen(content_frame, back_command), width=25, height=2)
    btn_voltar.pack(pady=10, side="left", padx=10)