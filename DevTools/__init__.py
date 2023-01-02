# ─── Web Scrapping ────────────────────────────────────────────────────────────


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


# ─── Identificação De Erros ───────────────────────────────────────────────────


def debug_function(function, output: str = "", *args, **kwargs):
    """
    English:
    ----------
    Executes a function with error logging.

    Parameters
    ----------
    function : function
        The function to be executed.
    output : str
        The name of the log file. If not provided, errors will be displayed in the console.
    *args : list
        The arguments to be passed to the function.
    **kwargs : dict
        The keyword arguments to be passed to the function.

    Returns
    -------
    None

    Português (brasileiro):
    ----------
    Executa uma função com logging de erros.

    Parâmetros
    ----------
    function : function
        A função a ser executada.
    output : str
        O nome do arquivo de log. Se não for informado, os erros serão mostrados no console.
    *args : list
        Os argumentos a serem passados para a função.
    **kwargs : dict
        Os argumentos com palavras-chave a serem passados para a função.

    Retorna
    -------
    None
    """
    from loguru import logger as log

    if output != "":
        log.add(f'{output}.log', rotation='10 MB')

    @log.catch
    def f(*args, **kwargs):
        return function(*args, **kwargs)

    f(*args, **kwargs)


# ─── Manipulação De Arquivos ──────────────────────────────────────────────────


def create_cfg(file: str, cfg_dict: dict):
    """
    English:
    ----------
    Creates a configuration file from a dictionary. Note: the names of the options must be lowercase.

    Parameters
    ----------
    file : str
        The path to the configuration file to be created.
    cfg_dict : dict
        The dictionary containing the settings to be written to the file. The key of the dictionary is the name of the section, and the value is a dictionary with the options of the section and their respective values.

    Returns
    -------
    None

    Português (brasileiro):
    ----------
    Cria um arquivo de configuração a partir de um dicionário. Obs.: os nomes das opções devem ser minúsculos.

    Parâmetros
    ----------
    file : str
        O caminho para o arquivo de configuração a ser criado.
    cfg_dict : dict
        O dicionário que contém as configurações a serem escritas no arquivo. A chave do dicionário é o nome da seção, e o valor é um dicionário com as opções da seção e seus respectivos valores.

    Retorna
    -------
    None
    """
    with open(file, 'w') as file:
        for section, options in cfg_dict.items():
            file.write(f'\n[{section}]\n')
            for option, value in options.items():
                file.write(f'{option}={value}\n')


def read_cfg(file: str):
    """
    English:
    ----------
    Reads a .cfg configuration file and returns the options as a dictionary.

    Parameters
    ----------
    file : str
        The name of the configuration file to be read.

    Returns
    -------
    options : dict
        A dictionary containing the options and their values, organized by section.

    Português (brasileiro):
    ----------
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


def backup(file: str, output_path: str = '', backup_name: str = ''):
    """
    English:
    ----------
    Makes a backup of a file.

    Parameters
    ----------
    file : str
        The path to the file that will be copied.
    output_path : str
        The path where the backup will be saved. The default is an empty string.
    backup_name : str
        The name of the backup. If not provided, the name will be the current date and time.

    Returns
    -------
    None

    Português (brasileiro):
    ----------
    Realiza uma cópia de segurança de um arquivo.

    Parâmetros
    ----------
    file : str
        O caminho para o arquivo que será copiado.
    output_path : str
        O caminho onde a cópia de segurança será salva. O padrão é uma string vazia.
    backup_name : str
        O nome da cópia de segurança. Se não for informado, o nome será a data e hora atual.

    Retorna
    -------
    None
    """
    import shutil

    if backup_name == '':
        from datetime import datetime

        try:
            extension = file[file.rindex('.'):]
        except ValueError:
            extension = ''

        backup_name = datetime.now().strftime("%Y-%m-%d %Hh%M") + extension

    if len(output_path) > 0 and (output_path[-1] != '\\'
                                 or output_path[-1] != '/'):
        output_path += '/'

    try:
        shutil.copy(file, output_path + backup_name)
    except FileNotFoundError:
        try:
            import os

            os.makedirs(output_path)
        except PermissionError:
            print(
                'Caminho informado não existe. Criação de diretório não foi autorizado.\nAjuste a permissão do algoritmo ou crie manualmente a pasta de destino.'
            )
    finally:
        shutil.copy(file, output_path + backup_name)


def check_hash(*files):
    """
    English:
    ----------
    Checks the integrity of multiple files by comparing their hashes, or returns the hash if a single file is provided.

    Parameters
    ----------
    *files : list
        The path to the files to be checked.

    Returns
    -------
    bool (if more than one file was provided)
        If the check was successful.
    str (if a single file was provided)
        The hash of the provided file.

    Português (brasileiro):
    ----------
    Verifica a integridade de vários arquivos comparando seus hashes, ou retorna o hash caso um único arquivo seja informado.

    Parâmetros
    ----------
    *files : list
        O caminho para os arquivos a serem verificados.

    Retorna
    -------
    bool (caso mais de um arquivo tiver sido fornecido)
        Se a verificação foi realizada com sucesso.
    str (caso um único arquivo foi fornecido)
        O hash do arquivo informado.
    """
    import hashlib

    if len(files) > 1:
        for file in files:
            with open(file, 'rb') as f:
                h = hashlib.sha256()
                h.update(f.read())
                try:
                    if hash == h.digest():
                        continue
                    else:
                        return False
                except UnboundLocalError:
                    hash = h.digest()
                    continue
        return True

    else:
        with open(files[0], 'rb') as f:
            h = hashlib.sha256()
            h.update(f.read())
            hash = h.hexdigest()
            return hash

#todo: Testes
# ─── Ferramentas Git ──────────────────────────────────────────────────────────


def create_env(env_name: str = ".venv"):
    """
    English:
    ----------
    Creates a virtual environment with the given name.

    Parameters
    ----------
    env_name : str
        The name of the virtual environment. The default is '.venv'.

    Returns
    -------
    None

    Português (brasileiro):
    ----------
    Cria um ambiente virtual com o nome informado.

    Parâmetros
    ----------
    env_name : str
        O nome do ambiente virtual. O padrão é '.venv'.

    Retorna
    -------
    None
    """
    import os

    os.system(f'python -m venv "{env_name}"')


def license(license_type: str, name: str, year: str | int = ""):
    """
    English:
    ----------
    Generates a license file.

    Parameters
    ----------
    license_type : str
        The type of license. Options: 'mit' or 'mozilla'.
    name : str
        The name of the license author.
    year : str or int
        The year in which the license was generated. The default is the current year.

    Returns
    -------
    None

    Português (brasileiro):
    ----------
    Gera um arquivo de licença.

    Parâmetros
    ----------
    license_type : str
        O tipo de licença. Opções: 'mit' ou 'mozilla'.
    name : str
        O nome do autor da licença.
    year : str ou int
        O ano em que a licença foi gerada. O padrão é o ano atual.

    Retorna
    -------
    None
    """
    import requests as re
    from bs4 import BeautifulSoup
    from loguru import logger as log

    licenses = {"mit": "mit", "mozilla": "mpl-2.0"}

    if year == "":
        from datetime import datetime
        year = datetime.now().year

    try:
        source = BeautifulSoup(re.get(
            f'https://choosealicense.com/licenses/{licenses[f"{license_type.lower()}"]}/'
        ).text,
                               features="lxml")
        license_str = source.find('pre').text
        license_str = license_str.replace('[fullname]', name)
        license_str = license_str.replace('[year]', str(year))
    except Exception as e:
        log.error(e)

    with open('LICENSE', 'w') as file:
        file.write(license_str)


def git_ignore(folders: list = [], extensions: list = []):
    """
    English:
    ----------
    Creates a .gitignore file with the specified folders and extensions.

    Parameters
    ----------
    folders : list
        A list of folders that should be ignored by git. The default is an empty list.
    extensions : list
        A list of file extensions that should be ignored by git. The default is an empty list.

    Returns
    -------
    None

    Português (brasileiro):
    ----------
    Cria um arquivo .gitignore com as pastas e extensões informadas.

    Parâmetros
    ----------
    folders : list
        Uma lista de pastas que devem ser ignoradas pelo git. O padrão é uma lista vazia.
    extensions : list
        Uma lista de extensões de arquivos que devem ser ignoradas pelo git. O padrão é uma lista vazia.

    Retorna
    -------
    None
    """
    import requests as re

    folders_str = '\n'
    for folder in folders:
        folders_str += folder + '/' + '\n'

    extensions_str = '\n'
    for extension in extensions:
        extensions_str += f'*.{extension}\n'

    ignore_str = re.get('https://raw.githubusercontent.com/github/gitignore/main/Python.gitignore').text

    with open('.gitignore', 'w') as file:
        file.write(ignore_str+folders_str+extensions_str)


def requirements():
    """
    English:
    ----------
    Runs the 'pipreqs' command to generate a 'requirements.txt' file with all project dependencies.

    Returns
    -------
    None

    Português (brasileiro):
    ----------
    Executa o comando 'pipreqs' para gerar um arquivo 'requirements.txt' com todas as dependências do projeto.

    Retorna
    -------
    None
    """
    import os
    import pipreqs
    
    filepath = os.getcwd()
    os.system(f'pipreqs --encoding utf-8 --force {filepath}')

#todo: Testes
# ─── Ferramentas Windows ──────────────────────────────────────────────────────


def notify(**kwargs):
    """
    English:
    ----------
    Displays a notification with the specified parameters.

    Parameters
    ----------
    id : str, optional
        The ID of the application sending the notification.
    title : str, optional
        The title of the notification.
    message : str, optional
        The message of the notification.
    icon : str, optional
        The path to the icon to be displayed with the notification.
    duration : str, optional
        The duration of the notification. Possible values: 'long' or 'short'.
    link : str, optional
        The link to be opened when the notification is clicked.
    buttons : dict, optional
        A dictionary with the labels and links of the buttons to be displayed in the notification.
    sound : bool, optional
        If a sound should be played when the notification is displayed.
    audio_loop : bool, optional
        If the sound should be played in a loop when it is played.

    Returns
    -------
    None

    Português (brasileiro):
    ----------
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


def shutdown(time: int | str, message: str = ''):
    """
    English:
    ----------
    Shutdowns the computer. The user can specify the time until the shutdown (in seconds) and a message to be displayed.

    Parameters
    ----------
    time: int or str
        The time until the shutdown, in seconds.
    message: str, optional
        A message to be displayed. Defaults to an empty string.

    Returns
    -------
    None

    Português (brasileiro):
    ----------
    Desliga o computador. O usuário pode especificar o tempo até o desligamento (em segundos) e uma mensagem a ser exibida.

    Parâmetros
    ----------
    time: int ou str
        O tempo até o desligamento, em segundos.
    message: str, optional
        Uma mensagem a ser exibida. Padrão é uma string vazia.

    Retorna
    -------
    None
    """
    import subprocess

    command = f'shutdown -s -t {time}'
    if message != "":
        command += f' -c "{message}"'

    subprocess.run(command,
                   shell=True,
                   check=True,
                   stdout=subprocess.PIPE,
                   stderr=subprocess.PIPE)


# ─── Otimização ───────────────────────────────────────────────────────────────


def prof(filename: str, func, *args, **kwargs):
    """
    English:
    ----------
    Runs a function and generates a performance profile of it.

    Parameters
    ----------
    filename : str
        The name of the file where the performance profile will be saved. Ex.: "profiling".
    func : function
        The function that will be executed and profiled.
    *args : tuple
        The arguments to be passed to the function.
    **kwargs : dict
        The keyword arguments to be passed to the function.

    Returns
    -------
    None
        There is no return. The performance profile is saved to a file and opened in the 'snakeviz' performance profile viewer.

    Português (brasileiro):
    ----------
    Executa uma função e gera um perfil de desempenho dela.

    Parâmetros
    ----------
    filename : str
        O nome do arquivo onde o perfil de desempenho será salvo. Ex.: "profiling".
    func : function
        A função que será executada e perfilada.
    *args : tuple
        Os argumentos a serem passados para a função.
    **kwargs : dict
        Os argumentos com palavras-chave a serem passados para a função.

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
        func(*args,**kwargs)

    stats = pstats.Stats(pr)
    stats.sort_stats(pstats.SortKey.TIME)
    stats.dump_stats(filename=f'{filename}.prof')

    os.system(f'snakeviz {filename}.prof')


# ─── Misc ─────────────────────────────────────────────────────────────────────


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

#todo: Testes
# ─── APIs ─────────────────────────────────────────────────────────────────────


def smartphone_notify(topic: str,
                      message: str,
                      title: str,
                      tags: list = [],
                      priority: int = 3,
                      attach: str = '',
                      filename: str = '',
                      click: str = '',
                      actions: list = [],
                      email:str=''):
    """English:
    ----------
    Sends a notification to a smartphone. The user can specify the topic, message, title, and tags of the notification, as well as the priority, attachment, filename, and click action. The user can also specify a list of actions to be included in the notification.

    Parameters
    ----------
    topic: str
        The topic of the notification.
    message: str
        The message of the notification.
    title: str
        The title of the notification.
    tags: list, optional
        A list of tags to be included in the notification. Defaults to an empty list.
    priority: int, optional
        The priority of the notification. Defaults to 3.
    attach: str, optional
        The attachment of the notification. Defaults to an empty string.
    filename: str, optional
        The filename of the attachment. Defaults to an empty string.
    click: str, optional
        The click action of the notification. Defaults to an empty string.
    actions: list, optional
        A list of actions to be included in the notification. Defaults to an empty list.
    email: str, optional
        The email of the user to whom the notification will be sent. Defaults to an empty string.

    Returns
    -------
    bool
        True if notification was successful, False in other case.

    Português (brasileiro):
    ----------
    Envia uma notificação para um smartphone. O usuário pode especificar o tópico, a mensagem, o título e as tags da notificação, assim como a prioridade, o anexo, o nome do arquivo e a ação de clique. O usuário também pode especificar uma lista de ações a serem incluídas na notificação.

    Parâmetros
    ----------
    topic: str
        O tópico da notificação.
    message: str
        A mensagem da notificação.
    title: str
        O título da notificação.
    tags: list, optional
        Uma lista de tags a serem incluídas na notificação. Padrão é uma lista vazia.
    priority: int, optional
        A prioridade da notificação. Padrão é 3.
    attach: str, optional
        O anexo da notificação. Padrão é uma string vazia.
    filename: str, optional
        O nome do arquivo do anexo. Padrão é uma string vazia.
    click: str, optional
        A ação de clique da notificação. Padrão é uma string vazia.
    actions: list, optional
        Uma lista de ações a serem incluídas na notificação. Padrão é uma lista vazia.
    email: str, optional
        O email do usuário a quem a notificação será enviada. Padrão é uma string vazia.

    Retorna
    -------
    bool
        True se a notificação foi submetida com sucesso, False caso contrário.
    """
    import requests as re
    import json

    data = {
        'topic': topic,
        'message': message,
        'title': title,
        'tags': tags,
        'priority': priority,
        'attach': attach,
        'filename': filename,
        'click': click,
        'actions': actions,
        'email' : email
    }

    response = re.post('https://ntfy.sh/',data=json.dumps(data))
    if response.status_code != 200:
        return False

    return True


def short_url(url: str):
    """
    English:
    ----------
    Shortens a URL.

    Parameters
    ----------
    url: str
        The URL to be shortened.

    Returns
    -------
    short_url: str
        The shortened URL.

    Português (brasileiro):
    ----------
    Encurta uma URL.

    Parâmetros
    ----------
    url: str
        A URL a ser encurtada.

    Retorna
    -------
    short_url: str
        A URL encurtada.
    """
    import requests as re

    response = re.post('https://gotiny.cc/api', json={'input': url})

    if response.status_code != 200:
        return False

    return f"https://gotiny.cc/{response.json()[0]['code']}"

if __name__ == '__main__':
    requirements()