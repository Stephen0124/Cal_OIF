import tkinter as tk
from tkinter import filedialog
from cal_OIF import calculate_OIF

def open_file(entry):
    file_path = filedialog.askopenfilename()
    entry.delete(0, tk.END)
    entry.insert(0, file_path)

def clear_entries():
    for entry in (entry_band_total, entry_band_group, entry_std_dev, entry_corr_coeff):
        entry.delete(0, tk.END)

def start_cal():
    num1 = entry_band_total.get()
    num2 = entry_band_group.get()
    filepath1 = entry_std_dev.get()
    filepath2 = entry_corr_coeff.get()
    print(num1,num2,filepath1,filepath2)
    calculate_OIF(num1,num2,filepath1,filepath2)

root = tk.Tk()
root.title("OIF计算器")

# a部分: 界面标题
frame_a = tk.Frame(root)
frame_a.pack(pady=15)

label_title = tk.Label(frame_a, text="波段分组OIF计算", font=("等线", 24))
label_title.pack()

tk.Canvas(frame_a, height=2, bg="black", width=1)

# b部分: 输入框
frame_b = tk.Frame(root)
frame_b.pack(pady=15, padx=10)

# 总波段数
label_band_total = tk.Label(frame_b, text="总波段数")
label_band_total.grid(row=0, column=0, sticky=tk.W)
entry_band_total = tk.Entry(frame_b)
entry_band_total.grid(row=0, column=1)

# 每组波段数
label_band_group = tk.Label(frame_b, text="每组波段数")
label_band_group.grid(row=1, column=0, sticky=tk.W)
entry_band_group = tk.Entry(frame_b)
entry_band_group.grid(row=1, column=1)

# 标准差文件路径
label_std_dev = tk.Label(frame_b, text="标准差文件路径")
label_std_dev.grid(row=2, column=0, sticky=tk.W)
entry_std_dev = tk.Entry(frame_b)
entry_std_dev.grid(row=2, column=1)
button_std_dev = tk.Button(frame_b, text="打开文件", command=lambda: open_file(entry_std_dev))
button_std_dev.grid(row=2, column=2)

# 相关系数文件路径
label_corr_coeff = tk.Label(frame_b, text="相关系数文件路径")
label_corr_coeff.grid(row=3, column=0, sticky=tk.W)
entry_corr_coeff = tk.Entry(frame_b)
entry_corr_coeff.grid(row=3, column=1)
button_corr_coeff = tk.Button(frame_b, text="打开文件", command=lambda: open_file(entry_corr_coeff))
button_corr_coeff.grid(row=3, column=2)

# c部分: 按钮
frame_c = tk.Frame(root)
frame_c.pack(pady=15)

button_start = tk.Button(frame_c, text="开始计算", command=start_cal)
button_start.pack(side=tk.LEFT, padx=10)

button_clear = tk.Button(frame_c, text="清空输入", command=clear_entries)
button_clear.pack(side=tk.RIGHT, padx=10)

root.mainloop()