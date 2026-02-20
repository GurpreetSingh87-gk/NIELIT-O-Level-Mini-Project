import customtkinter
from customtkinter import CTkImage
from PIL import Image
import webbrowser
from tkinter import messagebox

# Main Window:-
# -----------

root = customtkinter.CTk()
root.title("Fist GUI Window")
root.geometry("900x525")
root.resizable(False,False)

# =================================================================================

# White Background Frame:-
# ----------------------

my_frame = customtkinter.CTkFrame(
     root,
     width=450,
     height=450,
     fg_color="white"
)
my_frame.place(x=400, y=30)

# =================================================================================

# Illustration Image Background Frame:-
# -----------------------------------

left_image_frame = customtkinter.CTkFrame(
     root,
     width=348,
     height=450,
     fg_color="white",
     bg_color="white",
     border_width=0
)
left_image_frame.place(x=60, y=30)

# Illustration Image:-
# ------------------

illustration_image = customtkinter.CTkImage(
     light_image=Image.open(r"C:\Users\HARMEET KAUR\Downloads\undraw_investor-update_ou4c.png"),
     size=(360,300)
)

# Illustration Label:-
# ------------------

illustration_image_label = customtkinter.CTkLabel(
     left_image_frame,
     text="",
     image=illustration_image,
)
illustration_image_label.place(x=0, y=90)

# Border Line:-
# -----------

Borderline_frame = customtkinter.CTkFrame(
     my_frame,
     width=3,
     height=385,
     bg_color="#f2f2f2",
     border_width=0
).place(x=20, y=30)

# =================================================================================

# Heading:-
# -------

my_label = customtkinter.CTkLabel(
     my_frame,
     text="Sign in",
     font=("Segoe UI", 25, "bold"),
     text_color="#2196F3"
)
my_label.place(x=186, y=20)

# ==================================================================================

# Username Image:-
# --------------

username_image = customtkinter.CTkImage(
     light_image=Image.open(r"C:\Users\HARMEET KAUR\Downloads\icons8-username-60.png"),
     size=(20,20)
)

# Username Image Placement:-
# ------------------------

username_label = customtkinter.CTkLabel(
     my_frame,
     text="",
     image=username_image
)
username_label.place(x=100, y=100)

# Username Entry Widget:-
# ---------------------

username_entry = customtkinter.CTkEntry(
     my_frame,
     placeholder_text="Username or Email",
     font=("Segoe UI", 17),
     width=280,
     height=20,
     corner_radius=20,
     border_width=0,
     fg_color="white"
)
username_entry.place(x=120, y=100)

# Frame:-
# ------

frame = customtkinter.CTkFrame(
     my_frame,
     width=250,
     height=2,
     bg_color="#f2f2f2",
     border_width=0
).place(x=100, y=135)

# =================================================================================

# Password Image:-
# --------------

password_image = customtkinter.CTkImage(
     light_image=Image.open(r"C:\Users\HARMEET KAUR\Downloads\icons8-password-60.png"),
     size=(20,20)
)

# Password Image Placement:-
# ------------------------

password_label = customtkinter.CTkLabel(
     my_frame,
     text="",
     image=password_image
)
password_label.place(x=100, y=160)

# Password Entry Widget:-
# ---------------------

password_entry = customtkinter.CTkEntry(
     my_frame,
     placeholder_text="Password",
     show="*",
     font=("Segoe UI", 17),
     width=280,
     height=20,
     corner_radius=20,
     border_width=0,
     fg_color="white"
)
password_entry.place(x=120, y=160)

# Frame:-
# -----

frame = customtkinter.CTkFrame(
     my_frame,
     width=250,
     height=2,
     bg_color="#f2f2f2",
     border_width=0
).place(x=100, y=195)

# =================================================================================

# Hide Frame:-
# ----------

hide_frame = customtkinter.CTkFrame(
     my_frame,
     fg_color="white",
     width=30,
     height=30
)
hide_frame.place(x=320, y=160)

# Hide Password Image:-
# -------------------

hide_image = customtkinter.CTkImage(
     light_image=Image.open(r"C:\Users\HARMEET KAUR\Downloads\icons8-hide-24.png"),
     size=(18,18)
)

# Hide Password Function:-
# ----------------------

def open_hide():
     if password_entry.cget('show') == '':
          password_entry.configure(show='*')
     else:
          password_entry.configure(show='')
               
# Hide Password button:-
# --------------------

Hide_btn = customtkinter.CTkButton(
     hide_frame,
     image=hide_image,
     text="",
     width=25,
     height=25,
     fg_color="white",
     hover_color="#f2f2f2",
     corner_radius=25,
     command=open_hide
)
Hide_btn.pack(side="right")

# =================================================================================

# Forgot Password Link:-
# --------------------

def open_google_forgotps():
     webbrowser.open("https://accounts.google.com/signin/recovery")
     
forgot_btn = customtkinter.CTkButton(
     my_frame,
     text="Forgot password?",
     font=("Segoe UI", 14),
     text_color="#2196F3",
     fg_color="white",
     width=10,
     corner_radius=25,
     hover_color="#f2f2f2",
     command=open_google_forgotps
)
forgot_btn.place(x=230, y=200)

# Forgot Password Button Functions:-
# --------------------------------

def open_forgotps(event=None):
     print("Forgot Password clicked!")
     
def on_enter(event):
     forgot_btn.configure(text_color="red")  

def on_leave(event):
     forgot_btn.configure(text_color="#2196F3")  

forgot_btn.bind("<Button-1>", open_forgotps)

forgot_btn.bind("<Enter>", on_enter)

forgot_btn.bind("<Leave>", on_leave)

# =================================================================================

# Send Backend logic:-
# ------------------

def login():
     username = username_entry.get()
     password = password_entry.get()
     
     if username == "" or password == "":
          messagebox.showerror("Error","Please fill all fields!")
     else:
          messagebox.showinfo("Success","Sign in Successfully")     

# Send Button:-
# -----------

btn = customtkinter.CTkButton(
     my_frame,
     text="Sign in",
     font=("Segoe UI", 15),
     fg_color="#2196F3",
     corner_radius=20,
     width=250,
     command=login,
)
btn.place(x=100, y=250)
     
# =================================================================================

# Don't have an account label:-
# ---------------------------

title_label = customtkinter.CTkLabel(
     my_frame,
     text="Don't have an account?",
     font=("Segoe UI", 15),
)
title_label.place(x=120, y=290)

# =================================================================================

# Sign in Link:-
# ------------

def open_google():
    webbrowser.open("https://accounts.google.com")

signin_label = customtkinter.CTkButton(
     my_frame,
     text="Sign in",
     font=("Segoe UI", 15, "underline"),
     text_color="#2196F3",
     fg_color="white",
     width=10,
     corner_radius=25,
     command=open_google,
     hover_color="#f2f2f2",
)
signin_label.place(x=270, y=290)

# Sign in Function:-
# ----------------

def open_signin(event=None):
     print("Sign in clicked")
     
def on_enter(event):
     signin_label.configure(text_color="red")  

def on_leave(event):
     signin_label.configure(text_color="#2196F3")  

signin_label.bind("<Button-1>", open_signin)

signin_label.bind("<Enter>", on_enter)

signin_label.bind("<Leave>", on_leave)

# =================================================================================

# line frame:-
# ----------

line_frame = customtkinter.CTkFrame(
     my_frame,
     width=330,
     height=2,
     bg_color="#f2f2f2",
     border_width=0
)      
line_frame.place(x=60, y=350) 

# or connect with label:-
# ---------------------

text_label = customtkinter.CTkLabel(
     my_frame,
     text="or connect with",
     font=("Segoe UI", 16),
     fg_color="white"
) 
text_label.place(x=170, y=334)

# =================================================================================

# Social Media Link:-
# -----------------

def open_facebook():
    webbrowser.open("https://www.facebook.com/login")

def open_google():
    webbrowser.open("https://accounts.google.com")

def open_instagram():
    webbrowser.open("https://www.instagram.com/accounts/login/?hl=en")

# =================================================================================

# Icons Frame:-
# -----------

icons_frame = customtkinter.CTkFrame(
     my_frame, 
     fg_color="white",
     width=250,
     height=50,
)
icons_frame.place(x=90, y=380)

# ==================================================================================

# Load Images:-
# -----------

fb_img = customtkinter.CTkImage(
    Image.open(r"C:\Users\HARMEET KAUR\Downloads\facebook.png"),
    size=(29, 29)
)

google_img = customtkinter.CTkImage(
    Image.open(r"C:\Users\HARMEET KAUR\Downloads\google.png"),
    size=(26, 26)
)

instagram_img = customtkinter.CTkImage(
    Image.open(r"C:\Users\HARMEET KAUR\Downloads\instagram.png"),
    size=(29, 29)
)

# =================================================================================

# Icon Buttons:-
# ------------

# Facebook:-

customtkinter.CTkButton(
    icons_frame,
    image=fb_img,
    text="",
    width=40,
    height=40,
    corner_radius=25,
    fg_color="white",
    hover_color="#f2f2f2",
    command=open_facebook
).pack(side="left", padx=10)

# Google:-

customtkinter.CTkButton(
    icons_frame,
    image=google_img,
    text="",
    width=40,
    height=40,
    corner_radius=25,
    fg_color="white",
    hover_color="#f2f2f2",
    command=open_google
).pack(side="left", padx=12)

# Instagram:-

customtkinter.CTkButton(
    icons_frame,
    image=instagram_img,
    text="",
    width=40,
    height=40,
    corner_radius=25,
    fg_color="white",
    hover_color="#f2f2f2",
    command=open_instagram
).pack(side="left", padx=12)

root.mainloop()

