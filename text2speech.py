import tkinter as tk
from tkinter import ttk
import pyttsx3

class Text2SpeechApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Text2Speech")
        self.root.geometry('640x320')
        self.root.configure(bg='#3b3b3b')
        
        self.engine = pyttsx3.init()
        self.voices = self.engine.getProperty('voices')
        self.selected_voice = tk.StringVar()

        self.create_widgets()

    def create_widgets(self):
        # Title label
        title_label = ttk.Label(self.root, text='WELCOME 2 TEXT2SPEECH! ENTER YOUR TEXT BELOW!', font='arial 16 bold', background='#3b3b3b', foreground='white')
        title_label.pack(pady=10)

        # Text entry
        self.text_entry = ttk.Entry(self.root, font=("arial", 20))
        self.text_entry.pack(pady=20)

        # Voice selection
        voice_label = ttk.Label(self.root, text="Select Voice:", font='arial 12 bold', background='#3b3b3b', foreground='white')
        voice_label.pack()

        voice_combobox = ttk.Combobox(self.root, textvariable=self.selected_voice, state='readonly')
        voice_combobox['values'] = [voice.name for voice in self.voices]
        voice_combobox.current(0)
        voice_combobox.pack(pady=10)

        # Speak button
        speak_button = ttk.Button(self.root, text="Speak", command=self.talk)
        speak_button.pack(pady=10)

        # Download button
        download_button = ttk.Button(self.root, text="Download", command=self.download)
        download_button.pack(pady=10)

    def talk(self):
        self.engine.setProperty('voice', self.voices[self.selected_voice_index()].id)
        self.engine.say(self.text_entry.get())
        self.engine.runAndWait()

    def download(self):
        self.engine.setProperty('voice', self.voices[self.selected_voice_index()].id)
        self.engine.save_to_file(self.text_entry.get(), 'sound.mp3')
        self.engine.runAndWait()
        ttk.Label(self.root, text='DOWNLOADED...COPY THE FILE IN ANOTHER FOLDER', font='arial 14 bold', background='#3b3b3b', foreground='white').place(x=90, y=250)

    def selected_voice_index(self):
        return [voice.name for voice in self.voices].index(self.selected_voice.get())

if __name__ == "__main__":
    root = tk.Tk()
    app = Text2SpeechApp(root)
    root.mainloop()
