def chrome2dict(headers_path: str = "", headers_str: str = ""):
    """
    English:
    ----------
    This function converts Chrome request headers (in string or saved in files) into a dictionary.

    Parameters
    ----------
    headers_path : str
        The path to the headers file. The default is an empty string.
    headers_str : str
        The string containing the headers. The default is an empty string.

    Returns
    -------
    dict
        The dictionary containing the headers.

    Português (brasileiro):
    ----------
    Esta função converte os cabeçalhos de uma solicitação do Chrome (em string ou salvos em arquivos) em um dicionário.

    Parâmetros
    ----------
    headers_path : str
        O caminho para o arquivo de cabeçalhos. O padrão é uma string vazia.
    headers_str : str
        A string contendo os cabeçalhos. O padrão é uma string vazia.

    Retorna
    -------
    dict
        O dicionário contendo os cabeçalhos.
    """
    if headers_path == "" and headers_str == "":
        raise AttributeError(
            "Necessário informar o caminho do arquivo com cabeçalho ou a própria string do cabeçalho"
        )

    elif headers_path != "":
        with open(headers_path, 'r') as raw_headers:
            return dict([[
                h.strip('\n').partition(': ')[0],
                h.strip('\n').partition(': ')[2]
            ] for h in raw_headers.readlines()])

    else:
        return dict([[
            h.partition(': ')[0],
            h.partition(': ')[2]
        ] for h in headers_str.split('\n')])


def html2txt(url: str = '',
             response='',
             output_path: str = 'output.txt',
             exit_flag: bool = False,
             headers: dict = {},
             params: dict = {}):
    """
    English:
    ----------
    Converts the HTML content of a URL or requests response into text.

    Parameters
    ----------
    url : str
        The URL of the HTML file to be converted. The default is an empty string.
    response : str
        The requests response containing the HTML content to be converted. The default is an empty string.
    output_path : str
        The path and name of the output file. The default is 'output.txt'.
    exit_flag : bool
        If True, ends the program after conversion. The default is False.
    headers : dict
        The header settings of the request. The default is an empty dictionary.
    params : dict
        The parameters of the request. The default is an empty dictionary.

    Returns
    -------
    None

    Português (brasileiro):
    ----------
    Converte o conteúdo HTML de uma URL ou resposta do requests em texto.

    Parâmetros
    ----------
    url : str
        A URL do arquivo HTML a ser convertido. O padrão é uma string vazia.
    response : str
        A resposta do requests contendo o conteúdo HTML a ser convertido. O padrão é uma string vazia.
    output_path : str
        O caminho e nome do arquivo de saída. O padrão é 'output.txt'.
    exit_flag : bool
        Se True, encerra o programa após a conversão. O padrão é False.
    headers : dict
        As configurações de cabeçalho da requisição. O padrão é um dicionário vazio.
    params : dict
        Os parâmetros da requisição. O padrão é um dicionário vazio.

    Retorna
    -------
    None
    """
    from bs4 import BeautifulSoup

    if url == '' and response == '':
        raise AttributeError(
            "Necessário informar a URL ou a resposta (requests)")
    elif url != '':
        import requests as re

        response = re.get(url, headers=headers, params=params)

    with open(output_path, 'w', encoding='utf-8') as output:
        output.write(BeautifulSoup(response.text, features='lxml').prettify())

    if exit_flag == True:
        from sys import exit

        exit()


def verify_proxy(ip: str, port: str | int, timeout: int = 5, verbose: int = 1):
    """
    English:
    ----------
    This function checks if a given IP address and port can be used as a proxy.

    Parameters
    ----------
    ip : str
        The IP address of the proxy.
    port : str or int
        The port of the proxy.
    timeout : int, optional
        The maximum wait time for the connection to the proxy to be established. The default is 5 seconds.
    verbose : int, optional
        If 1, displays log messages with information about exceptions that occurred during proxy check. The default is 1.

    Returns
    -------
    bool
        True if the proxy is valid, False otherwise.

    Português (brasileiro):
    ----------
    Esta função verifica se um determinado endereço IP e porta podem ser usados como proxy.

    Parâmetros
    ----------
    ip : str
        O endereço IP do proxy.
    port : str ou int
        A porta do proxy.
    timeout : int, opcional
        O tempo de espera máximo para a conexão com o proxy ser estabelecida. O padrão é 5 segundos.
    verbose : int, opcional
        Se 1, exibe mensagens de log com informações sobre exceções que ocorreram durante a verificação do proxy. O padrão é 1.

    Retorna
    -------
    bool
        True se o proxy é válido, False caso contrário.
    """
    import requests as re
    from loguru import logger as log

    proxy = f'{ip}:{str(port)}'
    try:
        response = re.get('https://httpbin.org/ip',
                          proxies={
                              'http': proxy,
                              'https': proxy
                          },
                          timeout=timeout).json()['origin']
        if response == ip:
            return True
        else:
            return False
    except Exception as e:
        if verbose == 1: log.exception(e)
        return False