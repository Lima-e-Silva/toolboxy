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