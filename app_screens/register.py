import tkinter as tk
from func_bd import adicionar_usuario_pagou_db, adicionar_tipo_gasto, adicionar_local_gasto
from func_bd import adicionar_cartao, adicionar_tipo_pagamento, adicionar_metodo_pagamento
from tkinter import messagebox
from app_screens.utils import clear_frame

def show_cadastros_screen(content_frame, back_command):
    #Exibe a tela do menu 'Configurações'.
    clear_frame(content_frame)
    label_title = tk.Label(content_frame, text="Cadastros", font=("Arial", 16, "bold"))
    label_title.pack(pady=20)

    # Sub-opções para cadastro de usuário
    btn_cadastro_usuario = tk.Button(content_frame, text="Usuário", command=lambda: show_cadastrar_usuario(content_frame, back_command), width=25, height=2)
    btn_cadastro_usuario.pack(pady=5)

    # Sub-opções para cadastro de tipo de gasto
    btn_cadastro_tipo_gasto = tk.Button(content_frame, text="Tipo de gasto", command=lambda: show_cadastrar_tipo_gasto(content_frame, back_command), width=25, height=2)
    btn_cadastro_tipo_gasto.pack(pady=5)

    # Sub-opções para cadastro de local de gasto
    btn_cadastro_local_gasto = tk.Button(content_frame, text="Local", command=lambda: show_cadastrar_local_gasto(content_frame, back_command), width=25, height=2)
    btn_cadastro_local_gasto.pack(pady=5)

    # Sub-opções para cadastro de tipo de pagamento
    btn_cadastro_tipo_pagamento = tk.Button(content_frame, text="Tipo de pagamento", command=lambda: show_cadastrar_tipo_pagamento(content_frame, back_command), width=25, height=2)
    btn_cadastro_tipo_pagamento.pack(pady=5)

    # Sub-opções para cadastro de metodo de pagamento
    btn_cadastro_metodo_pagamento = tk.Button(content_frame, text="Metodo de pagamento", command=lambda: show_cadastrar_metodo_pagamento(content_frame, back_command), width=25, height=2)
    btn_cadastro_metodo_pagamento.pack(pady=5)

    # Sub-opções para cadastro de cartão
    btn_cadastro_cartao = tk.Button(content_frame, text="Cartão", command=lambda: show_cadastrar_cartao(content_frame, back_command), width=25, height=2)
    btn_cadastro_cartao.pack(pady=5)

    # Botão para voltar ao menu principal
    btn_voltar = tk.Button(content_frame, text="Voltar", command=back_command, width=25, height=2)
    btn_voltar.pack(pady=25)

def show_cadastrar_usuario(content_frame, back_command):
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
    btn_voltar = tk.Button(content_frame, text="Voltar", command=lambda: show_cadastros_screen(content_frame, back_command), width=25, height=2)
    btn_voltar.pack(pady=5)

def show_cadastrar_tipo_gasto(content_frame, back_command):
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
    btn_voltar = tk.Button(content_frame, text="Voltar", command=lambda: show_cadastros_screen(content_frame, back_command), width=25, height=2)
    btn_voltar.pack(pady=5)

def show_cadastrar_local_gasto(content_frame, back_command):
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
    btn_voltar = tk.Button(content_frame, text="Voltar", command=lambda: show_cadastros_screen(content_frame, back_command), width=25, height=2)
    btn_voltar.pack(pady=5)

def show_cadastrar_tipo_pagamento(content_frame, back_command):
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
    btn_voltar = tk.Button(content_frame, text="Voltar", command=lambda: show_cadastros_screen(content_frame, back_command), width=25, height=2)
    btn_voltar.pack(pady=5)

def show_cadastrar_metodo_pagamento(content_frame, back_command):
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
    btn_voltar = tk.Button(content_frame, text="Voltar", command=lambda: show_cadastros_screen(content_frame, back_command), width=25, height=2)
    btn_voltar.pack(pady=5)

def show_cadastrar_cartao(content_frame, back_command):
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
    btn_voltar = tk.Button(content_frame, text="Voltar", command=lambda: show_cadastros_screen(content_frame, back_command), width=25, height=2)
    btn_voltar.pack(pady=5)