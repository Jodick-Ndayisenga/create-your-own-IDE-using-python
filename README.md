#CREATE YOUR OWN IDE USING SIMPLE PYTHON CODE

##snippet that implements a basic Python Integrated Development Environment (IDE) with ##execution capabilities. The code utilizes the Tkinter library for creating the GUI ##components and subprocess for executing Python scripts. Let's delve into the details of ##each section.

the code starts by importing the necessary libraries which are tkinter and subprocess.
we also import imported asksaveasfilene and askopenasfilename functions to be able to interact with the system repositories.
In the beginning, we also initialize a global variable that will be used to store or retrieve files.

##we declared and initialized several functions:

##codeRun():
This function is responsible for executing the Python script. It first checks if file_path is empty. If it is, it displays a message indicating that the code needs to be saved first. Otherwise, it constructs a command using the file_path and invokes subprocess.Popen() to create a new process. The standard output and error streams are captured using stdout=subprocess.PIPE and stderr=subprocess.PIPE. The output is then inserted into a text widget named codeOutput using codeOutput.insert(). Additionally, the error output is inserted after the output.

##Setting the File Path():
We also have this function to always be updating the file path whenever repository is changed

##A. openFile():
This function is called when the user selects "Open file" from the menu. It opens a file dialog using askopenfilename() and retrieves the selected file's path. The file is then opened, its contents are read, and the text widget named codeEditor is updated with the file's content. The setFilePath() function is called to set the file_path variable to the selected file's path.

##B. saveFile():
The saveFileAs() function is responsible for saving the current code to a file. If file_path is empty, the function prompts the user to select a save location using asksaveasfilename(). Otherwise, it uses the existing file_path. The code from the codeEditor text widget is retrieved using codeEditor.get() and written to the file. The setFilePath() function is called to set the file_path variable to the saved file's path.

#After initialization of necessary tools and some funtions:

##Creating the GUI and Main Loop

The code creates a Tkinter object called compiler and sets the title to "My own IDE". It creates a menu bar using Menu(compiler) and defines various menu options, including "New File", "Open file", "Save", "Save As", and "Exit". The runCode() function is bound to the "Run" option.

The code creates a text widget named codeEditor to display and edit the code. It also creates another text widget named codeOutput to display the output of the executed code.

Finally, the main loop compiler.mainloop() is used to continuously display the IDE's window and handle user interactions.

Conclusion:
In conclusion, this code snippet showcases a basic Python IDE that allows users to create, open, and save Python code files. It provides execution capabilities by running the code through subprocess and capturing the output and error streams. The code demonstrates the usage of Tkinter for GUI creation and interaction.
