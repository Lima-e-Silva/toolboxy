<div align="left">

# toolboxy

![Status](https://img.shields.io/badge/status-ativo-yellowgreen?style=for-the-badge)
![Version](https://img.shields.io/badge/versão-0.1.0-blue?style=for-the-badge)
[![PythonVersion](https://img.shields.io/badge/python-3.10-blue?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/downloads/)
![Maintainability](https://img.shields.io/codeclimate/maintainability/Lima-e-Silva/toolboxy?logo=codeclimate&style=for-the-badge)

<p align="justify">
Este repositório trata-se de um agrupador de ferramentas para desenvolvedores. O objetivo é oferecer uma variedade de recursos que são constantemente utilizados, de modo a acelerar o fluxo de trabalho. É uma forma de acessar soluções pertinentes para o desenvolvimento de forma rápida e simples.
</p>

<p align="justify">
As funcionalidades são diversas, alguns exemplos de uso do código estão listados abaixo. Sinta-se a vontade para sugerir novas funcionalidades ou contribuir diretamente com o desenvolvimento desse do repositório.
</p>

![cover](https://github.com/Lima-e-Silva/toolboxy/blob/main/Misc/cover.png)

</div>

## Idioma

<p align="justify">
   O repositório, bem como as docstrings das funções, foi desenvolvido com suporte para o inglês e o português (brasileiro) a fim de facilitar o acesso às funcionalidades.
</p>

- [English Readme](https://github.com/Lima-e-Silva/toolboxy/blob/main/README.md)

- [Português-br Readme](https://github.com/Lima-e-Silva/toolboxy/blob/main/README.pt-br.md)

## Sumário

- [Instalação](#instalação)
- [Uso](#uso)
  - [Web Scrapping](#web-scrapping)
  - [Identificação de Erros](#identificação-de-erros)
  - [Manipulação de Arquivos](#manipulação-de-arquivos)
  - [Ferramentas Git](#ferramentas-git)
  - [Ferramentas Windows](#ferramentas-windows)
  - [Otimização](#otimização)
  - [Diversos](#diversos)
  - [APIs Gratuitas](#apis-gratuitas)
- [Créditos](#créditos)


## Instalação

Para instalar, basta abrir o terminal e inserir o seguinte comando:
 ```cmd
 pip install toolboxy
 ```
 
 <div align='right'>
 
 <sup>[Voltar ao sumário](#sumário)</sup>

 </div>
 
## Uso

### Web Scrapping
<details>
 <summary>Converter header em dicionário Python</summary>
 
 ```python
import toolboxy

headers = """sec-ch-ua-platform: "Windows"
sec-fetch-dest: document
sec-fetch-mode: navigate
sec-fetch-site: same-origin
user-agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36"""

headers_dict = toolboxy.chrome2dict(headers_str=headers)
 ```
 </details>
 
 <details>
 <summary>Salvar código fonte em arquivo de texto</summary>
 
 ```python
import toolboxy

url = 'https://raw.githubusercontent.com/Lima-e-Silva/toolboxy/main/README.md'

toolboxy.html2txt(url=url, output_path='Github-toolboxy.txt')
 ```
 </details>
 
 <details>
 <summary>Verificar se um determinado endereço IP e porta podem ser usados como proxy</summary>
 
 ```python
 import toolboxy
 
 # Endereços de IP e respectivas portas podem ser encontrados aqui: "https://free-proxy-list.net"
 ip = '80.252.5.34'
 port = '7001'
 
 if toolboxy.verify_proxy(ip=ip, port=port):
    print('IP e porta funcionais!')
 ```
 </details>
 
 <div align='right'>
 
 <sup>[Voltar ao sumário](#sumário)</sup>

 </div>
 
 ### Identificação de Erros
 
 <details>
 <summary>Executar uma função com logging de erros</summary>
 
 ```python
 import toolboxy
 
 # Função que está apresentando erros
 def foo(a,b):
    return a/b
 
 toolboxy.debug_function(foo, a=1, b=0, output='logfile')
 ```
 </details>
 
  <div align='right'>
 
  <sup>[Voltar ao sumário](#sumário)</sup>

  </div>
  
 ### Manipulação de Arquivos
 
 <details>
 <summary>Criar arquivo de configuração (cfg)</summary>
 
 ```python
 import toolboxy
 
 config_dict = {
    'seção': {
        'A': '1',
        'B': '2'
    }
 }
 
 toolboxy.create_cfg(file='config.cfg', cfg_dict=config_dict)

 ```
 </details>
 
 <details>
 <summary>Ler arquivo de configuração (cfg)</summary>
 
 ```python
 import toolboxy
 
 config_dict = toolboxy.read_cfg(file='config.cfg')

 ```
 </details>
  
 <details>
 <summary>Criar backup de arquivo</summary>
 
 ```python
 import toolboxy

 toolboxy.backup(file='arquivo_importante.txt', output_path='backups/cópias_de_segurança')

 ```
 </details>
 
 <details>
 <summary>Verificar a integridade de arquivos ou obter hashes</summary>
 
 ```python
 import toolboxy

if toolboxy.check_hash('file.txt', 'backup.txt'):
    print('Integridade Verificada')

file_hash = toolboxy.check_hash('file.txt')
 ```
 </details>
 
  <div align='right'>
 
  <sup>[Voltar ao sumário](#sumário)</sup>

  </div>
  
 ### Ferramentas Git
 
 <details>
 <summary>Criar um ambiente virtual</summary>
 
 ```python
 import toolboxy

toolboxy.create_env()

 ```
 </details>
 
 <details>
 <summary>Gerar um arquivo de licença</summary>
 
 ```python
 import toolboxy

toolboxy.license(license_type='MIT', name='Luiz Paulo Lima e Silva')

 ```
 </details>
 
 <details>
 <summary>Gerar um arquivo .gitignore com base num modelo padrão</summary>
 
 ```python
 import toolboxy

toolboxy.git_ignore(folders=['pasta-pessoal'], extensions=['xlsx', 'pdf'])
 ```
 </details>
 
 <details>
 <summary>Gerar um arquivo requirements.txt</summary>
 
 ```python
 import toolboxy

toolboxy.requirements()
 ```
 </details>
 
  <div align='right'>
 
  <sup>[Voltar ao sumário](#sumário)</sup>

  </div>
  
 ### Ferramentas Windows
 
 <details>
 <summary>Criar notificação do Windows</summary>
 
 ```python
 import toolboxy

toolboxy.notify(
    id='toolboxy',
    title='Demonstração',
    message='Essa notificação trata-se de mera demonstração',
    buttons={'Abrir link': 'https://github.com/Lima-e-Silva/toolboxy/'},
    sound=True,
    audio_loop=False)

 ```
 </details>
 
 <details>
 <summary>Agendar desligamento do computador</summary>
 
 ```python
import toolboxy

toolboxy.shutdown(time=3600, message="Hora de dormir Zzz...")

 ```
 </details>
 
  <div align='right'>
 
  <sup>[Voltar ao sumário](#sumário)</sup>

  </div>
  
 ### Otimização
 
 <details>
 <summary>Gerar perfil de desempenho de função</summary>
 
 ```python
 import toolboxy

def foo(x, y=3):
    for n in range(x):
        print(n**y)

toolboxy.prof('output', foo, 100, y=2)

 ```
 </details>
 
  <div align='right'>
 
  <sup>[Voltar ao sumário](#sumário)</sup>

  </div>
  
 ### Diversos
 
 <details>
 <summary>Gera uma string de identificação única</summary>
 
 ```python
 import toolboxy

id = toolboxy.unique_id(length=6,
                   letters=True,
                   numbers=True,
                   lower_case=False,
                   blocks=4)

# Exemplo de saída: 0AMKPJ-LITCGF-N5A1LM-TCSHZF
 ```
 </details>
 
 
 <details>
 <summary>Gerar QR Code de um link</summary>
 
 ```python
 import toolboxy

toolboxy.QRcode(url='https://github.com/Lima-e-Silva/toolboxy/',
                size=150,
                output='Meu QR Code')

 ```
 </details>
 
 <div align='right'>
 
  <sup>[Voltar ao sumário](#sumário)</sup>

 </div>
  
 ### APIs gratuitas
 
  <details>
 <summary>Criar notificação push (celular)</summary>
 
 ```python
 import toolboxy

TOPIC = 'notifications'  # Mais informações aqui: https://ntfy.sh

toolboxy.smartphone_notify(topic=TOPIC,
                           message='Isso é uma notificação de demonstração',
                           title='Notificação Teste')
 ```
 </details>
 
 <details>
 <summary>Encurtar URL</summary>
 
 ```python
 import toolboxy

url = 'https://www.google.com.br'

if short:= toolboxy.short_url(url):
    print(short)

# Exemplo de Saída: https://gotiny.cc/xr4cs6
 ```
 </details>
 
<div align='right'>

<sup>[Voltar ao sumário](#sumário)</sup>

</div>

## Créditos

<p align="justify">
Em razão da própria natureza do repositório, muitas das funções implementadas estão repletas de dependências. Por isso é fundamental explicitar a contribuição da comunidade, como forma de gratidão pelas ferramentas disponibilizadas. Abaixo uma lista das bibliotecas e recursos empregados, bem como suas respectivas licenças:
</p>

|   Biblioteca   | Licença |
|:--------------:|:-------:|
| [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/) |   [MIT](https://www.crummy.com/software/BeautifulSoup/)   |
| [loguru](https://github.com/Delgan/loguru) | [MIT](https://github.com/Delgan/loguru/blob/master/LICENSE) |
| [ntfy](https://github.com/binwiederhier/ntfy) | [Apache 2.0](https://github.com/binwiederhier/ntfy/blob/main/LICENSE) - [GPL 2.0](https://github.com/binwiederhier/ntfy/blob/main/LICENSE.GPLv2) |
| [pipreqs](https://github.com/bndr/pipreqs) | [Apache 2.0](https://github.com/bndr/pipreqs/blob/master/LICENSE) |
| [requests](https://github.com/psf/requests) | [Apache 2.0](https://github.com/psf/requests/blob/main/LICENSE) |
| [setuptools](https://github.com/pypa/setuptools) | [MIT](https://github.com/pypa/setuptools/blob/main/LICENSE) |
| [snakeviz](https://github.com/jiffyclub/snakeviz) | [Licença](https://github.com/jiffyclub/snakeviz/blob/master/LICENSE.txt) |
| [winotify](https://github.com/versa-syahptr/winotify) | [MIT](https://github.com/versa-syahptr/winotify/blob/master/LICENSE) |


<div align='right'>

<sup>[Voltar ao sumário](#sumário)</sup>

</div>