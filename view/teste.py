# import tkinter as tk
# from PIL import Image, ImageTk

# # Crie a janela principal
# root = tk.Tk()


# # Caminho da imagem
# image_path = "C:/Users/182400232/Documents/Projetos-Python1/Trabalho X/Imagens/maxresdefault.jpg"

# # Carregue a imagem usando Pillow
# imagem = Image.open(image_path)
# imagem = ImageTk.PhotoImage(imagem)

# # Crie um widget Label para exibir a imagem
# w = tk.Label(root, image=imagem)
# w.imagem = imagem  # Mantenha uma referência para evitar coleta de lixo
# w.pack()

# # Inicie o loop do GUI



# # Função para carregar a imagem
#     def load_image():
#     # Carrega a imagem usando Pillow
#         image = Image.open("C:/Users/182400232/Documents/Projetos-Python1/Trabalho X/Imagens/maxresdefault.jpg")#tem que dar o caminho da imagem
#     # Redimensiona a imagem conforme necessário
#         image = image.resize((400, 400), Image.LANCZOS)
#     # Converte a imagem para um formato que o tkinter possa exibir
#         photo = ImageTk.PhotoImage(image)
#         return photo

# # Cria a janela principal
#     root = tk.Tk()

# # Carrega a imagem
#     image = load_image()

# # Cria a label com a imagem e o texto
#     label = tk.Label(root, image=image, compound="left")
#     label.pack()

# # Executa o loop principal do tkinter
#     root.mainloop()

#     def show_info(self):
#         messagebox.showinfo("Aviso!", "Os campos não podem estar vazios e a idade deve ser digito.")



# from model.usuario_m import UsuarioModel
# from view.user_v import UsuarioView
# import tkinter as tk


# class UsuarioController:
#     def __init__(self, view:UsuarioView, model:UsuarioModel):
#         self.view = view
#         self.model = model
#         self.view.adicionar_button.config(command=self.adicionar_chefe)
#         self.carregar_chefe()

#     def adicionar_chefe(self):
#         nome = self.view.get_nome()
#         fase = self.view.get_fase()
#         poder = self.view.get_poder()
#         if nome and fase and poder.isdigit():
#             self.model.inserir_chefe(nome, fase, poder)
#             self.view.nome_entry.delete(0, tk.END)
#             self.view.idade_entry.delete(0, tk.END)
#             self.view.usuarios_listbox.delete(0, tk.END)
#             self.carregar_chefe()

#     def carregar_chefe(self):
#         usuarios = self.model.selecionar_chefes()#retorna uma lista de tuplas
#         for usuario in usuarios:
#             self.view.adicionar_usuario_lista(usuario)




# import tkinter as tk
# from tkinter import ttk
# from PIL import Image, ImageTk

# class UsuarioView(tk.Frame):
  
#     def __init__(self, parent):
#         super().__init__(parent)
#         self.parent = parent
#         self.pack(fill=tk.BOTH, expand=True)
#         self.master.geometry('600x600')
#         self.create_background()
#         self.create_widgets()

#     def load_image(self):
#         image = Image.open("C:/Users/182400232/Documents/Projetos-Python1/Trabalho X/Imagens/maxresdefault.jpg")
#         image = image.resize((780, 600), Image.LANCZOS)
#         photo = ImageTk.PhotoImage(image)
#         return photo

#     def create_background(self):
#         # Cria um Label para exibir a imagem como plano de fundo
#         self.background_image = self.load_image()
#         self.background_label = tk.Label(self, image=self.background_image)
#         self.background_label.place(x=0, y=0, relwidth=1, relheight=1)  # Posiciona o Label para ocupar toda a área do Frame

#     def button_click(self):
#         print("Botão clicado!")

#     def create_widgets(self):
#         # Cria um Frame para centralizar o botão na tela
#         frame_center = tk.Frame(self)
#         frame_center.place(relx=0.5, rely=0.9, anchor=tk.S)

#         # Cria o botão dentro do Frame centralizado
#         button = tk.Button(frame_center, text="Iniciar O Jogo", command=self.button_click)
#         button.pack()

#     def create_widgets(self):
  
#         self.novo_jogo = ttk.Button(self, text="Novo Jogo")
#         self.novo_jogo.grid(row=0, column=0, padx=10, pady=5)
       
        
       
#         self.carregar_jogo = ttk.Button(self, text="Carregar Jogo")
#         self.carregar_jogo.grid(row=1, column=0, padx=10, pady=5)
       
#         self.usuarios_listbox = tk.Listbox(self)
#         self.usuarios_listbox.grid(row=3, column=0, columnspan=2, padx=10, pady=5, sticky="nsew")
       
#         self.grid_rowconfigure(3, weight=1)
#         self.grid_columnconfigure(1, weight=1)

#     def get_novo_jogo(self):
#         return self.novo_jogo.get()

#     def get_carregar_jogo(self):
#         return self.carregar_jogo.get()

#     def adicionar_chefes_lista(self, chefe):
#         self.usuarios_listbox.insert(tk.END, f"id {chefe[0]} | {chefe[1]} ({chefe[2]})")



# def load_image(self):
#         image = Image.open("C:/Users/182400232/Documents/Projetos-Python1/Trabalho X/Imagens/maxresdefault.jpg")
#         image = image.resize((780, 600), Image.LANCZOS)
#         photo = ImageTk.PhotoImage(image)
#         return photo

#     def create_background(self):
#         # Cria um Label para exibir a imagem como plano de fundo
#         self.background_image = self.load_image()
#         self.background_label = tk.Label(self, image=self.background_image)
#         self.background_label.place(x=0, y=0, relwidth=1, relheight=1)  # Posiciona o Label para ocupar toda a área do Frame


#     def button_click(self):
#         print("Botão clicado!")

#     def create_widgets(self):
#         # Cria um Frame para centralizar o botão na tela
#         frame_center = tk.Frame(self)
#         frame_center.place(relx=0.5, rely=0.9, anchor=tk.S)

#         # Cria o botão dentro do Frame centralizado
#         button = tk.Button(frame_center, text="Iniciar O Jogo", command=self.button_click)
#         button.pack()



# def create_widgets(self):
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
#             return self.nome_entry.get()

#     def get_idade(self):
#             return self.idade_entry.get()

#     def adicionar_usuario_lista(self, usuario):
#             self.usuarios_listbox.insert(tk.END, f"id {usuario[0]} | {usuario[1]} ({usuario[2]} anos)")
#     def show_info(self):
#             messagebox.showinfo("Aviso!", "Os campos não podem estar vazios e a idade deve ser digito.")



# import tkinter as tk
# from tkinter import ttk
# from tkinter import messagebox
# from PIL import Image, ImageTk


# class EscolhaView(tk.Frame):
#     def __init__(self, parent):
#         super().__init__(parent)
#         self.pack(fill=tk.BOTH, expand=True)
#         self.create_widgets()
#         self.master.geometry("700x980")
#         self.create_widgets()
    

#     def create_widgets(self):

#         self.id_label = ttk.Label(self, text="ID:")
#         self.id_label.grid(row=0, column=0, padx=10, pady=10)

#         self.id_entry = ttk.Entry(self)
#         self.id_entry.grid(row=0, column=1, padx=10, pady=10)
       
#         self.adicionar_button = ttk.Button(self, text="Escolher")
#         self.adicionar_button.grid(row=3, column=0, columnspan=2, pady=10)
       
#         self.chefes_listbox = tk.Listbox(self)
#         self.chefes_listbox.grid(row=4, column=0, columnspan=2, padx=10, pady=5, sticky="nsew")
       
#         self.grid_rowconfigure(3, weight=1)
#         self.grid_columnconfigure(1, weight=1)
        
#     def get_id(self):
#         id = self.id_entry.get()
#         return id

#     def adicionar_chefe_lista(self, chefe):
#         self.chefes_listbox.insert(tk.END, f"id {chefe[0]} | nome | {chefe[1]} fase | {chefe[2]} poder | {chefe[3]}")
#     def show_info(self):
#         messagebox.showinfo("Os campos não podem estar vazios e o id deve ser digito.")
