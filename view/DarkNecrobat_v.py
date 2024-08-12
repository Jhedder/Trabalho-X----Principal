import tkinter as tk
from PIL import Image, ImageTk

def create_gradient_background(canvas, width, height):
    # Definir cores para o gradiente
    color1 = '#800080'  # Tomato
    color2 = '#800080'  # DarkRed

    # Criar gradiente vertical no canvas
    num_rectangles = 100
    for i in range(num_rectangles):
        # Interpolar entre color1 e color2
        color = '#{:02x}{:02x}{:02x}'.format(
            int((num_rectangles - i) * int(color1[1:3], 16) + i * int(color2[1:3], 16)) // num_rectangles,
            int((num_rectangles - i) * int(color1[3:5], 16) + i * int(color2[3:5], 16)) // num_rectangles,
            int((num_rectangles - i) * int(color1[5:], 16) + i * int(color2[5:], 16)) // num_rectangles
        )
        canvas.create_rectangle(0, i * (height // num_rectangles), width, (i + 1) * (height // num_rectangles), fill=color, outline="")

# Função para centralizar a janela na tela
def center_window(window, width, height):
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    x = (screen_width // 2) - (width // 2)
    y = (screen_height // 2) - (height // 2)
    window.geometry(f'{width}x{height}+{x}+{y}')

# Função para atualizar a imagem (substitua com sua lógica de atualização)
def atualizar_imagem():
    # Aqui você pode implementar a lógica para atualizar a imagem
    # Por enquanto, vou manter a mesma imagem apenas para demonstração
    pass

# Criar a janela principal
root = tk.Tk()
root.title("Dark Necrobat - Mega Man X5")
root.resizable(False, False)

# Aumentar o tamanho mínimo da janela
min_width, min_height = 600, 800
root.minsize(min_width, min_height)

# Criar um canvas para o fundo com gradiente
canvas = tk.Canvas(root, width=min_width, height=min_height)
canvas.pack(fill=tk.BOTH, expand=True)

# Criar o fundo com gradiente
create_gradient_background(canvas, min_width, min_height)

# Carregar e redimensionar a imagem do Magma Dragoon
image_path = "C:/Users/182400232/Documents/Trabalho/Trabalho X  - Principal/midia/imagens/Dark Necrobat.jpg"  # Coloque o caminho da sua imagem aqui
original_image = Image.open(image_path)
resized_image = original_image.resize((400, 400))
photo = ImageTk.PhotoImage(resized_image)

# Criar um label para exibir a imagem
image_label = tk.Label(root, image=photo, bg='#8B0000')  # Fundo vermelho escuro para o label da imagem
image_label.place(x=100, y=100)  # Posição relativa ao canvas

# Texto com informações sobre o Magma Dragoon
info_text = """
Dark Necrobat (ダーク・ネクロバットDāku Nekurobatto ) , também
conhecido como Dark Dizzy , [2] é um Reploid baseado em morcego
vampiro de Mega Man X5 . Ele residia em um planetário em algum lugar
do Egito e estava de posse do Tanque de Combustível necessário para
tornar o Ônibus Espacial operável.
"""

# Criar um label para exibir o texto
text_label = tk.Label(root, text=info_text, justify=tk.LEFT, padx=10, pady=10, bg='#800080', fg='white',
font=('Helvetica', 12))  # Fundo vermelho escuro e texto branco
text_label.place(x=25, y=520)  # Posição relativa ao canvas

# Criar um botão para atualizar a imagem
atualizar_button = tk.Button(root, text="Atualizar Chefe", command=atualizar_imagem)
atualizar_button.place(x=250, y=700)  # Posição relativa ao canvas

# Centralizar a janela na tela
center_window(root, min_width, min_height)

# Rodar o loop principal
root.mainloop()
