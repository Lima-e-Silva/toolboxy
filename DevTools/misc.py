def unique_id(length: int,
              letters: bool = True,
              numbers: bool = True,
              upper_case: bool = True,
              lower_case: bool = True,
              blocks: int = 1,
              separator: str = '-'):
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
           output: str = 'QRCode'):
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
    output : str, optional
        The name of the output image file. The default is 'QRCode'.

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
    output : str, opcional
        O nome do arquivo de imagem de saída. O padrão é 'QRCode'.

    Retorna
    -------
    None
    """
    import requests as r

    img = r.get(
        f'https://image-charts.com/chart?chs={size}x{size}&cht=qr&choe=UTF-8&icqrf={color}&chl={url}'
    ).content
    with open(f'{output}.png', 'wb') as file:
        file.write(img)