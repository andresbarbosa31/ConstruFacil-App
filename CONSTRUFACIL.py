from kivymd.app import MDApp
from kivy.lang import Builder 
from kivymd.uix.screen import MDScreen
from kivymd.uix.screenmanager import ScreenManager
from kivymd.uix.button import MDFloatingActionButtonSpeedDial
from kivy.uix.button import Button
from kivy.core.window import Window as windows_pantalla
from kivy.uix.label import Label
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDFlatButton

class Gerencial(ScreenManager):
    pass
class Principal(MDScreen):
    pass
class Cadastro (MDScreen):
    def limpar(self):
        self.ids.caixa_texto1.text=''
        self.ids.caixa_texto2.text=''
        self.ids.caixa_texto3.text=''
    def cadastrar(self):
        usuario=self.ids.caixa_texto2.text
        telefone=self.ids.caixa_texto1.text
        email=self.ids.caixa_texto3.text
        arqu_cliente=open("cliente.txt","a")
        arqu_cliente.write('Nome:' + usuario + ', E-mail:' + email + ', Telefone: ' + telefone)
        arqu_cliente.close()
        self.ids.resposta.text='Cadastro realizado com sucesso!'

class Consulta(MDScreen): 
    def limpar(self):
        self.ids.caixa_texto1.text=''
    def buscar(self):
        cliente=self.ids.caixa_texto1.text=''
        Cadastro.arqu_cliente=open("cliente.txt")
        ler = Cadastro.arqu_cliente.read()
        Cadastro.arqu_cliente.close()
        self.ids.resposta.text= ler
        
class Agua(MDScreen):   
    def limpar(self):
        self.ids.caixa_texto1.text=''
        self.ids.caixa_texto2.text=''
        self.ids.caixa_texto3.text=''
    def calcular(self):
        self.dialog = MDDialog(title='ERRO', text='Digite outra vez!', buttons=[MDFlatButton(text="Ok", 
                    on_release=self.liberar)])
        try:  
            altura=float(self.ids.caixa_texto1.text)
            largura=float(self.ids.caixa_texto2.text)
            comprimento=float(self.ids.caixa_texto3.text)
            volume=altura*largura*comprimento
            litros=volume*1000
            self.ids.resposta.text='        {:0.0f} M³\n\n{:0.2f} Litros'.format(volume,litros)
        except ValueError:
            self.dialog.open()
    def liberar(self,obj):
        self.dialog.dismiss() 
class Reajunte (MDScreen):
    def limpar(self):
        self.ids.caixa_texto1.text=''
        self.ids.caixa_texto2.text=''
        self.ids.caixa_texto3.text=''
    def calcular (self):
        self.dialog = MDDialog(title='ERRO', text='Digite outra vez!', buttons=[MDFlatButton(text="Ok", 
            on_release=self.liberar)])
        try:  
            largura=float(self.ids.caixa_texto1.text)
            comprimento=float(self.ids.caixa_texto2.text)
            metragem_ceramica=float(self.ids.caixa_texto3.text)

            calc_base_epoxi=((comprimento*10+largura*10)*3*1*1.58)/((comprimento*10)*(largura*10))
            reajunte_epoxi=calc_base_epoxi*metragem_ceramica

            calc_base_acrilico=((comprimento*10+largura*10)*3*1*1.70)/((comprimento*10)*(largura*10))
            reajunte_acrilico=calc_base_acrilico*metragem_ceramica

            calc_base_cimenticio=((comprimento*10+largura*10)*3*1*1.75)/((comprimento*10)*(largura*10))
            reajunte_cimenticio=calc_base_cimenticio*metragem_ceramica

            self.ids.resposta.text='Epoxi: {:0.2f} Kg\n\nAcrilico: {:0.2f} Kg\n\nCimenticio: {:0.2f} Kg'.format(reajunte_epoxi,reajunte_acrilico,reajunte_cimenticio)
        except ValueError:
            self.dialog.open()
    def liberar(self,obj):
        self.dialog.dismiss() 
class Ceramica(MDScreen):
    def limpar(self):
        self.ids.caixa_texto1.text=''
        self.ids.caixa_texto2.text=''
    def calcular(self):
        self.dialog = MDDialog(title='ERRO', text='Digite outra vez!', buttons=[MDFlatButton(text="Ok", 
                    on_release=self.liberar)])
        try:  
            altura=float(self.ids.caixa_texto1.text)
            largura=float(self.ids.caixa_texto2.text)
            area=altura*largura
        
            self.ids.resposta.text='Normal: {:0.2f} M²\n\nDiagonal: {:0.2f} M²'.format(area+(area*0.1),area+(area*0.2))
        except ValueError:
            self.dialog.open()
    def liberar(self,obj):
        self.dialog.dismiss() 
        
class Tijolos(MDScreen):
    def limpar(self):
        self.ids.caixa_texto1.text=''
        self.ids.caixa_texto2.text=''
    def calcular(self):
        self.dialog = MDDialog(title='ERRO', text='Digite outra vez!', buttons=[MDFlatButton(text="Ok", 
                    on_release=self.liberar)])
        try:  
            altura=float(self.ids.caixa_texto1.text)
            largura=float(self.ids.caixa_texto2.text)
            area=altura*largura
            
            furos_4=area*10000/276
            furos_6=area*10000/266
            furos_8=area*10000/361
            furos_9=area*10000/456
            
            self.ids.resposta.text='4 Furos: {:0.2f}\n\n6 Furos: {:0.2f}\n\n'\
            '8 Furos: {:0.2f}\n\n9 Furos: {:0.2f}\n\nÁrea Total:{:0.2f} M²'.format(furos_4,furos_6,furos_8,furos_9,area)
        except ValueError:
            self.dialog.open()
    def liberar(self,obj):
        self.dialog.dismiss() 

class Servico(MDScreen):    
    def limpar(self):
        self.ids.caixa_texto1.text=''
        self.ids.caixa_texto2.text=''
        self.ids.caixa_texto3.text=''
    def calcular(self):
        self.dialog = MDDialog(title='ERRO', text='Dados Invalidos!', buttons=[MDFlatButton(text="Ok", 
                    on_release=self.liberar)])
        try:  
            valor_extra=float(self.ids.caixa_texto1.text)
            metragem=float(self.ids.caixa_texto2.text)
            valor_metro=float(self.ids.caixa_texto3.text)
            
            if valor_extra!=1:
                total=(valor_metro*metragem)+valor_extra
            else:
                total=valor_metro*metragem
            self.ids.resposta.text='R$ {:0.2f}'.format(total)
        except ValueError:
            self.dialog.open()
            
    def liberar(self,obj):
        self.dialog.dismiss()

class TelaPrincipal(MDApp):  
    def build(self):
        self.theme_cls.theme_style = "Light"
        self.theme_cls.primary_palette = "Blue"
        self.theme_cls.theme_style_switch_animation = True
        self.theme_cls.theme_style_switch_animation_duration = 1
        self.title ='ConstruFacil - Versão 1.0'         
        return Builder.load_file('INTERFACE.kv')
            
if __name__ == '__main__':
   TelaPrincipal().run()