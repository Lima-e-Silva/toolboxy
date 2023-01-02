import DevTools
import os


def test_uuid():
    letters = 'abcdefghijklmnopqrstuvwxyz'
    numbers = '0123456789'

    uid_1 = DevTools.unique_id(length=4,
                               letters=True,
                               numbers=True,
                               upper_case=True,
                               lower_case=True,
                               blocks=1,
                               separator='-')

    uid_2 = DevTools.unique_id(length=4,
                               letters=True,
                               numbers=True,
                               upper_case=True,
                               lower_case=True,
                               blocks=1,
                               separator='-')

    uid_3 = DevTools.unique_id(length=4,
                               letters=True,
                               numbers=True,
                               upper_case=True,
                               lower_case=True,
                               blocks=1,
                               separator='-')

    block_uid_1 = DevTools.unique_id(length=4,
                                     letters=False,
                                     numbers=True,
                                     upper_case=True,
                                     lower_case=True,
                                     blocks=2,
                                     separator='-')

    block_uid_2 = DevTools.unique_id(length=4,
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
    verification_hash = 'd7953fa0f18a9ced5b8c15a76640b9d62910c4c8b4acc670bc07f888739697c4'
    DevTools.QRcode(url=url)

    assert DevTools.check_hash('QRCode.png') == verification_hash

    os.remove('QRCode.png')
