import tkinter as tk

def calculate():
    try:
        result = eval(entry.get())
        label_result.config(text=f"結果: {result}")
    except Exception as e:
        label_result.config(text="錯誤！")

root = tk.Tk()
root.title("簡易計算機")

entry = tk.Entry(root, width=20)
entry.pack(pady=10)

button_calc = tk.Button(root, text="計算", command=calculate)
button_calc.pack(pady=5)

label_result = tk.Label(root, text="結果:")
label_result.pack(pady=10)

root.mainloop()