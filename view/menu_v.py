import tkinter as tk
from controler.delete_c import DeleteController
from model.usuario_m import UsuarioModel
from view.delete_v import DeleteView
from view.escolha_chefe_v import EscolhaView

from PIL import Image, ImageTk
from tkinter import Menu, Menubutton, Frame, BOTH, RAISED


# Definindo o caminho da imagem (ajuste conforme necessário)
image_path = "midia/imagens/Rockman_X5.webp"

class MenuView(Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.create_widgets()

    def opcao_selecionada(self, opcao):
        if opcao == "1":
            self.master.switch_frame(EscolhaView)
            self.master.title("Escolha de Chefes - Megaman X5")
        

    def criar_menu_dropdown(self, master):
        menu_dropdown = Menu(master, tearoff=0)
        menu_dropdown.add_command(label="Começar o Jogo", command=lambda: self.opcao_selecionada("1"))
        
        return menu_dropdown

    def create_widgets(self):
        mb = Menubutton(self, text="Menu", relief=RAISED)
        mb.menu = self.criar_menu_dropdown(mb)
        mb["menu"] = mb.menu
        mb.pack(anchor="center", pady=12, padx=12)

        # Carregar e exibir a imagem
        img = Image.open(image_path)
        img = img.resize((650, 550), Image.LANCZOS)
        photo = ImageTk.PhotoImage(img)
        
        label = tk.Label(self, image=photo)
        label.image = photo  # manter uma referência para evitar garbage collection
        label.pack(pady=10)