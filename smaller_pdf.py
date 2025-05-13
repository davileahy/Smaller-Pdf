import tkinter as tk
from tkinter import filedialog, messagebox, ttk
import subprocess
import os
import threading
import time

def compress_pdf(input_path, output_path, compression_level):
    """
    Comprime PDF usando Ghostscript via subprocess
    """
    gs_exe = os.path.join(os.path.dirname(os.path.abspath(__file__)), "gswin64c.exe")

    gs_command = [
        gs_exe,
        "-sDEVICE=pdfwrite",
        "-dCompatibilityLevel=1.4",
        f"-dPDFSETTINGS=/{compression_level}",
        "-dNOPAUSE",
        "-dQUIET",
        "-dBATCH",
        f"-sOutputFile={output_path}",
        input_path
    ]

    try:
        process = subprocess.Popen(gs_command)
        while process.poll() is None:
            time.sleep(0.2)
        on_done()
    except Exception as e:
        on_error(e)

def get_file_size(path):
    size = os.path.getsize(path) / (1024 * 1024)
    return round(size, 2)

def browse_input():
    filename = filedialog.askopenfilename(filetypes=[("PDF Files", "*.pdf")])
    if filename:
        input_var.set(filename)

def browse_output():
    filename = filedialog.asksaveasfilename(defaultextension=".pdf", filetypes=[("PDF Files", "*.pdf")])
    if filename:
        output_var.set(filename)

def start_compression():
    input_pdf = input_var.get()
    output_pdf = output_var.get()
    level = compression_var.get()

    if not input_pdf or not output_pdf:
        messagebox.showerror("Erro", "Por favor selecione os arquivos.")
        return

    if os.path.exists(output_pdf):
        os.remove(output_pdf)

    try:
        size_before = get_file_size(input_pdf)
        messagebox.showinfo("Tamanho Original", f"{size_before} MB")

        progress_bar.start(10)

        threading.Thread(target=compress_pdf, args=(input_pdf, output_pdf, level), daemon=True).start()

    except Exception as e:
        messagebox.showerror("Erro", str(e))

def on_done():
    progress_bar.stop()
    size_after = get_file_size(output_var.get())
    messagebox.showinfo("Sucesso", f"Compressão concluída!\nNovo tamanho: {size_after} MB")
    progress_bar["value"] = 0

def on_error(e):
    progress_bar.stop()
    messagebox.showerror("Erro", f"Erro durante compressão: {str(e)}")
    progress_bar["value"] = 0

# Cria janela principal
root = tk.Tk()
root.title("Compressão de PDF")
root.resizable(False, False)

# Variáveis
input_var = tk.StringVar()
output_var = tk.StringVar()
compression_var = tk.StringVar(value="ebook")

# Layout
tk.Label(root, text="Arquivo PDF:").grid(row=0, column=0, sticky="w")
tk.Entry(root, textvariable=input_var, width=40).grid(row=0, column=1)
tk.Button(root, text="Selecionar", command=browse_input).grid(row=0, column=2)

tk.Label(root, text="Salvar como:").grid(row=1, column=0, sticky="w")
tk.Entry(root, textvariable=output_var, width=40).grid(row=1, column=1)
tk.Button(root, text="Selecionar", command=browse_output).grid(row=1, column=2)

tk.Label(root, text="Nível de Compressão:").grid(row=2, column=0, sticky="w")
compression_options = ['screen', 'ebook', 'printer', 'prepress']
compression_menu = ttk.Combobox(root, textvariable=compression_var, values=compression_options, state="readonly")
compression_menu.grid(row=2, column=1, sticky="w")

progress_bar = ttk.Progressbar(root, orient="horizontal", mode="indeterminate", length=250)
progress_bar.grid(row=3, column=0, columnspan=3, pady=10)

tk.Button(root, text="Comprimir", command=start_compression, width=20).grid(row=4, column=0, columnspan=3, pady=5)

# Executa janela
root.mainloop()
