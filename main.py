import tkinter as tk
from app_screens.utils import clear_frame 
from app_screens.buy import show_compras_screen
from app_screens.register import show_cadastros_screen
from app_screens.report import show_relatorios_screen

# --- Classe Principal da Aplicação Tkinter ---
class MainApplication(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Sistema de Gastos")
        self.geometry("600x1000")
        self.state('zoomed')
        self.screens = {
            "Compras": show_compras_screen,
            "Cadastros": show_cadastros_screen,
            "Relatórios": show_relatorios_screen
        }

        # Cria o frame de conteúdo que será dinâmico
        self.content_frame = tk.Frame(self)
        self.content_frame.pack(fill="both", expand=True, padx=10, pady=10)

        # Exibe o menu principal ao iniciar a aplicação
        self.show_main_menu()

    def show_main_menu(self):
        clear_frame(self.content_frame)

        # Título de boas-vindas
        label_welcome = tk.Label(self.content_frame, text="Bem-vindo ao Sistema de Gastos", font=("Arial", 18, "bold"))
        label_welcome.pack(pady=20)

        # Cria um botão para cada tela no dicionário self.screens
        for name, screen_function in self.screens.items():

            btn = tk.Button(
                self.content_frame, 
                text=f"{name}",
                command=lambda func=screen_function: self.show_screen(func), 
                width=20, 
                height=2)
            btn.pack(pady=10)
    
    def show_screen(self, screen_function):
        """
        Exibe a tela selecionada.
        """
        # A função da tela é chamada aqui, com os argumentos corretos
        screen_function(self.content_frame, self.show_main_menu)

# --- Ponto de Entrada da Aplicação ---
if __name__ == "__main__":
    app = MainApplication()
    app.mainloop()