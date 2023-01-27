import os
import openai
from PyQt5 import QtCore, QtGui, QtWidgets

class GPT3Gui(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        # Use your API key stored in an environment variable
        openai.api_key = os.environ["OpenAi_API_KEY"]

        # Create a text box for the prompt
        self.prompt_textbox = QtWidgets.QLineEdit(self)
        self.prompt_textbox.setFont(QtGui.QFont("Arial", 14))
        self.prompt_textbox.setMinimumHeight(50)

        # Create a button to generate the completions
        self.generate_button = QtWidgets.QPushButton("Generate", self)
        self.generate_button.setFont(QtGui.QFont("Arial", 16))
        self.generate_button.clicked.connect(self.generate_completions)

        # Create a text box for the completions
        self.completions_textbox = QtWidgets.QTextEdit(self)
        self.completions_textbox.setFont(QtGui.QFont("Arial", 14))
        self.completions_textbox.setMinimumHeight(200)

        # Create a layout and add the widgets
        layout = QtWidgets.QVBoxLayout(self)
        layout.addWidget(QtWidgets.QLabel("Prompt:", self))
        layout.addWidget(self.prompt_textbox)
        layout.addWidget(self.generate_button)
        layout.addWidget(QtWidgets.QLabel("Completions:", self))
        layout.addWidget(self.completions_textbox)
        
        # Set the main window size
        self.setGeometry(200, 200, 600, 400)
        self.setWindowTitle("GPT-3 GUI")

    def generate_completions(self):
        # Get the prompt from the text box
        prompt = self.prompt_textbox.text()

        # Generate completions
        completions = openai.Completion.create(
            engine="text-davinci-002",
            prompt=prompt,
            max_tokens=1024,
            n=1,
            stop=None,
            temperature=0.5,
        )

        # Show the completions in the text box
        self.completions_textbox.setText(completions.choices[0].text)

if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    gui = GPT3Gui()
    gui.show()
    app.exec_()
