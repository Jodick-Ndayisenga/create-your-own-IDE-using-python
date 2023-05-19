from tkinter import *
from tkinter.filedialog import asksaveasfilename, askopenfilename
import subprocess

file_path = ""

def setFilePath(path):
    global file_path
    file_path = path

    
def runCode():
    if(file_path == ""):
        save_code_prompt = Toplevel()
        text = Label(save_code_prompt, text = "Please save your code first!")
        text.pack()
        return
        
    command = f"python {file_path}"
    myProcess = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    resultOfTheCode, codeError = myProcess.communicate()
    codeOutput.delete("1.0", END)
    codeOutput.insert("1.0", resultOfTheCode)
    codeOutput.insert("1.1", codeError)

    
def openFile():
    path = askopenfilename(filetypes=[("Python Files","*.py")])
    with open(path, 'r') as file:
        code = file.read()
        codeEditor.delete("1.0", END)
        codeEditor.insert("1.0", code)
        setFilePath(path)
   
def saveFileAs():
    if(file_path == ""):
        path = asksaveasfilename(filetypes=[("Python Files","*.py")])
    else:
        path = file_path

    with open(path,"w") as file:
        code = codeEditor.get("1.0", END)
        file.write(code)
        setFilePath(path)
    
#for this line below, we need to instantiate the object Tk and open the window
compiler = Tk()
compiler.title("My own IDE")

menu_bar = Menu(compiler)

file_menu = Menu(menu_bar, tearoff=0)
file_menu.add_command(label="New File", command=saveFileAs)
file_menu.add_command(label="Open file", command=openFile)
file_menu.add_command(label="Save", command=saveFileAs)
file_menu.add_command(label="Save As", command= saveFileAs)
file_menu.add_command(label="Exit", command=exit)
menu_bar.add_cascade(label="Open", menu = file_menu)

run_bar = Menu(menu_bar, tearoff=0)
run_bar.add_command(label="Run", command=runCode)
#on the line above, we are adding both label and command to be executed when run is hit
menu_bar.add_cascade(label="Run", menu=run_bar)


compiler.config(menu=menu_bar)
codeEditor = Text()
codeEditor.pack()

#these two lines below are to help me create another part to display the output
codeOutput = Text(height=9)
codeOutput.pack()
compiler.mainloop()
#In order to still have the window running, we need to have this loop
