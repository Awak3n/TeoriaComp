try:
	from tkinter import *
	from tkinter import ttk
	from PIL import Image as pImg, ImageTk
except:
    print("Este programa requer Python 3.x e as bibliotecas Python-Tk e Pillow")
    exit(0)

#Classe principal
class Application():

	#Construtor da classe, recebe a janela como parâmetro
	def __init__(self, root):
		self.initComponents()
		
	#Inicizalização dos componentes principais da janela
	def initComponents(self):
		root.title("Comparador de Programas 2000")	
		Label(root,text="Comparador de Programas Monolíticos",font=('Times',30)).grid(row=0,column=0,columnspan=2)
		Message(root,text="Insira dois programa monolíticos no formato de instruções rolutadas e pressione prosseguir para compará-los.").grid(row=1,column=0,columnspan=2)
		self.ltb = Text(root,width = 40, height = 20)
		self.ltb.grid(row=2,column=0,sticky=E)
		self.rtb = Text(root,width = 40, height = 20)
		self.rtb.grid(row=2,column=1,sticky=E)
		self.btn = Button(root,text="Prosseguir",command=self.action)
		self.btn.bind('<Button-3>',self.easterEgg)
		self.btn.grid(row=3,column=0,columnspan=2,sticky=N)

	#Realiza a ação do botão pressionado
	def action(self):
		print("Primeiro programa:\n" + self.ltb.get('1.0','end-1c'))
		print("Segundo programa:\n" + self.rtb.get('1.0','end-1c'))

	#Código secreto - shh!
	def easterEgg(self,event):
		img = ImageTk.PhotoImage(pImg.open("vove.jpeg"))
		lbl = Label(root,image=img)
		lbl.image = img
		lbl.grid(row=1,column=0,columnspan=2,rowspan=2)

#inicialização do programa
if __name__ == '__main__':
	root = Tk()
	app = Application(root)
	root.mainloop()