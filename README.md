# Compressão de PDF com Tkinter

Este projeto tem como objetivo oferecer uma interface gráfica simples para a compressão de arquivos PDF, utilizando o Ghostscript para reduzir o tamanho dos arquivos. O aplicativo permite ao usuário selecionar um arquivo PDF, escolher um nível de compressão e salvar o arquivo comprimido em um novo local.

## Funcionalidades

* Seleção do arquivo PDF para compressão.
* Escolha do local de saída para o arquivo comprimido.
* Opção de escolher o nível de compressão (screen, ebook, printer, prepress).
* Exibição do tamanho do arquivo original e do tamanho do arquivo comprimido após a compressão.
* Barra de progresso para indicar o andamento da compressão.

## Requisitos

### Dependências

* **Python 3.x**
* **Tkinter** (biblioteca gráfica para a interface de usuário)
* **Ghostscript** (necessário para a compressão de PDFs)

### Instalação do Ghostscript

1. **Windows**: Baixe e instale o Ghostscript [aqui](https://www.ghostscript.com/download/gsdnld.html).
2. **Linux**: Para sistemas baseados em Linux, o Ghostscript pode ser instalado via o seguinte comando:

   ```bash
   sudo apt-get install ghostscript
   ```

Após a instalação do Ghostscript, você deve ajustar o caminho do executável (`gswin64c.exe` no Windows ou `gs` no Linux) no código, conforme explicado no item de erros.

## Como Usar

1. Clone ou baixe este repositório para o seu computador.
2. Instale as dependências necessárias (caso não tenha o Tkinter instalado, ele pode ser instalado junto com o Python).
3. Instale o Ghostscript no seu sistema e ajuste o caminho do executável no código (se necessário).
4. Execute o script `compress_pdf.py` para iniciar a aplicação.
5. Na interface gráfica, selecione um arquivo PDF, escolha o nível de compressão e o local de saída.
6. Clique no botão **Comprimir** para iniciar o processo de compressão. O progresso será exibido na barra de progresso.
7. Após a compressão ser concluída, você verá o novo tamanho do arquivo comprimido.

## Exemplo de uso

1. Selecione o arquivo PDF original.
2. Escolha o local onde deseja salvar o arquivo comprimido.
3. Selecione o nível de compressão (por exemplo, "screen", "ebook", "printer", "prepress").
4. Clique no botão **Comprimir** para iniciar a compressão.
5. A barra de progresso será exibida enquanto o arquivo é comprimido.
6. Quando a compressão terminar, o tamanho do arquivo comprimido será mostrado.

## Estrutura do Projeto

```bash
compress_pdf/
│
├── compress_pdf.py  # Código principal do projeto
├── README.md        # Este arquivo
└── gswin64c.exe     # Executável do Ghostscript (se necessário para Windows)
```

## Problemas Conhecidos

* O caminho do executável do Ghostscript pode precisar ser ajustado dependendo do sistema operacional e da instalação do Ghostscript.
* O aplicativo pode não funcionar corretamente em versões de sistemas operacionais mais antigas, especialmente em sistemas Linux onde o Ghostscript não está instalado corretamente.
