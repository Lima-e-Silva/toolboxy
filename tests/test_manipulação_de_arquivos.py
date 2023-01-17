import toolboxy
from random import randrange
import os

cfg_dict = {
    'Sec1': {
        'opt1': str(randrange(1, 1000)),
        'opt2': str(randrange(1, 1000)),
        'opt3': 'string test'
    },
    'Sec2': {
        'opt1': str(randrange(1, 1000)),
        'opt2': str(randrange(1, 1000)),
        'opt3': 'string test'
    }
}

cfg_dict_compare = {'Sec2': {'opt1': '45', 'opt2': '2'}}


def test_create_cfg():
    toolboxy.create_cfg('tests/cfg_test.cfg', cfg_dict)
    assert 'cfg_test.cfg' in os.listdir('tests/')

    with open('tests/cfg_test.cfg', 'r') as file:
        raw_text = file.read()
        for key in cfg_dict.keys():
            assert key in raw_text


def test_read_cfg():
    cfg_from_file = toolboxy.read_cfg('tests/cfg_test.cfg')
    assert cfg_dict == cfg_from_file


def test_backup():
    toolboxy.backup('tests/cfg_test.cfg',
                    output_path='tests/',
                    backup_name='backup_test.cfg')
    assert 'backup_test.cfg' in os.listdir('tests/')

    backup_dict = toolboxy.read_cfg('tests/backup_test.cfg')
    assert cfg_dict == backup_dict


def test_check_hash():
    assert toolboxy.check_hash('tests/cfg_test.cfg', 'tests/cfg_test.cfg')
    assert toolboxy.check_hash('tests/cfg_test.cfg', 'tests/backup_test.cfg')

    toolboxy.create_cfg('tests/compare.cfg', cfg_dict_compare)
    assert '94d031c851fc47c9c41dc16c11956dc3672287c50859276624b691a43fb62a91' == toolboxy.check_hash(
        'tests/compare.cfg', sha=256)
    assert '92d031c851fc47c9c41dc16c11956dc3672287c50859276624b691a43fb62a91' != toolboxy.check_hash(
        'tests/compare.cfg')
    assert toolboxy.check_hash('tests/cfg_test.cfg', 'tests/cfg_test.cfg',
                               'tests/compare.cfg') == False

    assert toolboxy.check_hash(
        'LICENSE', sha=1) == "ee53e9103dcb40c94ff509d435ef701eb52b5756"
    assert toolboxy.check_hash(
        'LICENSE',
        sha=224) == "a442e961618c9fa7c6786bede7764343da62650f630b02e6b519c7ee"
    assert toolboxy.check_hash(
        'LICENSE', sha=256
    ) == "bfb48cc8af096321bdf6c7863c467763043f7a0d1ae5ef6252fc1feb065eb766"
    assert toolboxy.check_hash(
        'LICENSE', sha=384
    ) == "dc387a896b2be723ad93562f482071bbd7b0b2f5aa50d4dfcb989fcd77eac1e211283de8029664939f7610ad3e153a9e"

    os.remove('tests/cfg_test.cfg')
    os.remove('tests/backup_test.cfg')
    os.remove('tests/compare.cfg')