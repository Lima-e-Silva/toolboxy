import toolboxy
import os


def useless_function():
    print('This is a useless function')


def test_delay_print(capsys):
    toolboxy.delay_print('test_delay_print_n1')
    captured = capsys.readouterr()
    assert captured.out == 'test_delay_print_n1\n'

    toolboxy.delay_print('test_delay_print_n2')
    captured = capsys.readouterr()
    assert captured.out == 'test_delay_print_n2\n'


def test_gpt_docstring():
    response = toolboxy.gpt_docstring(useless_function)
    assert response
    assert 'Português (brasileiro)' in response
    assert 'English' in response


def test_uuid():
    letters = 'abcdefghijklmnopqrstuvwxyz'
    numbers = '0123456789'

    uid_1 = toolboxy.unique_id(length=4,
                               letters=True,
                               numbers=True,
                               upper_case=True,
                               lower_case=True,
                               blocks=1,
                               separator='-')

    uid_2 = toolboxy.unique_id(length=4,
                               letters=True,
                               numbers=True,
                               upper_case=True,
                               lower_case=True,
                               blocks=1,
                               separator='-')

    uid_3 = toolboxy.unique_id(length=4,
                               letters=True,
                               numbers=True,
                               upper_case=True,
                               lower_case=True,
                               blocks=1,
                               separator='-')

    block_uid_1 = toolboxy.unique_id(length=4,
                                     letters=False,
                                     numbers=True,
                                     upper_case=True,
                                     lower_case=True,
                                     blocks=2,
                                     separator='-')

    block_uid_2 = toolboxy.unique_id(length=4,
                                     letters=True,
                                     numbers=False,
                                     upper_case=True,
                                     lower_case=False,
                                     blocks=2,
                                     separator='-')

    assert len(uid_1) == 4
    assert len(uid_2) == 4
    assert len(uid_3) == 4
    assert uid_1 != uid_2
    assert uid_1 != uid_3
    assert uid_2 != uid_3

    assert len(block_uid_1) == 9
    assert len(block_uid_2) == 9
    assert block_uid_1 != block_uid_2

    for n in block_uid_1:
        if n == '-': continue
        assert n not in letters
        assert n in numbers

    for n in block_uid_2:
        if n == '-': continue
        assert n not in letters
        assert n.lower() in letters
        assert n not in numbers


def test_qrcode():
    url = 'https://www.google.com.br'
    toolboxy.QRcode(url=url)

    assert 'QRCode.png' in os.listdir()
    assert os.stat('QRCode.png').st_size > 380/1.5
    assert os.stat('QRCode.png').st_size < 380*1.5

    os.remove('QRCode.png')
