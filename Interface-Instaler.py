#Interface Instaler created by Deyvid g. m.
#My GitHub: https://github.com/Srflash
#Project by CosmosWorld
#GitHub: https://github.com/CosmosWorld

from tkinter import *
import subprocess

janela = Tk()

Archivc = ['git','clone','https://github.com/Srflash/InterfaceArchive-Cosmos.git']

clipg1 = ['sh','InterfaceArchives-Cosmos/clipg.sh']

clipg2 = ['sudo','apt-get','install','clipgrab']

upd = ['sudo','apt-get','update']

audac = ['sudo','apt-get','install','audacity']

retr1 = ['sh','InterfaceArchives-Cosmos/retr.sh']

retr2 = ['sudo','apt-get','install','retroarch*','libretro-*']

def next1():
	nex1 = int(list1.get() + int('1'))
	nex2 = int(list2.get() + int('2'))
	nexres = (int(nex1) * int(nex2))
	if nexres == 2:
		jan2 = Tk()
		
		textja1 = Label(jan2, text="Error. Choose an option!")
		textja1.grid(row=0, column=0)
		
		btja1 = Button(jan2, width=20, text="Ok", command=jan2.destroy)
		btja1.grid(row=1, column=0)
		
		jan2.mainloop()
	
	if nexres == 4:
		janela.destroy()
		subprocess.run(Archivc)
		subprocess.run(clipg1)
		subprocess.run(upd)
		subprocess.run(clipg2)
		subprocess.run(audac)
		subprocess.run(retr1)
		subprocess.run(upd)
		subprocess.run(retr2)
	
	if nexres == 3:
		janela.destroy()
		
		root = Tk()
		
		def inst1():
			num1 = int(ck1.get() + int('1'))
			num2 = int(ck2.get() + int('3'))
			num3 = int(ck3.get() * int('6'))
			res = (int(num1) * int(num2) + int(num3))
			subprocess.run(Archivc)
			if res == 6:
				root.destroy()
				subprocess.run(clipg1)
				subprocess.run(upd)
				subprocess.run(clipg2)
			
			if res == 4:
				root.destroy()
				subprocess.run(audac)
			
			if res == 9:
				root.destroy()
				subprocess.run(retr1)
				subprocess.run(upd)
				subprocess.run(retr2)
			
			if res == 8:
				root.destroy()
				subprocess.run(clipg1)
				subprocess.run(upd)
				subprocess.run(clipg2)
				subprocess.run(audac)
			
			if res == 14:
				root.destroy()
				subprocess.run(clipg1)
				subprocess.run(upd)
				subprocess.run(clipg2)
				subprocess.run(audac)
				subprocess.run(retr1)
				subprocess.run(upd)
				subprocess.run(retr2)
			
			if res == 10:
				root.destroy()
				subprocess.run(audac)
				subprocess.run(retr1)
				subprocess.run(upd)
				subprocess.run(retr2)
			
			if res == 12:
				root.destroy()
				subprocess.run(clipg1)
				subprocess.run(upd)
				subprocess.run(clipg2)
				subprocess.run(retr1)
				subprocess.run(upd)
				subprocess.run(retr2)
			
		lb1 = Label(root, text="Choose the programs you want to install:")
		lb1.grid(row=0, column=0)
		
		ck1 = IntVar()
		Checkbutton(root, text="ClipGrab", variable=ck1).grid(row=1, column=0, stick=W)
		
		ck2 = IntVar()
		Checkbutton(root, text="Audacity", variable=ck2).grid(row=2, column=0, stick=W)
		
		ck3 = IntVar()
		Checkbutton(root, text="RetroArch", variable=ck3).grid(row=3, column=0, stick=W)
		
		bt1 = Button(root, width=20, text="Install", command=inst1)
		bt1.grid(row=4, column=0)
		
	if nexres == 6:
		jan1 = Tk()
		
		textja = Label(jan1, text="Error. Choose only one option!")
		textja.grid(row=0, column=0)
		
		btja = Button(jan1, width=20, text="Ok", command=jan1.destroy)
		btja.grid(row=1, column=0)
		
		jan1.mainloop()
		
	root.title('Cosmos Instaler')
	root.geometry("350x180+100+100")
	root.mainloop()
	
#texto
text1 = Label(janela, text="Choose the type of installation you want to do:")
text1.grid(row=0, column=0)

text2 = Label(janela, text="(Install the following programs - ClipGrab, Audacity, RetroArch)")
text2.grid(row=2, column=0, stick=W)

text3 = Label(janela, text="(Choose which programs you want to install)")
text3.grid(row=5, column=0, stick=W)

space1 = Label(janela, text="")
space1.grid(row=3, column=0)

#checklist
list1 = IntVar()
Checkbutton(janela, text="Complete installation", variable=list1).grid(row=1, column=0, stick=W)

list2 = IntVar()
Checkbutton(janela, text="Custom install", variable=list2).grid(row=4, column=0, stick=W)

#botão
bot1 = Button(janela, width=20, text="Next", command=next1)
bot1.grid(row=6, column=0)

janela.title('Cosmos Instaler')
janela.geometry("350x180+100+100")
janela.mainloop()