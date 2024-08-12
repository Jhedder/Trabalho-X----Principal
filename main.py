import tkinter as tk
from PIL import Image, ImageTk
from controler.chefe_c import ChefeController


from controler.delete_c import DeleteController
from model.usuario_m import UsuarioModel
from view.chefeview_v import ChefeView
from view.delete_v import DeleteView
from view.menu_v import MenuView
from view.splash_v import SplashView
from view.escolha_chefe_v import EscolhaView
from controler.escolha_chefe_c import EscolhaController



class MainApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Megaman X5")
        self.escolha_chefe_v = EscolhaView
        self.splash_v = SplashView
        self.chefe_v = ChefeView
        self.usuario_model = UsuarioModel()
        self.menu_v = MenuView(self)
        self.switch_frame(SplashView)
   
    def switch_frame(self, frame_class):
        new_frame = frame_class(self)
        if frame_class ==  EscolhaView:
            EscolhaController(self,new_frame,self.usuario_model)
        elif frame_class == DeleteView:
            DeleteController(new_frame, self.usuario_model)
        
        elif frame_class == self.chefe_v :
            self.chefe_c = ChefeController(self,new_frame, self.usuario_model)
        else:
            print("algo deu errado switch_Frame")
        if hasattr(self, "current_frame"):
            self.current_frame.destroy()#fica aqui para apagar a visualização antiga....
        self.current_frame = new_frame
        #self.current_frame.pack(fill=tk.BOTH, expand=True)

if __name__ == "__main__":
    app = MainApp()
    app.mainloop()