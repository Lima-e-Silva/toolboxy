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