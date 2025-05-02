import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk, ImageFilter
import pyautogui

def create_blurred_background():
    screenshot = pyautogui.screenshot()
    blurred_image = screenshot.filter(ImageFilter.GaussianBlur(radius=15))
    return ImageTk.PhotoImage(blurred_image)

def check_password():
    if password_entry.get() == "secret":
        root.destroy()
    else:
        messagebox.showerror("Ошибка", "Неверный пароль")
        password_entry.delete(0, 'end')

# Создаем главное окно
root = tk.Tk()
root.overrideredirect(True)  # Убираем рамки окна

# Получаем размеры экрана
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# Устанавливаем размеры окна вручную
root.geometry(f"{screen_width}x{screen_height}+0+0")
root.attributes('-alpha', 5.0)
root.attributes('-topmost', True)  # Окно поверх всех других

# Создаем размытый фон
background_image = create_blurred_background()

# Добавляем фон
background_label = tk.Label(root, image=background_image)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

# Создаем рамку для центрирования элементов
frame = tk.Frame(root, bg='gray')
frame.place(relx=0.5, rely=0.5, anchor='center')

# Поле ввода пароля
password_entry = tk.Entry(
    frame,
    show="*",
    font=('Arial', 24),
    width=20,
    bd=0,
    highlightthickness=1
)
password_entry.pack(pady=20, padx=40)

# Кнопка входа
login_button = tk.Button(
    frame,
    text="Войти",
    command=check_password,
    font=('Arial', 14),
    bg='#4CAF50',
    fg='white',
    bd=0,
    padx=20,
    pady=10
)
login_button.pack(pady=(0, 20))

# Привязываем Enter к проверке пароля
password_entry.bind('<Return>', lambda event: check_password())

# Выход по Esc
#root.bind('<Escape>', lambda e: root.destroy())

# Фокус на поле ввода
password_entry.focus_set()

root.mainloop()