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