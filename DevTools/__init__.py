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


def debug_function(function, *args, output: str = ""):
    """
    Executa uma função com logging de erros.

    Parâmetros
    ----------
    function : function
        A função a ser executada.
    *args : list
        Os argumentos a serem passados para a função.
    output : str
        O nome do arquivo de log. Se não for informado, os erros serão mostrados no console.

    Retorna
    -------
    None
    """
    from loguru import logger as log

    if output != "":
        log.add(f'{output}.log', rotation='10 MB')

    @log.catch
    def f(*args):
        return function(*args)

    f(*args)


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


# ─── Ferramentas Git ──────────────────────────────────────────────────────────


def MIT_license(name: str, year: str | int = ""):
    """
    Cria um arquivo de licença MIT com o nome e ano especificados.

    Parâmetros
    ----------
    name : str
        O nome do titular da licença.
    year : str | int, opcional
        O ano da licença. Se não especificado, o ano atual será usado.

    Retorna
    -------
    None
    """
    from loguru import logger as log

    if year == "":
        from datetime import datetime
        year = datetime.now().year

    license_str = f"""MIT License

Copyright (c) {year} {name}

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
    """

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