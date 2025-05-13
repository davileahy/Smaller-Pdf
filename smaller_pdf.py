import PySimpleGUI as sg
import subprocess
import os
import threading
import time

def compress_pdf(input_path, output_path, compression_level, window):
    """
    Função para comprimir PDF usando Ghostscript via subprocess
    """
    gs_command = [
        "gs",
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
        # Simula progresso enquanto o subprocess roda
        process = subprocess.Popen(gs_command)
        while process.poll() is None:
            window.write_event_value('-PROGRESS-', None)
            time.sleep(0.2)
        window.write_event_value('-DONE-', None)

    except Exception as e:
        window.write_event_value('-ERROR-', str(e))


def get_file_size(path):
    """
    Retorna tamanho do arquivo em MB
    """
    size = os.path.getsize(path) / (1024 * 1024)
    return round(size, 2)


# Layout da janela
layout = [
    [sg.Text("Arquivo PDF:"), sg.Input(key='-IN-'), sg.FileBrowse(file_types=(("PDF Files", "*.pdf"),))],
    [sg.Text("Salvar como:"), sg.Input(key='-OUT-'), sg.FileSaveAs(file_types=(("PDF Files", "*.pdf"),))],
    [sg.Text("Nível de Compressão:")],
    [sg.Combo(values=['screen', 'ebook', 'printer', 'prepress'], default_value='ebook', key='-LEVEL-')],
    [sg.ProgressBar(max_value=100, orientation='h', size=(30, 20), key='-PROG-')],
    [sg.Button("Comprimir"), sg.Button("Sair")]
]

# Criar janela
window = sg.Window("Compressão de PDF", layout)

# Loop principal
progress = 0

while True:
    event, values = window.read(timeout=100)
    
    if event in (sg.WINDOW_CLOSED, "Sair"):
        break

    if event == "Comprimir":
        input_pdf = values['-IN-']
        output_pdf = values['-OUT-']
        level = values['-LEVEL-']

        if not input_pdf or not output_pdf:
            sg.popup_error("Por favor selecione os arquivos.")
            continue

        if os.path.exists(output_pdf):
            os.remove(output_pdf)  # Remove se já existe para evitar erro

        try:
            # Mostra tamanho original
            size_before = get_file_size(input_pdf)
            sg.popup(f"Tamanho original: {size_before} MB")

            # Inicia thread para compressão
            threading.Thread(target=compress_pdf, args=(input_pdf, output_pdf, level, window), daemon=True).start()
            progress = 0
            window['-PROG-'].update_bar(0)

        except Exception as e:
            sg.popup_error(f"Ocorreu um erro: {e}")

    elif event == '-PROGRESS-':
        # Incrementa barra de progresso
        progress = (progress + 5) % 105  # Loop progressivo
        window['-PROG-'].update_bar(progress)

    elif event == '-DONE-':
        window['-PROG-'].update_bar(100)
        size_after = get_file_size(values['-OUT-'])
        sg.popup(f"Compressão concluída!\nNovo tamanho: {size_after} MB")
        window['-PROG-'].update_bar(0)

    elif event == '-ERROR-':
        sg.popup_error(f"Erro durante compressão: {values[event]}")
        window['-PROG-'].update_bar(0)

window.close()
