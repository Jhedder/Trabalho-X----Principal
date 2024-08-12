import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from PIL import Image, ImageTk

class UsuarioView(tk.Frame):
  
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.pack(fill=tk.BOTH, expand=True)
        self.master.geometry('600x600')
        self.create_widgets()
        
def button_click():
        print("Botão clicado!")
        root.destroy()  # Destroi a janela principal quando o botão é clicado

root = tk.Tk()
root.title('Megaman X5')

    # Abre a imagem usando PIL (Pillow)
image = Image.open("C:/Users/182400232/Documents/Trabalho/Trabalho X/Imagens/maxresdefault.jpg")

    # Converte a imagem PIL para um objeto PhotoImage
photo = ImageTk.PhotoImage(image)

    # Cria um Label para exibir a imagem
label = tk.Label(root, image=photo)
label.pack()

    # Cria um Frame para o botão
frame = tk.Frame(root)
frame.pack(pady=10)

    # Cria o botão dentro do Frame
button = tk.Button(frame, text="Iniciar o Jogo", command=button_click)
button.pack()

root.mainloop()