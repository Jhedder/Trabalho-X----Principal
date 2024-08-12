import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from PIL import Image, ImageTk

class SplashView(tk.Frame):
  
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.pack(fill=tk.BOTH, expand=True)
        self.create_widgets()
    def button_click(self):
            print("Botão clicado!")
            self.destroy()
            self.parent.menu_v.pack()    
            

    def create_widgets(self):
        parent = self.parent
        parent.title('Megaman X5')

            # Abre a imagem usando PIL (Pillow)
        image = Image.open("midia/imagens/maxresdefault.jpg")

            # Converte a imagem PIL para um objeto PhotoImage
        photo = ImageTk.PhotoImage(image)

            # Cria um Label para exibir a imagem
        self.label = tk.Label(self, image=photo)
        self.label.pack()

            # Cria um Frame para o botão
        self.frame = tk.Frame(self)
        self.frame.pack(pady=10)

            # Cria o botão dentro do Frame
        self.button = tk.Button(self.frame, text="Iniciar o Jogo", command=self.button_click)
        self.button.pack()
        self.mainloop()

    def fechar_children(self):
        # Obter a lista de children da janela principal
        children = self.winfo_children()
        
        # Fechar cada child
        for child in children:
            child.destroy()