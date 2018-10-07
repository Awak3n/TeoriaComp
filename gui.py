try:
	import logic
	from tkinter import *
	from tkinter import ttk
	from tkinter import messagebox
	from tkinter import filedialog
except:
	print("Este programa requer Python 3.x e a biblioteca Python-Tk")
	exit(0)

class Application():
	'''Classe principal'''

	def __init__(self, root):
		'''Construtor da classe, recebe a janela como parâmetro'''
		self.initComponents()
		self.initMenu()
		
	def initComponents(self):
		'''Inicizalização dos componentes principais da janela'''
		root.title("Comparador de Programas 2000")
		Label(root,text="Comparador de Programas Monolíticos",font=('Times',30)).grid(row=0,column=0,columnspan=2,sticky=W+E)
		Label(root, text="Insira dois programas monolíticos no formato de instruções rolutadas \n e pressione prosseguir para compará-los.").grid(row=1, column=0, columnspan=2, sticky=W + E)
		Label(root, text="Passo atual ", font=('Verdana', 20), fg="RED").grid(row=2, column=0, columnspan=2)
		self.ltxt= ["0 - Inserção dos Programas","1 - Definição das Instruções Rotuladas Compostas","2 - Definição da Cadeida de Conjuntos Finitos","3 - Simplificação de Ciclos","4 - Comparação dos Programas"]
		self.lbl = Label(root,text=self.ltxt[0] , font=('Verdana',15), fg="RED")
		self.lbl.grid(row=3, column=0,columnspan=2)
		self.ltb = Text(root,width = 40, height = 20)
		self.ltb.grid(row=4, column=0, sticky=E)
		self.ltb.insert("1.0", "Se t1 vá_para 2 senão vá_para 0\nSe t2 vá_para 0 senão vá_para 3\nFaça V vá_para 4\nFaça W vá_para 2")
		self.rtb = Text(root,width = 40, height = 20)
		self.rtb.grid(row=4, column=1, sticky=E)
		self.rtb.insert("1.0","Se t1 vá_para 2 senão vá_para 0\nSe t2 vá_para 3 senão vá_para 0\nSe t3 vá_para 0 senão vá_para 4\nFaça V vá_para 5\nFaça W vá_para 3")
		self.btn = Button(root, text="Prosseguir")
		self.btn.bind("<Button-1>",self.action_n1)
		self.btn.grid(row=5,column=1,sticky=N)
		self.retbtn = Button(root, text="Retroceder", state=DISABLED)
		self.retbtn.bind("<Button-1>",self.retaction_n1)
		self.retbtn.grid(row=5,column=0,sticky=N)
	
	def initMenu(self):
		menu = Menu(root)
		file = Menu(menu, tearoff=0)
		file.add_command(label="Abrir programas", command=self.loadProgram)
		file.add_command(label="Sair", command=root.quit)
		menu.add_cascade(label="Arquivo", menu=file)
		menu.add_command(label="Sobre",command=self.showInfo)
		root.config(menu=menu)

	def showInfo(self):
		messagebox.showinfo(icon="info", title='Sobre', message="Comparador de programas monolíticos feito por:\n\n#Êndril Castilho da Silveira\n#Leonardo Pellegrini Silva\n\nMatrícula: 78226 e 78159")

	def loadProgram(self):
		'''Carrega os programas do disco'''
		try:
			messagebox.showinfo(icon="info",title='Abrir',message="Selecione o arquivo do primeiro programa.")
			p1 = open(filedialog.askopenfilename(title="Programa 1"),'r')
			messagebox.showinfo(icon="info",title='Abrir',message="Selecione o arquivo do segundo programa.")
			p2 = open(filedialog.askopenfilename(title="Programa 2"), 'r')
			self.backInBlack()
			self.ltb.insert('1.0', p1.read())
			self.rtb.insert('1.0', p2.read())
		except:
			messagebox.showinfo(icon="error",title='Erro',message="Formato de arquivo inválido.")

	def backInBlack(self):
		'''Retorna para o estado inicial do programa'''
		self.btn.unbind_all
		self.btn.bind("<Button-1>", self.action_n1)
		self.ltb.configure(state=NORMAL)
		self.ltb.delete('1.0','end')
		self.rtb.configure(state=NORMAL)
		self.rtb.delete('1.0', 'end')
		self.retbtn.unbind_all
		self.retbtn.configure(state=DISABLED)
		self.lbl.configure(text=self.ltxt[0])

	def action_n1(self,event):    
		'''Passo 1 - Conversão dos programas para o formato composto'''
		self.line_p1 = self.ltb.get('1.0', 'end-1c')
		self.line_p2 = self.rtb.get('1.0', 'end-1c')
		if(len(self.line_p1) == 0 or len(self.line_p2) == 0):
			messagebox.showinfo(icon="error",title='Erro',message="Um dos programas está vazio.")
		else:
			try:
				self.line_p1c = logic.translation(self.line_p1)
				self.line_p2c = logic.translation(self.line_p2)
				if (len(self.line_p1c) != 0 or len(self.line_p2c) != 0):
					self.line_p2c = logic.numCorrection(self.line_p2c,len(self.line_p1c))
				self.btn.unbind_all
				self.btn.bind("<Button-1>", self.action_n2)
				self.ltb.delete('1.0','end')
				self.ltb.insert('1.0', logic.textFormat(self.line_p1c))
				self.ltb.configure(state=DISABLED)
				self.rtb.delete('1.0','end')
				self.rtb.insert('1.0', logic.textFormat(self.line_p2c))
				self.rtb.configure(state=DISABLED)
				self.retbtn.configure(state=NORMAL)
				self.retbtn.bind("<Button-1>",self.retaction_n1)
				self.lbl.configure(text=self.ltxt[1])
			except:
				messagebox.showinfo(icon="warning",title='Aviso',message="Por favor, preencha os campos corretamente.")
				
	def retaction_n1(self,event):
		'''Retrocede o estado do programa para o passo 1'''
		self.btn.unbind_all
		self.btn.bind("<Button-1>", self.action_n1)
		self.ltb.configure(state=NORMAL)
		self.ltb.delete('1.0','end')
		self.ltb.insert('1.0', self.line_p1)
		self.rtb.configure(state=NORMAL)
		self.rtb.delete('1.0','end')
		self.rtb.insert('1.0', self.line_p2)
		self.retbtn.unbind_all
		self.retbtn.configure(state=DISABLED)
		self.lbl.configure(text=self.ltxt[0])
		
	def action_n2(self,event):
		'''Passo 2 - Comparação do programa'''
		self.showseq_p1, self.seq_p1 = logic.finiteArrayDefinition(self.line_p1c, 0)
		self.showseq_p2, self.seq_p2 = logic.finiteArrayDefinition(self.line_p2c, int(len(self.line_p1c) / 5))
		self.btn.unbind_all
		self.btn.bind("<Button-1>", self.action_n3)
		self.ltb.configure(state=NORMAL)
		self.ltb.insert('end', "\n"+self.showseq_p1)
		self.ltb.configure(state=DISABLED)
		self.rtb.configure(state=NORMAL)
		self.rtb.insert('end', "\n"+self.showseq_p2)
		self.rtb.configure(state=DISABLED)
		self.retbtn.unbind_all
		self.retbtn.bind("<Button-1>",self.retaction_n2)
		self.lbl.configure(text=self.ltxt[2])
		
	def retaction_n2(self,event):
		'''Retrocede o estado o programa para o passo 2'''
		self.btn.unbind_all
		self.btn.bind("<Button-1>", self.action_n2)
		self.ltb.configure(state=NORMAL)
		self.ltb.delete('1.0','end')
		self.ltb.insert('1.0', logic.textFormat(self.line_p1c))
		self.ltb.configure(state=DISABLED)
		self.rtb.configure(state=NORMAL)
		self.rtb.delete('1.0','end')
		self.rtb.insert('1.0', logic.textFormat(self.line_p2c))
		self.rtb.configure(state=DISABLED)
		self.retbtn.unbind_all
		self.retbtn.bind("<Button-1>", self.retaction_n1)
		self.lbl.configure(text=self.ltxt[1])

	def action_n3(self,event):
		'''Action 3'''
		print("aqui não tem ninguém")

	def retaction_n3(self,event):
		'''Return action 3'''
		print("não tem pão velho")

	def action_n4(self,event):
		'''Action 3'''
		print("nope")

	def retaction_n4(self,event):
		'''Return action 4'''
		print("nada")

#inicialização do programa
if __name__ == '__main__':
	root = Tk()
	app = Application(root)
	root.mainloop()