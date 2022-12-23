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

  Returns
  -------
  unique_id : str
      O identificador único gerado, no formato "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx".
  """

  import uuid
  return uuid.uuid4()


def read_cfg(file: str):
    """
    Lê um arquivo de configuração no formato .cfg e retorna as opções como um dicionário.

    Parameters
    ----------
    file : str
        O nome do arquivo de configuração a ser lido.

    Returns
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

if __name__ == '__main__':
    pass