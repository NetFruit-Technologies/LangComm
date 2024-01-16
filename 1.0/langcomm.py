from tkinter import *
from speech_recognition import Recognizer, Microphone, RequestError, UnknownValueError
from gtts import gTTS
from playsound import playsound
from deep_translator import GoogleTranslator
from PIL import Image
from pytesseract import *
from os import remove, path, chmod
from time import sleep

if path.exists("audio.mp3"):

    remove("audio.mp3")

pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

footer_text = "Copyright © NetFruit Technologies LTD. All rights reserved."

class App(Tk):

    def __init__(self, *args, **kwargs):

        Tk.__init__(self, *args, **kwargs)

        container = Frame(self)

        container.pack(side="top", fill="both", expand=True)

        container.grid_rowconfigure(0, weight=1)

        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for i in (Start, Text, Speech, Picture, Settings):

            frame = i(container, self)

            self.frames[i] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(Start)

    def show_frame(self, contn):

        frame = self.frames[contn]

        frame.tkraise()

class Start(Frame):

    def __init__(self, parent, controller):

        Frame.__init__(self, parent)

        title_label = Label(
            self, fg="darkblue", text="Welcome to LangComm!", font=("Arial", 48))

        title_label.pack()

        blank_label = Label(self, text="")

        blank_label.pack()

        button_text = Button(
            self, text="Text Translation ⇒", fg="red", bg="black", font=("Arial", 36), command=lambda: controller.show_frame(Text))

        button_text.pack()

        blank_label2 = Label(self, text="")

        blank_label2.pack()

        button_speech = Button(
            self, text="Speech Translation ⇒", fg="red", bg="black", font=("Arial", 36), command=lambda: controller.show_frame(Speech))

        button_speech.pack()

        blank_label3 = Label(self, text="")

        blank_label3.pack()

        button_picture = Button(
            self, text="Picture Translation ⇒", fg="red", bg="black", font=("Arial", 36), command=lambda: controller.show_frame(Picture))

        button_picture.pack()

        blank_label4 = Label(self, text="")

        blank_label4.pack()

        button_settings = Button(
            self, text="Settings ⇒", fg="red", bg="black", font=("Arial", 36), command=lambda: controller.show_frame(Settings))

        button_settings.pack()
        
        footer = Label(self, text=footer_text, font=("Arial", 5))

        footer.place(x=400, y=760, anchor=CENTER)


class Text(Frame):

    def __init__(self, parent, controller):

        Frame.__init__(self, parent)

        text_heading = Label(
            self, fg="darkblue", text="Text Translation", font=("Arial", 48))

        text_heading.pack()

        button_back_h = Button(
            self, text="⇐", fg="red", bg="black", font=("Arial", 24), command=lambda: controller.show_frame(Start))

        button_back_h.place(x=0, y=20, anchor=W)

        settings_button = Button(self, text="⚙", fg="red", bg="black", font=("Arial", 24), command=lambda: controller.show_frame(Settings))

        settings_button.place(relx=1, rely=0, anchor=NE)

        blank_label = Label(self, text="")

        blank_label.pack()

        txt_e = Entry(self, width=100, borderwidth=5)

        txt_e.insert(END, "Enter in your text to translate here")

        txt_e.pack()

        def text_get():

            label.config(text=txt_e.get())

            def speak():

                speaking = gTTS(text=label2.cget("text"), lang=l_code)

                if path.exists("audio.mp3"):

                    remove("audio.mp3")

                speaking.save("audio.mp3")

                playsound("audio.mp3")

            label2 = Label(self, text="", bg="lightblue")

            label2.pack()

            translation = GoogleTranslator(source='auto', target=trans_lang).translate(label.cget("text"))

            label2.config(text=translation)

            speak_button = Button(self, text="🔊", command=speak)

            speak_button.pack()

        e_get_button = Button(self, text="Enter", command=text_get)

        e_get_button.pack()

        blank_label2 = Label(self, text="")

        blank_label2.pack()

        user_input_label = Label(
            self, fg="darkblue", text="Your Sentence:", font=("Arial", 24)).pack()

        label = Label(self, text="", bg="lightblue")
        
        label.pack()

        translation_label = Label(
            self, fg="darkblue", text="Translation:", font=("Arial", 24)).pack()

        footer = Label(
            self, text=footer_text, font=("Arial", 5))

        footer.place(x=400, y=760, anchor=CENTER)

class Speech(Frame):

    def __init__(self, parent, controller):

        Frame.__init__(self, parent)

        def get_user_speech():

            detector = Recognizer()

            try:

                with Microphone() as voice_input:

                    detector.adjust_for_ambient_noise(voice_input, duration=0.5)

                    v = detector.listen(voice_input)

                    content = detector.recognize_google(v)

                    label.config(text=content)

            except RequestError as e:

                print(e)
                        
            except UnknownValueError as u:
                        
                print(u)

            def speak():

                speaking = gTTS(text=label2.cget("text"), lang=l_code)

                if path.exists("audio.mp3"):

                    remove("audio.mp3")

                speaking.save("audio.mp3")

                playsound("audio.mp3")

            label2 = Label(self, text="", bg="lightblue")

            label2.pack()

            translation = GoogleTranslator(source='auto', target=trans_lang).translate(label.cget("text"))

            label2.config(text=translation)

            speak_button = Button(self, text="🔊", command=speak)

            speak_button.pack()


        speech_heading = Label(
            self, fg="darkblue", text="Speech Translation", font=("Arial", 48))

        speech_heading.pack()

        button_back_a = Button(
            self, text="⇐", fg="red", bg="black", font=("Arial", 24), command=lambda: controller.show_frame(Start))

        button_back_a.place(x=0, y=20, anchor=W)

        settings_button = Button(self, text="⚙", fg="red", bg="black", font=("Arial", 24), command=lambda: controller.show_frame(Settings))

        settings_button.place(relx=1, rely=0, anchor=NE)

        blank_label = Label(self, text="")

        blank_label.pack()

        user_input_label = Label(
            self, fg="darkblue", text="Your Sentence:", font=("Arial", 24)).pack()

        mic_button = Button(self, text="🎙️", command=get_user_speech)

        mic_button.pack()

        label = Label(self, text="", bg="lightblue")
        
        label.pack()

        translation_label = Label(
            self, fg="darkblue", text="Translation:", font=("Arial", 24)).pack()

        footer = Label(
            self, text=footer_text, font=("Arial", 5))

        footer.place(x=400, y=760, anchor=CENTER)

class Picture(Frame):

    def __init__(self, parent, controller):

        Frame.__init__(self, parent)

        picture_heading = Label(
            self, fg="darkblue", text="Picture Translation", font=("Arial", 48))

        picture_heading.pack()

        button_back_a = Button(
            self, text="⇐", fg="red", bg="black", font=("Arial", 24), command=lambda: controller.show_frame(Start))

        button_back_a.place(x=0, y=20, anchor=W)

        settings_button = Button(self, text="⚙", fg="red", bg="black", font=("Arial", 24), command=lambda: controller.show_frame(Settings))

        settings_button.place(relx=1, rely=0, anchor=NE)

        blank_label = Label(self, text="")

        blank_label.pack()

        path_e = Entry(self, width=100, borderwidth=5)

        path_e.insert(END, "Enter in your image path here")

        path_e.pack()

        def image_read():

            img = image_to_string(Image.open(path_e.get()))

            label.config(text=img)

            def speak():

                speaking = gTTS(text=label2.cget("text"), lang=l_code)

                if path.exists("audio.mp3"):

                    remove("audio.mp3")

                speaking.save("audio.mp3")

                playsound("audio.mp3")

            label2 = Label(self, text="", bg="lightblue")

            label2.pack()

            translation = GoogleTranslator(source='auto', target=trans_lang).translate(label.cget("text"))

            label2.config(text=translation)

            speak_button = Button(self, text="🔊", command=speak)

            speak_button.pack()

        e_get_button = Button(self, text="Enter", command=image_read)

        e_get_button.pack()

        blank_label2 = Label(self, text="")

        blank_label2.pack()

        user_input_label = Label(
            self, fg="darkblue", text="Your Sentence:", font=("Arial", 24)).pack()

        label = Label(self, text="", bg="lightblue")
        
        label.pack()

        translation_label = Label(
            self, fg="darkblue", text="Translation:", font=("Arial", 24)).pack()

        footer = Label(
            self, text=footer_text, font=("Arial", 5))

        footer.place(x=400, y=760, anchor=CENTER)

class Settings(Frame):

    def __init__(self, parent, controller):

        Frame.__init__(self, parent)

        picture_heading = Label(
            self, fg="darkblue", text="Settings", font=("Arial", 48))

        picture_heading.pack()

        button_back_a = Button(
            self, text="⇐", fg="red", bg="black", font=("Arial", 24), command=lambda: controller.show_frame(Start))

        button_back_a.place(x=0, y=20, anchor=W)

        blank_label = Label(self, text="")

        blank_label.pack()

        lang_e = Entry(self, width=100, borderwidth=5)

        lang_e.insert(END, "Enter in your translation language here")

        lang_e.pack()

        def set_language():

            global trans_lang

            trans_lang = lang_e.get()

        enter_button = Button(self, text="Enter", command=set_language)

        enter_button.pack()

        blank_label2 = Label(self, text="").pack()

        lang_code = Entry(self, width=100, borderwidth=5)

        lang_code.insert(END, "Enter in your translation language code here (eg: fr for French, de for German)")

        lang_code.pack()

        def set_lang_code():

            global l_code

            l_code = lang_code.get()

        enter_button2 = Button(self, text="Enter", command=set_lang_code)

        enter_button2.pack()

        footer = Label(
            self, text=footer_text, font=("Arial", 5))

        footer.place(x=400, y=760, anchor=CENTER)


root = App()

root.title("LangComm")

root.geometry("800x800")

root.mainloop()

root = Tk()