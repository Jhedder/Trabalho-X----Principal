import tkinter as tk
from PIL import Image, ImageTk

def button_click():
    print("Botão Clicado.")

def create_gradient(canvas, x, y, width, height, start_color="#ffffff", end_color="#000000"):
    # Cria um gradiente de cor no canvas
    for i in range(height):
        # Calcula a cor atual no gradiente
        r = int(start_color[1:3], 16) * (height - i) // height + int(end_color[1:3], 16) * i // height
        g = int(start_color[3:5], 16) * (height - i) // height + int(end_color[3:5], 16) * i // height
        b = int(start_color[5:7], 16) * (height - i) // height + int(end_color[5:7], 16) * i // height
        color = f"#{r:02x}{g:02x}{b:02x}"
        # Desenha uma linha horizontal no canvas com a cor calculada
        canvas.create_line(x, y + i, x + width, y + i, fill=color, width=1)

root = tk.Tk()
root.title('Burn Dinorex')

# Impede que a janela seja redimensionada manualmente
root.resizable(False, False)

# Cria um Canvas para o fundo vermelho
canvas = tk.Canvas(root, width=500, height=600, bg="red")
canvas.pack()

# Abre a imagem usando PIL (Pillow)
image = Image.open("C:/Users/182400232/Documents/Trabalho/Trabalho X  - Principal/midia/imagens/BurnDinorex.jpg")

# Redimensiona a imagem para uma resolução menor
image = image.resize((400, 400), Image.LANCZOS)

# Converte a imagem PIL para um objeto PhotoImage
photo = ImageTk.PhotoImage(image)

# Cria um Label para exibir a imagem
label = tk.Label(root, image=photo)
label.place(x=50, y=100)  # Posiciona o Label na janela

# Cria um Label com a descrição do Burn Dinorex
descricao_label = tk.Label(root, text="Descrição do Burn Dinorex do Megaman X5", fg="white", bg="red")
descricao_label.place(x=50, y=80)  # Posiciona o Label acima da imagem

# Cria um botão
button = tk.Button(root, text="Atualizar Chefe", command=button_click)
button.place(x=225, y=520)  # Posiciona o botão na janela

root.mainloop()