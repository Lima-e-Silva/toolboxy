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
        func(*args,**kwargs)

    stats = pstats.Stats(pr)
    stats.sort_stats(pstats.SortKey.TIME)
    stats.dump_stats(filename=f'{filename}.prof')

    os.system(f'snakeviz {filename}.prof')