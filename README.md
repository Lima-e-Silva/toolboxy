<div align="center">

 # DevTools
 
![Status](https://img.shields.io/badge/status-ativo-yellowgreen?style=for-the-badge)
![Version](https://img.shields.io/badge/versão-1.0-blue?style=for-the-badge)
[![PythonVersion](https://img.shields.io/badge/python-3.10-blue?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/downloads/)

 Repositório criado com o intuito de armazenar funções úteis e constantemente reutilizadas, a fim de economizar tempo.
 
 ![cover](https://github.com/Lima-e-Silva/DevTools/blob/main/Misc/cover.png)
 
 </div>


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


## Instalação

Para instalar, basta abrir o terminal e inserir o seguinte comando:
 ```cmd
 pip --upgrade https://github.com/Lima-e-Silva/DevTools.git
 ```
 
 <div align='right'>
 
 <sup>[Voltar ao sumário](#sumário)</sup>

 </div>
 
## Uso

### Web Scrapping
<details>
 <summary>Converter header em dicionário Python</summary>
 
 ```python
 import DevTools
 
 # Os parâmetros do header devem estar salvos num arquivo de texto.
 headers_dict = DevTools.chrome2dict(headers_path='folder\file.txt')
 ```
 </details>
 
 <details>
 <summary>Salvar código fonte em arquivo de texto</summary>
 
 ```python
 import requests
 import DevTools
 
 DevTools.html2txt(url="www.google.com.br", output_path='saída.txt')
 ```
 </details>
 
 <details>
 <summary>Verificar se um determinado endereço IP e porta podem ser usados como proxy</summary>
 
 ```python
 import DevTools
 
 # Endereços de IP e respectivas portas podem ser encontrados aqui: "https://free-proxy-list.net"
 ip = '80.252.5.34'
 port = '7001'
 
 if DevTools.verify_proxy(ip=ip, port=port):
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
 import DevTools
 
 # Função que está apresentando erros
 def foo(a,b):
    return a/b
 
 DevTools.debug_function(foo, a=1, b=0, output='logfile')
 ```
 </details>
 
  <div align='right'>
 
  <sup>[Voltar ao sumário](#sumário)</sup>

  </div>
  
 ### Manipulação de Arquivos
 
 <details>
 <summary>Criar arquivo de configuração (cfg)</summary>
 
 ```python
 import DevTools
 
 config_dict = {
    'seção': {
        'A': '1',
        'B': '2'
    }
 }
 
 DevTools.create_cfg(file='config.cfg', cfg_dict=config_dict)

 ```
 </details>
 
 <details>
 <summary>Ler arquivo de configuração (cfg)</summary>
 
 ```python
 import DevTools
 
 config_dict = DevTools.read_cfg(file='config.cfg')

 ```
 </details>
  
 <details>
 <summary>Criar backup de arquivo</summary>
 
 ```python
 import DevTools

 DevTools.backup(file='arquivo_importante.txt', output_path='backups/cópias_de_segurança')

 ```
 </details>
 
  <div align='right'>
 
  <sup>[Voltar ao sumário](#sumário)</sup>

  </div>
  
 ### Ferramentas Git
 
 <details>
 <summary>Criar um ambiente virtual</summary>
 
 ```python
 import DevTools

DevTools.create_env()

 ```
 </details>
 
 <details>
 <summary>Gerar um arquivo de licença</summary>
 
 ```python
 import DevTools

DevTools.license(license_type='MIT', name='Luiz Paulo Lima e Silva')

 ```
 </details>
 
 <details>
 <summary>Gerar um arquivo .gitignore com base num modelo padrão</summary>
 
 ```python
 import DevTools

DevTools.git_ignore(folders=['pasta-pessoal'], extensions=['xlsx', 'pdf'])
 ```
 </details>
 
 <details>
 <summary>Gerar um arquivo requirements.txt</summary>
 
 ```python
 import DevTools

DevTools.requirements()
 ```
 </details>
 
  <div align='right'>
 
  <sup>[Voltar ao sumário](#sumário)</sup>

  </div>
  
 ### Ferramentas Windows
 
 <details>
 <summary>Criar notificação do Windows</summary>
 
 ```python
 import DevTools

DevTools.notify(
    id='DevTools',
    title='Demonstração',
    message='Essa notificação trata-se de mera demonstração',
    buttons={'Abrir link': 'https://github.com/Lima-e-Silva/DevTools/'},
    sound=True,
    audio_loop=False)

 ```
 </details>
 
  <div align='right'>
 
  <sup>[Voltar ao sumário](#sumário)</sup>

  </div>
  
 ### Otimização
 
 <details>
 <summary>Gerar perfil de desempenho de função</summary>
 
 ```python
 import DevTools

def foo(x, y=3):
    for n in range(x):
        print(n**y)

DevTools.prof('output', foo, 100, y=2)

 ```
 </details>
 
  <div align='right'>
 
  <sup>[Voltar ao sumário](#sumário)</sup>

  </div>
  
 ### Diversos
 
 <details>
 <summary>Gerar QR Code de um link</summary>
 
 ```python
 import DevTools

DevTools.QRcode(url='https://github.com/Lima-e-Silva/DevTools/',
                size=150,
                output='Meu QR Code')

 ```
 </details>
 
 <div align='right'>
 
  <sup>[Voltar ao sumário](#sumário)</sup>

  </div>