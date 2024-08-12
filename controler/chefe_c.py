from view.menu_v import MenuView

class ChefeController:
    def __init__(self, parent, view, model):
        self.parent = parent
        self.view = view
        self.model = model
        self.view.create_widgets()
        self.view.escolher_button.config(command=self.selecionar_chefe)
    def selecionar_chefe(self):
        #self.parent.menu_v = MenuView(self.parent)
        self.parent.menu_v.pack()
        self.parent.minsize(700, 980)
        self.parent.resizable(True, True)
        self.parent.geometry("700x980")
        self.parent.switch_frame(self.parent.escolha_chefe_v)
      

    def retornar_url_img_chefe(self):
        chefe = self.model.carregar_chefe(self.id_chefe)
        self.view.image_path = chefe[0][4]
        self.view.update_image()

    def retornar_descricao(self):
        chefe = self.model.carregar_chefe(self.id_chefe)
        return chefe[0][5]
        

    def get_chefe_id(self,id):
        self.id_chefe = id

    def carregar_view(self):
        self.retornar_url_img_chefe()
        descricao = self.retornar_descricao()
        self.view.update_info(descricao)
