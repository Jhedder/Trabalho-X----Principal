from model.usuario_m import UsuarioModel
from view.chefeview_v import ChefeView
import tkinter as tk
from controler.chefe_c import ChefeController


class EscolhaController:
    def __init__(self,parent, view, model:UsuarioModel):
        self.parent= parent
        self.view = view
        self.model = model
        self.view.escolher_button.config(command=self.selecionar_chefe)
        self.carregar_chefes()

    def selecionar_chefe(self):
        id = self.view.get_id()
        self.parent.menu_v.pack_forget()
        self.parent.switch_frame(ChefeView)
        self.parent.chefe_c.get_chefe_id(id)
        self.parent.chefe_c.carregar_view()
        self.parent.title("Escolha Chefes - Megaman X5")
       
        

    def carregar_chefes(self):
        chefes = self.model.carregar_chefes()#retorna uma lista de tuplas
        for chefe in chefes:
            self.view.adicionar_chefe_lista(chefe)