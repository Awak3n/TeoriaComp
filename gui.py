try:
	import logic
	from tkinter import *
	from tkinter import ttk
	from tkinter import messagebox
except:
    print("Este programa requer Python 3.x e a biblioteca Python-Tk")
    exit(0)

#Classe principal
class Application():

	#Construtor da classe, recebe a janela como parâmetro
	def __init__(self, root):
		self.initComponents()
		
	def initComponents(self):
		'''Inicizalização dos componentes principais da janela'''
		root.title("Comparador de Programas 2000")	
		Label(root,text="Comparador de Programas Monolíticos",font=('Times',30)).grid(row=0,column=0,columnspan=2,sticky=W+E)
		Label(root,text="Insira dois programa monolíticos no formato de instruções rolutadas \n e pressione prosseguir para compará-los.").grid(row=1,column=0,columnspan=2,sticky=W+E)
		self.ltb = Text(root,width = 40, height = 20)
		self.ltb.grid(row=2,column=0,sticky=E)
		self.rtb = Text(root,width = 40, height = 20)
		self.rtb.grid(row=2,column=1,sticky=E)
		self.btn = Button(root, text="Prosseguir")
		self.btn.bind("<Button-1>",self.action_n1)
		self.btn.grid(row=3,column=0,columnspan=2,sticky=N)

	def action_n1(self,event):    
		'''Conversão dos programas para o formato composto'''
		self.line_p1 = self.ltb.get('1.0', 'end-1c')
		self.line_p2 = self.rtb.get('1.0', 'end-1c')
		if(self.line_p1 is "" or self.line_p2 is ""):
			messagebox.showinfo(icon="error",title='Erro',message="Um dos programas está vazio.")
		else:
			print("Primeiro programa:\n" + self.line_p1)
			self.line_p1c = logic.translation(self.line_p1)
			print("Segundo programa:\n" + self.line_p2)
			self.line_p2c = logic.translation(self.line_p2)
			if (len(self.line_p1c) != 0 or len(self.line_p2c) != 0):
				print("yay")
				self.btn.unbind_all
				self.btn.bind("<Button-1>", self.action_n2)
				self.ltb.delete('1.0','end')
				self.ltb.insert('1.0', self.textFormat(self.line_p1c))
				self.ltb.configure(state=DISABLED)
				self.rtb.delete('1.0','end')
				self.rtb.insert('1.0', self.textFormat(self.line_p2c))
				self.rtb.configure(state=DISABLED)
				self.btn.focus_get
				
				
	def action_n2(self,event):
		'''Comparação do programa'''
		print("nada aqui")

	def textFormat(self,array):
		text = ''
		for line in array:
			text += line + '\n'
		return text

#inicialização do programa
if __name__ == '__main__':
	root = Tk()
	app = Application(root)
	root.mainloop()