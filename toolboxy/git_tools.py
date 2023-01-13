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
    os.system(f'pipreqs --encoding utf-8 --force "{filepath}"')