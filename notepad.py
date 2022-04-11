import tkinter 
import os 
from tkinter import * 
from tkinter.messagebox import * 
from tkinter.filedialog import * 

class Notepad :
	root = Tk()

	# setting default width and height of the notepad screen
	WIDTH  , HEIGHT = 300 , 300
	TextArea = Text(root)
	MenuBar = Menu(root)
	FileMenu = Menu(MenuBar , tearoff = 0)
	EditMenu = Menu(MenuBar , tearoff = 0)
	HelpMenu = Menu(MenuBar , tearoff = 0)

	ScrollBar = Scrollbar(TextArea)
	file = None 

	def __init__(self , **kwargs):
		try :
			self.root.wm_iconbitmap("Notepad.ico")
		except :
			pass 

		try :
			self.WIDTH = kwargs['width']
			self.HEIGHT = kwargs['height']

		except KeyError :
			pass 


		# set the window text 
		self.root.title("Untitled - Notepad")

		# center the window
		screenWidth = self.root.winfo_screenwidth()
		screenHeight = self.root.winfo_screenheight()	

		# code for aligning to left and right
		left = screenWidth/2 - self.WIDTH/2

		# code for aligning to up and down 
		up = screenHeight/2 - self.HEIGHT/2

		self.root.geometry(f'{self.WIDTH}x{self.HEIGHT}+{int(left)}+{int(up)}')

		# to make teh text area auto resizable
		self.root.grid_rowconfigure(0, weight=1)
		self.root.grid_columnconfigure(0, weight=1)

		# add controls 
		self.TextArea.grid(sticky = N + E + S + W)

		# to open neww file 
		self.FileMenu.add_command(label = "New" , command = self.newFile)

		# to open an already existing file 
		self.FileMenu.add_command(label = "Open" , command = self.openFile)

		# to save current file
		self.FileMenu.add_command(label = "Save" , command = self.saveFile)

		# to create a line in the dialog 
		self.FileMenu.add_separator()
		self.FileMenu.add_command(label = "Exit" , command = self.quitApplication )

		self.MenuBar.add_cascade(label = "File" , menu = self.FileMenu)

		# adding teh features of cut copy and paste 
		self.EditMenu.add_command(label = "Cut" , command = self.cut)
		self.EditMenu.add_command(label = "Copy" , command = self.copy)
		self.EditMenu.add_command(label = "Paste" , command = self.paste)

		self.MenuBar.add_cascade(label = "Edit", menu = self.EditMenu)

		# adding help and feature as well

		self.HelpMenu.add_command(label = "About Notepad" , command = self.showAbout)

		self.MenuBar.add_cascade(label = "Help" , menu = self.HelpMenu)

		# adding few keyboard shortcuts in the notepad 
		self.root.bind('<Control-o>' , self.openFile)
		self.root.bind('<Control-s>' , self.saveFile)
		self.root.bind('<Control-n>' , self.newFile)
		
		# adding the menu bar and the scroll bar 
		self.root.config(menu = self.MenuBar)
		self.ScrollBar.pack(side = RIGHT , fill = Y)

	def quitApplication(self):
		self.root.destory()

	def showAbout(self):
		showinfo("Notepad" , "Gaurav Negi")

	def openFile(self , event):
		self.file = askopenfilename(defaultextension = ".txt" , filetypes = [("All Files" , "*.*") , ("Text Documents" , "*.txt*")])

		if self.file == "" :
			self.file = None 

		else :

			self.root.title(os.path.basename(self.file) + ' - Notepad')
			self.TextArea.delete(1.0 , END)
			file = open(self.file , "r")
			self.TextArea.insert(1.0 , file.read())

			file.close()

	def newFile(self , event):
		self.root.title("Untitled - Notepad")
		self.file = None 
		self.TextArea.delete(1.0 , END)

	def saveFile(self , event):
		if self.file == None :
			self.file = asksaveasfilename(initialfile = 'Untitled.txt' , defaultextension = '.txt' , filetypes = [("All Files" , "*.*") , ("Text Documents" , "*.txt")])

			if self.file == "":
				self.file = None 

			else :
				# trying to save the file 
				file = open(self.file , "w")
				file.write(self.TextArea.get(1.0 , END))
				file.close()

				# change the window title
				self.root.title(os.path.basename(self.file) + ' - Notepad')

		else :
			file = open(self.file , "w")
			file.write(self.TextArea.get(1.0 , END))
			file.close()

	def cut(self):
		self.TextArea.event_generate("<<Cut>>")

	def copy(self):
		self.TextArea.event_generate("<<Copy>>")

	def paste(self):		
		self.TextArea.event_generate("<<Paste>>")

	def run(self):
		self.root.mainloop()

notepad = Notepad(width = 600 , height = 400)
notepad.run()