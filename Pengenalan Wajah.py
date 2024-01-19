import cv2 
import tkinter as tk
from tkinter import ttk
from ttkbootstrap import Style
from PIL import Image, ImageTk


#menampilkan hasil di antarmuka Tkinter
def process_video():
    ret, frame = cap.read()
    if ret:        
        # Proses frame menggunakan OpenCV (contoh: deteksi wajah)
        gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray_frame, scaleFactor=1.3, minNeighbors=5)

        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)

        # Konversi frame OpenCV ke format yang dapat ditampilkan di Tkinter
        img = Image.fromarray(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
        img = ImageTk.PhotoImage(img)

        video_label.img = img
        video_label.config(image=img)

        video_label.after(10, process_video)

# Membuat aplikasi GUI
app = tk.Tk()
app.title("Pengenalan Wajah dengan Tkinter")

style = Style('cosmo') 

frame_main = ttk.Frame(app, padding="10")
frame_main.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

cap = cv2.VideoCapture(0)

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

video_label = ttk.Label(frame_main)
video_label.grid(row=0, column=0)

process_video()
app.mainloop()
cap.release()