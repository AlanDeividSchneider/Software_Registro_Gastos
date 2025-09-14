import tkinter as tk

# --- Funções para Gerenciar as Telas (Frames) ---
def clear_frame(frame):
    #Remove todos os widgets de um frame para preparar para um novo conteúdo.
    for widget in frame.winfo_children():
        widget.destroy()

