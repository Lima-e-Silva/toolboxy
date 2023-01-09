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
    import cProfile
    import os
    import pstats

    import snakeviz

    with cProfile.Profile() as pr:
        func(*args, **kwargs)

    stats = pstats.Stats(pr)
    stats.sort_stats(pstats.SortKey.TIME)
    stats.dump_stats(filename=f'{filename}.prof')

    os.system(f'snakeviz {filename}.prof')


def elapsed_clocktime(func, *args, **kwargs):
    """
    English:
    ----------
    Calculates the elapsed time between the start and end of the execution of a function.

    Parameters
    ----------
    func: function
        The function to be executed.
    *args: tuple
        Positional arguments to be passed to the function.
    **kwargs: dict
        Keyword arguments to be passed to the function.

    Returns
    -------
    elapsed_time: datetime.timedelta
        The elapsed time between the start and end of the function execution.

    Português (brasileiro):
    ----------
    Calcula o tempo decorrido entre o início e o fim da execução de uma função.

    Parâmetros
    ----------
    func: function
        A função a ser executada.
    *args: tuple
        Argumentos posicionais a serem passados para a função.
    **kwargs: dict
        Argumentos de palavra-chave a serem passados para a função.

    Retorna
    -------
    elapsed_time: datetime.timedelta
        O tempo decorrido entre o início e o fim da execução da função.
    """
    from datetime import datetime

    start = datetime.now()
    func(*args, **kwargs)
    end = datetime.now()

    return end - start


def elapsed_cputime(func, *args, **kwargs):
    """
    English:
    ----------
    Display elapsed CPU time between the start and end of the execution of a function.

    Parameters
    ----------
    func: function
        The function to be executed.
    *args: tuple
        Positional arguments to be passed to the function.
    **kwargs: dict
        Keyword arguments to be passed to the function.

    Returns
    -------
    None

    Português (brasileiro):
    ----------
    Exibe o tempo de CPU decorrido entre o início e o fim da execução de uma função.

    Parâmetros
    ----------
    func: function
        A função a ser executada.
    *args: tuple
        Argumentos posicionais a serem passados para a função.
    **kwargs: dict
        Argumentos de palavra-chave a serem passados para a função.

    Retorna
    -------
    None
    """
    import cProfile

    with cProfile.Profile() as pr:
        pr.runcall(func, *args, **kwargs)
        pr.print_stats()