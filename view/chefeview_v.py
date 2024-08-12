import tkinter as tk
from PIL import Image, ImageTk

class ChefeView(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.pack(fill=tk.BOTH, expand=True)
      
        

    def create_widgets(self):
        # Criar a janela principal
        self.parent.title("Burn Dinorex - Mega Man X5")
        self.parent.resizable(False, False)

        # Aumentar o tamanho mínimo da janela
        min_width, min_height = 600, 600
        self.parent.minsize(min_width, min_height)

        # Criar um canvas para o fundo com gradiente
        self.canvas = tk.Canvas(self, width=min_width, height=min_height,background="Grey")
        self.canvas.pack(fill=tk.BOTH, expand=True)

        # Caminho inicial da imagem
        self.image_path = "midia/imagens/BurnDinorex.jpg"
        self.photo = None
        self.image_label = tk.Label(self, bg='#8B0000')
        self.image_label.place(x=150, y=100)

        self.update_image()

        # Texto com informações sobre o Magma Dragoon
        

        self.text_label = tk.Label(self, justify=tk.LEFT, padx=10, pady=10, bg='#8B0000', fg='white',
                                font=('Helvetica', 12), wraplength=550)  # Largura máxima em pixels
        self.text_label.place(x=75, y=570, width=550)  # Define a largura do Label



        # Criar um botão para atualizar a imagem
        self.escolher_button = tk.Button(self, text="Atualizar Chefe")
        self.escolher_button.place(x=300, y=700)

    def update_image(self):
        original_image = Image.open(self.image_path)
        resized_image = original_image.resize((400, 400))
        self.photo = ImageTk.PhotoImage(resized_image)
        self.image_label.config(image=self.photo)

    def update_info(self,textp):
        self.text_label.config(text=textp)