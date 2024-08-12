import tkinter as tk
from PIL import Image, ImageTk

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

#User_v Abaixo:
# import tkinter as tk
# from tkinter import ttk
# from tkinter import messagebox
# from PIL import Image, ImageTk

# class UsuarioView(tk.Frame):
  
#     def __init__(self, parent):
#         super().__init__(parent)
#         self.parent = parent
#         self.pack(fill=tk.BOTH, expand=True)
#         self.master.geometry('600x600')
#         self.create_widgets()
        

    

#     def button_click():
#         print("Botão clicado!")
#         root.destroy()  # Destroi a janela principal quando o botão é clicado

#     root = tk.Tk()
#     root.title('Megaman X5')

#     # Abre a imagem usando PIL (Pillow)
#     image = Image.open("C:/Users/182400232/Documents/Trabalho/Trabalho X/Imagens/maxresdefault.jpg")

#     # Converte a imagem PIL para um objeto PhotoImage
#     photo = ImageTk.PhotoImage(image)

#     # Cria um Label para exibir a imagem
#     label = tk.Label(root, image=photo)
#     label.pack()

#     # Cria um Frame para o botão
#     frame = tk.Frame(root)
#     frame.pack(pady=10)

#     # Cria o botão dentro do Frame
#     button = tk.Button(frame, text="Iniciar o Jogo", command=button_click)
#     button.pack()

#     root.mainloop()

    
    
#     def create_widgets(self):
#         self.nome_label = ttk.Label(self, text="Nome:")
#         self.nome_label.grid(row=0, column=0, padx=10, pady=5)
       
#         self.nome_entry = ttk.Entry(self)
#         self.nome_entry.grid(row=0, column=1, padx=10, pady=5)
       
#         self.idade_label = ttk.Label(self, text="Idade:")
#         self.idade_label.grid(row=1, column=0, padx=10, pady=5)
       
#         self.idade_entry = ttk.Entry(self)
#         self.idade_entry.grid(row=1, column=1, padx=10, pady=5)
       
#         self.adicionar_button = ttk.Button(self, text="Adicionar")
#         self.adicionar_button.grid(row=2, column=0, columnspan=2, pady=10)
       
#         self.usuarios_listbox = tk.Listbox(self)
#         self.usuarios_listbox.grid(row=3, column=0, columnspan=2, padx=10, pady=5, sticky="nsew")
       
#         self.grid_rowconfigure(3, weight=1)
#         self.grid_columnconfigure(1, weight=1)

#     def get_nome(self):
#         return self.nome_entry.get()

#     def get_idade(self):
#         return self.idade_entry.get()

#     def adicionar_usuario_lista(self, usuario):
#         self.usuarios_listbox.insert(tk.END, f"id {usuario[0]} | {usuario[1]} ({usuario[2]} anos)")
#     def show_info(self):
#         messagebox.showinfo("Aviso!", "Os campos não podem estar vazios e a idade deve ser digito.")