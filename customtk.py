import tkinter as tk
import tkinter.messagebox
import customtkinter
from PIL import Image, ImageTk
import cv2

customtkinter.set_appearance_mode("System")  #System/Dark/Light
customtkinter.set_default_color_theme("blue")  #blue/green/dark-blue


class App(customtkinter.CTk):

    WIDTH = 1280
    HEIGHT = 720

    def __init__(self):
        super().__init__()

        self.title("HotBastards")
        self.geometry(f"{App.WIDTH}x{App.HEIGHT}")
        self.set_grid_layout()
        self.camera_init()
        self.protocol("WM_DELETE_WINDOW", self.destructor)  

        self.video_loop()

    

    def set_grid_layout(self):
        self.grid_columnconfigure(1, weight = 1)
        self.grid_rowconfigure(0, weight = 1)

        self.left_frame = customtkinter.CTkFrame(master = self,
                                                 width = 300,
                                                 corner_radius = 20)                                        
        self.left_frame.grid(row = 0, column = 0, sticky = "nswe")
        

        self.right_frame = customtkinter.CTkFrame(master=self, corner_radius = 20)
        self.right_frame.grid(row = 0, column = 1, sticky = "nswe", padx = 20)
        self.video_label = tk.Label(self)
        self.video_label.grid(row = 0, column = 1, padx = 30, pady = 30)
        
    def video_loop(self):
        _, current_frame = self.cap.read()  # Pobranie klatki z kamery
        current_frame = cv2.flip(current_frame, 1)
        current_frame = cv2.cvtColor(current_frame, cv2.COLOR_BGR2RGBA)  
        self.final_frame = Image.fromarray(current_frame)  
        frame_tk = ImageTk.PhotoImage(image = self.final_frame)  
        self.video_label.imgtk = frame_tk 
        self.video_label.config(image = frame_tk)  

        self.after(1, self.video_loop)


    def button_event(self):
        print("Button pressed")

    def camera_init(self):
        self.cap = cv2.VideoCapture(0)
        self.final_frame = None
        
    def change_appearance_mode(self, new_appearance_mode):
        customtkinter.set_appearance_mode(new_appearance_mode)

    def destructor(self):
        self.destroy()
        self.cap.release()  
        cv2.destroyAllWindows()  


if __name__ == "__main__":
    app = App()
    app.mainloop()