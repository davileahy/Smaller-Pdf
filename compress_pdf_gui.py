import pikepdf
from tkinter import Tk, filedialog
import os

def compress_pdf(input_pdf, output_pdf):
    """
    Compress the entire PDF, including images and other elements.

    Args:
        input_pdf (str): Path to the input PDF file.
        output_pdf (str): Path to save the compressed PDF file.
    """
    try:
        # Open the PDF with pikepdf
        with pikepdf.open(input_pdf) as pdf:
            # Remove unused objects and compress streams
            pdf.save(output_pdf, linearize=True)
        print(f"PDF comprimido salvo em: {output_path}")
    except Exception as e:
        print(f"Erro ao comprimir o PDF: {e}")

def main():
    """
    Main function to select a PDF file and compress it.
    """
    root = Tk()
    root.withdraw()

    input_path = filedialog.askopenfilename(
        title="Selecione o PDF para comprimir",
        filetypes=[("PDF files", "*.pdf")]
    )

    if not input_path:
        print("Nenhum arquivo selecionado.")
        return

    base, ext = os.path.splitext(input_path)
    output_path = f"{base}_comprimido{ext}"

    print(f"Comprimindo: {input_path}")
    compress_pdf(input_path, output_path)

if __name__ == "__main__":
    main()