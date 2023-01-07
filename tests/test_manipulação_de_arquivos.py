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
        'tests/compare.cfg')
    assert '92d031c851fc47c9c41dc16c11956dc3672287c50859276624b691a43fb62a91' != toolboxy.check_hash(
        'tests/compare.cfg')
    assert toolboxy.check_hash('tests/cfg_test.cfg', 'tests/cfg_test.cfg',
                               'tests/compare.cfg') == False

    os.remove('tests/cfg_test.cfg')
    os.remove('tests/backup_test.cfg')
    os.remove('tests/compare.cfg')