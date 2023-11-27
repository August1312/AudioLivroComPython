# Leitor de PDF com Síntese de Voz em Python

Este script em Python utiliza as bibliotecas PyPDF2 e pyttsx3 para realizar a leitura de um arquivo PDF com síntese de voz. A seguir, uma descrição passo a passo do que o código faz:

## Passos:

1. **Importação de Bibliotecas:**
   - `import PyPDF2`: Importa a biblioteca PyPDF2, que fornece funcionalidades para trabalhar com arquivos PDF.
   - `import pyttsx3`: Importa a biblioteca pyttsx3, que é um wrapper para o mecanismo de síntese de voz Text-to-Speech (TTS).

2. **Abertura do Arquivo PDF:**
   - `path = open('Introdução ao Python.pdf', 'rb')`: Abre o arquivo PDF chamado "Introdução ao Python.pdf" em modo de leitura binária.

3. **Leitura do PDF:**
   - `pdf_reader = PyPDF2.PdfReader(path)`: Cria um objeto PdfReader para ler o arquivo PDF.

4. **Inicialização do Módulo de Voz:**
   - `speak = pyttsx3.init()`: Inicializa o módulo Text-to-Speech para a leitura de texto em voz.

5. **Iteração sobre Páginas do PDF:**
   - `for page in range(len(pdf_reader.pages)):`: Itera sobre cada página do PDF.
   - `text = pdf_reader.pages[page].extract_text()`: Extrai o texto da página atual.

6. **Leitura em Voz:**
   - `speak.say(text)`: Faz a leitura em voz do texto extraído da página.
   - `speak.runAndWait()`: Aguarda até que a leitura seja concluída antes de prosseguir para a próxima página.

7. **Finalização da Leitura em Voz:**
   - `speak.stop()`: Encerra a leitura em voz após a conclusão da iteração.

Lembre-se de que este código depende das bibliotecas PyPDF2 e pyttsx3, e você precisa instalá-las antes de executar o script. O código extrai o texto de cada página do arquivo PDF e usa a biblioteca pyttsx3 para transformar esse texto em fala, permitindo que o conteúdo do PDF seja ouvido. Certifique-se de que o arquivo PDF e as bibliotecas necessárias estejam disponíveis no ambiente de execução.
   - 'pip install PyPDF2'
   - 'pip install pyttsx3' 
   - 'pip install python'
