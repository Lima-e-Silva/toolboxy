# ─── Web Scrapping ────────────────────────────────────────────────────────────


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


def html2txt(url: str = '',
             response='',
             output_path: str = 'output.txt',
             exit_flag: bool = False,
             headers: dict = {},
             params: dict = {}):
    """
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
    url = 'https://httpbin.org/ip'
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
    Cria um arquivo de configuração a partir de um dicionário.

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


# ─── Ferramentas Git ──────────────────────────────────────────────────────────


def create_env(env_name: str = ".venv"):
    """
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
    folders_str = ''
    for folder in folders:
        folders_str += folder + '/' + '\n'

    extensions_str = ''
    for extension in extensions:
        extensions_str += f'*.{extension}\n'

    ignore_str = f"""# Byte-compiled / optimized / DLL files
__pycache__/
*.py[cod]
*$py.class

# C extensions
*.so

# Distribution / packaging
.Python
build/
develop-eggs/
dist/
downloads/
eggs/
.eggs/
lib/
lib64/
parts/
sdist/
var/
wheels/
pip-wheel-metadata/
share/python-wheels/
*.egg-info/
.installed.cfg
*.egg
MANIFEST

# PyInstaller
#  Usually these files are written by a python script from a template
#  before PyInstaller builds the exe, so as to inject date/other infos into it.
*.manifest
*.spec

# Installer logs
pip-log.txt
pip-delete-this-directory.txt

# Unit test / coverage reports
htmlcov/
.tox/
.nox/
.coverage
.coverage.*
.cache
nosetests.xml
coverage.xml
*.cover
*.py,cover
.hypothesis/
.pytest_cache/

# Translations
*.mo
*.pot

# Django stuff:
*.log
local_settings.py
db.sqlite3
db.sqlite3-journal

# Flask stuff:
instance/
.webassets-cache

# Scrapy stuff:
.scrapy

# Sphinx documentation
docs/_build/

# PyBuilder
target/

# Jupyter Notebook
.ipynb_checkpoints

# IPython
profile_default/
ipython_config.py

# pyenv
.python-version

# pipenv
#   According to pypa/pipenv#598, it is recommended to include Pipfile.lock in version control.
#   However, in case of collaboration, if having platform-specific dependencies or dependencies
#   having no cross-platform support, pipenv may install dependencies that don't work, or not
#   install all needed dependencies.
#Pipfile.lock

# PEP 582; used by e.g. github.com/David-OConnor/pyflow
__pypackages__/

# Celery stuff
celerybeat-schedule
celerybeat.pid

# SageMath parsed files
*.sage.py

# Environments
.env
.venv
env/
venv/
ENV/
env.bak/
venv.bak/

# Spyder project settings
.spyderproject
.spyproject

# Rope project settings
.ropeproject

# mkdocs documentation
/site

# mypy
.mypy_cache/
.dmypy.json
dmypy.json

# Pyre type checker
.pyre/
{extensions_str}

# Pastas
{folders_str}
    """
    with open('.gitignore', 'w') as file:
        file.write(ignore_str)


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


# ─── Ferramentas Windows ──────────────────────────────────────────────────────


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


# ─── Otimização ───────────────────────────────────────────────────────────────


def prof(filename: str, func, *args):
    """
    Executa uma função e gera um perfil de desempenho dela.
    
    Parâmetros
    ----------
    filename : str
        O nome do arquivo onde o perfil de desempenho será salvo. Ex.: "profiling".
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


# ─── Misc ─────────────────────────────────────────────────────────────────────


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


if __name__ == '__main__':
    requirements()