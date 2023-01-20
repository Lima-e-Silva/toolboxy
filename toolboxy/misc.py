def delay_print(string: str, wpm=180) -> None:
    """
    English
    --------
    Prints a string with a delay.

    Parameters
    ----------
    string : str
        The string to be printed.
    wpm : int, optional
        The word per minute speed. The default is 180.
    
    Returns
    -------
    None.

    Português (brasileiro)
    -------
    Imprime uma string com um delay.

    Parâmetros
    ----------
    string : str
        A string a ser impressa.
    wpm : int, optional
        A velocidade de impressão em palavras por minuto. O padrão é 180.
    
    Retorna
    -------
    None.
    """
    import sys
    import time

    words_count = len(string.split())
    total_time = (words_count / wpm) * 60
    letter_time = total_time / len(string)
    for letter in string:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(letter_time)

    print('')


def gpt_docstring(func,
                  api_key: str = "",
                  max_tokens: int = 500,
                  show_cost: bool = False):
    """
    English:
    ----------
    Generates a docstring for the given function and copy to the clipboard.

    Parameters
    ----------
    func: function
        Function to generate the docstring.
    api_key: str, optional
        OpenAI API key.
    max_tokens: int, optional
        Maximum number of tokens to generate.
    show_cost: bool, optional
        Show the cost of the request.

    Returns
    -------
    docstring: str
        The generated docstring.

    Português (brasileiro):
    ----------
    Gera uma docstring para a função informada e a copia para a área de transferência.

    Parâmetros
    ----------
    func: function
        Função para gerar a docstring.
    api_key: str, opcional
        Chave da API do OpenAI.
    max_tokens: int, opcional
        Número máximo de tokens para gerar.
    show_cost: bool, opcional
        Mostra o custo da requisição.

    Retorna
    -------
    docstring: str
        A docstring gerada.
    """
    import inspect
    import openai
    import pyperclip

    if api_key == "":
        from dotenv import load_dotenv
        import os

        load_dotenv()
        api_key = os.environ.get('OPENAI_API_KEY')

    code = inspect.getsource(func)
    prompt = f"""
Crie docstrings em inglês e português semelhante ao exemplo abaixo, para a função informada. Seja sucinto.

\"""
English:
----------
Runs the 'pipreqs' command to generate a 'requirements.txt' file with dependencies.

Returns
-------
None

Português (brasileiro):
----------
Executa o comando 'pipreqs' para gerar um arquivo 'requirements.txt' com as dependências.

Retorna
-------
None
\"""

Função:
{code}
    """
    openai.api_key = api_key
    response = openai.Completion.create(
        model='text-davinci-003',
        prompt=prompt,
        max_tokens=max_tokens,
        temperature=0.1,
    )
    docstring = response['choices'][0]['text']
    pyperclip.copy(docstring)

    if show_cost:
        from loguru import logger as log

        cost = f"${round((response['usage']['total_tokens'] / 1000) * 0.02,4)}"
        log.success(f'[Cost]: {cost}')

    return docstring


def unique_id(length: int,
              letters: bool = True,
              numbers: bool = True,
              upper_case: bool = True,
              lower_case: bool = True,
              blocks: int = 1,
              separator: str = '-') -> str:
    """
    English:
    ----------
    Generates a unique id string. The id is composed of randomly generated characters, which can be letters or numbers (or both). The user can specify the length of each block of characters, the number of blocks, and the separator to be used between them.

    Parameters
    ----------
    length: int
        The number of characters in each block.
    letters: bool, optional
        Whether to include letters in the id string. Defaults to True.
    numbers: bool, optional
        Whether to include numbers in the id string. Defaults to True.
    upper_case: bool, optional
        Whether to include upper-case letters in the id string. Defaults to True.
    lower_case: bool, optional
        Whether to include lower-case letters in the id string. Defaults to True.
    blocks: int, optional
        The number of blocks of characters in the id string. Defaults to 1.
    separator: str, optional
        The separator to be used between blocks. Defaults to '-'.

    Returns
    -------
    uid: str
        The unique id string.

    Português (brasileiro):
    ----------
    Gera uma string de identificação única. A id é composta por caracteres gerados aleatoriamente, que podem ser letras ou números (ou ambos). O usuário pode especificar o tamanho de cada bloco de caracteres, o número de blocos e o separador a ser usado entre eles.

    Parâmetros
    ----------
    length: int
        O número de caracteres em cada bloco.
    letters: bool, optional
        Se deve incluir letras na string de id. Padrão é True.
    numbers: bool, optional
        Se deve incluir números na string de id. Padrão é True.
    upper_case: bool, optional
        Se deve incluir letras maiúsculas na string de id. Padrão é True.
    lower_case: bool, optional
        Se deve incluir letras minúsculas na string de id. Padrão é True.
    blocks: int, optional
        O número de blocos de caracteres na string de id. Padrão é 1.
    separator: str, optional
        O separador a ser usado entre os blocos. Padrão é '-'.

    Retorna
    -------
    uid: str
        A string de identificação única.
    """
    from random import sample

    letters_str = 'abcdefghijklmnopqrstuvwxyz'
    numbers_str = '0123456789'
    possibilities = ''
    uid = list()

    if letters:
        if lower_case: possibilities += letters_str
        if upper_case: possibilities += letters_str.upper()
    if numbers: possibilities += numbers_str

    for n in range(blocks):
        result = ''.join(sample(possibilities, length))
        uid.append(result)

    return separator.join(uid)


def QRcode(url: str,
           size: int = 150,
           color: str = '000000',
           bg_color: str = 'ffffff',
           output: str = 'QRCode',
           format: str = 'png') -> None:
    """
    English:
    ----------
    Generates a QR code from a URL and saves it to an image file.

    Parameters
    ----------
    url : str
        The URL to be encoded in the QR code.
    size : int, optional
        The size of the QR code in pixels. The default is 150.
    color : str, optional
        The color of the QR code in hexadecimal format. The default is '000000' (black).
    bg_color : str, optional
        The background color of the QR code in hexadecimal format. The default is 'ffffff' (white).
    output : str, optional
        The name of the output image file. The default is 'QRCode'.
    format : str, optional
        The format of the output image file (png or svg). The default is 'png'.

    Returns
    -------
    None

    Português (brasileiro):
    ----------
    Gera um QR code a partir de uma URL e salva-o em um arquivo de imagem.

    Parâmetros
    ----------
    url : str
        A URL a ser codificada no QR code.
    size : int, opcional
        O tamanho do QR code em pixels. O padrão é 150.
    color : str, opcional
        A cor do QR code em formato hexadecimal. O padrão é '000000' (preto).
    bg_color : str, opcional
        A cor do background do QR code em formato hexadecimal. O padrão é 'ffffff' (branco).
    output : str, opcional
        O nome do arquivo de imagem de saída. O padrão é 'QRCode'.
    format : str, opcional
        O formato do arquivo de saída (png ou svg). O padrão é 'png'.

    Retorna
    -------
    None
    """
    import requests as r

    img = r.get(
        f'https://image-charts.com/chart?chs={size}x{size}&cht=qr&choe=UTF-8&icqrf={color}&icqrb={bg_color}&chl={url}'
    ).content
    with open(f'{output}.{format}', 'wb') as file:
        file.write(img)