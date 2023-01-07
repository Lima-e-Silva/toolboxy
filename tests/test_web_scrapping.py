import os

import requests as re

import toolboxy

headers_str = """accept: image/avif,image/webp,image/apng,image/svg+xml,image/*,*/*;q=0.8
accept-encoding: gzip, deflate, br
accept-language: pt-BR,pt;q=0.9,en-US;q=0.8,en;q=0.7
sec-ch-ua: "Chromium";v="108", "Not?A_Brand";v="8"
sec-ch-ua-platform: "Windows"
sec-fetch-dest: image
sec-fetch-mode: no-cors
sec-fetch-site: cross-site
user-agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36"""


def test_chrome2dict():
    with open('tests/headers', 'w') as f:
        f.write(headers_str)

    headers_from_str = toolboxy.chrome2dict(headers_str=headers_str)
    headers_from_file = toolboxy.chrome2dict(headers_path='tests/headers')

    assert headers_from_str == headers_from_file
    assert headers_from_str['sec-fetch-dest'] == 'image'
    assert headers_from_str['sec-fetch-mode'] == 'no-cors'
    assert headers_from_str['sec-fetch-site'] == 'cross-site'
    assert headers_from_str[
        'user-agent'] == 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36'

    os.remove('tests/headers')


def test_html2txt():
    response = re.get('https://api.my-ip.io/ip')
    toolboxy.html2txt(response=response, output_path='tests/re.txt')
    with open('tests/re.txt', 'r') as f:
        response_file = f.read()
        assert response.text in response_file
    os.remove('tests/re.txt')

#note: Desabilitado até encontrar proxy estável
def test_verify_proxy():
    #assert DevTools.verify_proxy(ip='178.33.198.181', port=3128, verbose=False)
    pass
