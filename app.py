import tkinter as tk
import tkinter.messagebox
import customtkinter
from PIL import Image, ImageTk
import cv2
import psutil
import time

class App(customtkinter.CTk):

    APP_WIDTH = 1280
    APP_HEIGHT = 720

    def __init__(self):
        super().__init__()

        self.pTime = 0

        self.title("HotBastards")
        self.geometry(f"{App.APP_WIDTH}x{App.APP_HEIGHT}")
        self.wm_iconphoto(False, ImageTk.PhotoImage(Image.open('./Pictures/icon.jpg')))
        self.set_grid_layout()
        self.set_labels()
        self.set_buttons()
        self.set_switches()
        self.set_default_values()
        self.camera_init()
        self.protocol("WM_DELETE_WINDOW", self.destructor)  
        self.video_loop()


    def video_loop(self):
        _, self.current_frame = self.cap.read()  # Pobranie klatki z kamery
        self.current_frame = cv2.flip(self.current_frame, 1)
        self.current_frame = cv2.cvtColor(self.current_frame, cv2.COLOR_BGR2RGBA)  
        self.final_frame = Image.fromarray(self.current_frame)  
        frame_tk = ImageTk.PhotoImage(image = self.final_frame)  
        self.video_label.imgtk = frame_tk 
        self.video_label.config(image = frame_tk) 

        self.after(1, self.video_loop)
        
    def set_grid_layout(self):
        self.grid_columnconfigure(1, weight = 1)
        self.grid_rowconfigure(0, weight = 1)

        self.left_frame = customtkinter.CTkFrame(master = self, width = 250, corner_radius = 20)                                        
        self.left_frame.grid(row = 0, column = 0, sticky = "nswe")
        
        self.left_frame.grid_rowconfigure(0, minsize=10)   # empty row with minsize as spacing
        self.left_frame.grid_rowconfigure(5, weight=1)  # empty row as spacing
        self.left_frame.grid_rowconfigure(8, minsize=20)    # empty row with minsize as spacing
        self.left_frame.grid_rowconfigure(11, minsize=10)  # empty row with minsize as spacing

        self.mid_frame = customtkinter.CTkFrame(master=self, corner_radius = 20)
        self.mid_frame.grid(row = 0, column = 1, sticky = "nswe", padx = (20, 0))

        
    def set_labels(self):
        self.video_label = tk.Label(self, background = 'gray17')
        self.video_label.grid(row = 0, column = 1, padx = 30, pady = 30)

        self.menu_label = customtkinter.CTkLabel(
            master = self.left_frame,
            text = 'MENU',
            text_font = ('Cooper Black', 25)
        )
        self.menu_label.grid(column=0, row=0, sticky="n", padx=15, pady=15)

    def set_buttons(self):
        pass

    def set_switches(self):
        self.change_theme_menu = customtkinter.CTkOptionMenu(
            master=self.left_frame,
            values=["Light", "Dark"],
            text_font = ('Cooper Black', 12),
            command=self.change_theme)          
                                   
        self.change_theme_menu.grid(row=10, column=0, pady=10, padx=20, sticky="sw")

    def set_default_values(self):
        self.change_theme_menu.set('Dark')

    def button_test(self):
        print('Chuj dupa cipa')

    def camera_init(self):
        self.cap = cv2.VideoCapture(0)
        _, self.current_frame = self.cap.read()
        self.WEBCAM_HEIGHT = self.current_frame.shape[0]
        self.WEBCAM_WIDTH = self.current_frame.shape[1]
        self.final_frame = None
        
    def change_theme(self, new_theme):
        customtkinter.set_appearance_mode(new_theme)

    def destructor(self):
        self.destroy()
        self.cap.release()  
        cv2.destroyAllWindows()  


