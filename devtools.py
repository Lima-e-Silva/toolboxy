def chrome2dict(headers_path: str):
    """
    Esta função converte os cabeçalhos de uma solicitação do Chrome em um dicionário.
    
    Parâmetros
    ----------
    headers_path : str
        O caminho para o arquivo que contém os cabeçalhos a serem convertidos.
        
    Retorna
    -------
    dict
        Um dicionário contendo os cabeçalhos da solicitação do Chrome.
    """
    with open(headers_path, 'r') as raw_headers:
        return dict([[
            h.strip('\n').partition(': ')[0],
            h.strip('\n').partition(': ')[2]
        ] for h in raw_headers.readlines()])


def html2txt(response, output_path: str, exit_command: bool = False):
    """
    Esta função converte uma resposta HTML em texto simples e salva no caminho de saída especificado.
    
    Parâmetros
    ----------
    response : object
        A resposta HTML a ser convertida.
    output_path : str
        O caminho onde o texto convertido deve ser salvo.
    exit_command : bool, opcional
        Uma flag indicando se o programa deve sair depois de escrever a saída. O valor padrão é False.
        
    Retorna
    -------
    None
    """
    from sys import exit
    from bs4 import BeautifulSoup

    with open(output_path, 'w', encoding='utf-8') as output:
        output.write(BeautifulSoup(response.text, features='lxml').prettify())

    if exit_command == True: exit()


def unique_id():
    """
    Gera um identificador único aleatório no formato UUID.

    Retorna
    -------
    unique_id : str
        O identificador único gerado, no formato "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx".
    """

    import uuid
    return uuid.uuid4()


def create_cfg(file: str, cfg_dict: dict):
    """
    Cria um arquivo de configuração baseado em um dicionário de configuração.

    Parâmetros:
    ----------
    file (str): O caminho do arquivo a ser criado.
    cfg_dict (dict): O dicionário contendo as configurações a serem escritas no arquivo de configuração. Deve ser no formato {seção: {opção: valor}}.

    Retorna
    -------
    None

    Exemplo:
    ----------
    cfg_dict = {'section1': {'option1': 'value1', 'option2': 'value2'}, 'section2': {'option3': 'value3'}}
    create_cfg('config.cfg', cfg_dict)
    """
    with open(file, 'w') as file:
        for section, options in cfg_dict.items():
            file.write(f'\n[{section}]\n')
            for option, value in options.items():
                file.write(f'{option}={value}\n')


def read_cfg(file: str):
    """
    Lê um arquivo de configuração no formato .cfg e retorna as opções como um dicionário.

    Parâmetros
    ----------
    file : str
        O nome do arquivo de configuração a ser lido.

    Retorna
    -------
    options : dict
        Um dicionário contendo as opções e seus valores, organizados por seção.
    """
    from configparser import ConfigParser

    config = ConfigParser()

    config.read(file)
    sections = config.sections()

    sections_dict = dict()
    for section in sections:
        options = config.options(section)
        options_dict = dict()

        for option in options:
            value = config.get(section, option)
            options_dict[option] = value

        sections_dict[section] = options_dict

    return sections_dict


def backup(file: str, output_path: str):
    """
    Esta função cria uma cópia de segurança do arquivo especificado copiando-o para o caminho de saída especificado.
    
    Parâmetros
    ----------
    file : str
        O caminho para o arquivo que será copiado.
    output_path : str
        O caminho onde a cópia de segurança será salva.
        
    Retorna
    -------
    None
    """
    import shutil
    shutil.copy(file, output_path)


def QRcode(url: str,
           size: int = 150,
           color: str = '000000',
           output: str = 'QRCode'):
    """
    Gera um QR code a partir de uma URL e salva-o em um arquivo de imagem.
    
    Parâmetros
    ----------
    url : str
        A URL a ser codificada no QR code.
    size : int, optional
        O tamanho do QR code em pixels. O padrão é 150.
    color : str, optional
        A cor do QR code em formato hexadecimal. O padrão é '000000' (preto).
    output : str, optional
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


def requirements():
    """
    Executa o comando 'pipreqs' para gerar um arquivo 'requirements.txt' com todas as dependências do projeto.
    
    Retorna
    -------
    None
    """
    import os
    filepath = os.getcwd()
    os.system(f'pipreqs --encoding utf-8 --force {filepath}')


def notify(**kwargs):
    """
    Exibe uma notificação com os parâmetros especificados.

    Parâmetros
    ----------
    id : str, opcional
        O ID da aplicação que está enviando a notificação.
    title : str, opcional
        O título da notificação.
    message : str, opcional
        A mensagem da notificação.
    icon : str, opcional
        O caminho para o ícone a ser exibido com a notificação.
    duration : str, opcional
        A duração da notificação. Valores possíveis: 'long' ou 'short'.
    link : str, opcional
        O link a ser aberto quando a notificação for clicada.
    buttons : dict, opcional
        Um dicionário com os rótulos e links dos botões a serem exibidos na notificação.
    sound : bool, opcional
        Se deve reproduzir um som quando a notificação for exibida.
    audio_loop : bool, opcional
        Se o som deve ser reproduzido em loop quando for reproduzido.
    
    Retorna
    -------
    None
    """

    from winotify import Notification, audio

    app_id = kwargs.get('id', 'Python')
    title = kwargs.get('title', 'Title')
    message = kwargs.get('message', '')
    icon = kwargs.get('icon', '')
    duration = kwargs.get('duration', 'long')
    link = kwargs.get('link', '')
    buttons = kwargs.get('buttons', '')

    sound = kwargs.get('sound', True)
    loop = kwargs.get('audio_loop', False)

    Popup = Notification(app_id=app_id,
                         title=title,
                         msg=message,
                         icon=icon,
                         duration=duration,
                         launch=link)

    if type(buttons) == dict:
        for key in buttons:
            Popup.add_actions(label=key, launch=buttons[key])

    if sound == True: Popup.set_audio(audio.Default, loop=loop)

    Popup.show()


def prof(filename: str, func, *args):
    """
    Executa uma função e gera um perfil de desempenho dela.
    
    Parâmetros
    ----------
    filename : str
        O nome do arquivo onde o perfil de desempenho será salvo.
    func : function
        A função que será executada e perfilada.
    *args : tuple
        Os argumentos a serem passados para a função.

    Retorna
    -------
    None
        Não há retorno. O perfil de desempenho é salvo em um arquivo e aberto no visualizador de perfil de desempenho 'snakeviz'.
    """
    import snakeviz
    import cProfile
    import pstats
    import os

    with cProfile.Profile() as pr:
        func(*args)

    stats = pstats.Stats(pr)
    stats.sort_stats(pstats.SortKey.TIME)
    stats.dump_stats(filename=f'{filename}.prof')

    os.system(f'snakeviz {filename}.prof')


if __name__ == '__main__':
    requirements()