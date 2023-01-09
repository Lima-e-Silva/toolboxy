<div align="left">

# toolboxy

![Status](https://img.shields.io/badge/status-active-brightgree)
![Maintainability](https://img.shields.io/codeclimate/maintainability/Lima-e-Silva/toolboxy?logo=codeclimate)
[![PythonVersion](https://img.shields.io/pypi/pyversions/toolboxy)](https://www.python.org/downloads/)
[![Version](https://img.shields.io/pypi/v/toolboxy)](https://pypi.org/project/toolboxy/)
[![Downloads](https://static.pepy.tech/badge/toolboxy)](https://pepy.tech/project/toolboxy)

<p align="justify">
This repository is a collection of tools for developers. The goal is to offer a variety of resources that are constantly used, in order to accelerate the workflow. It is a way to quickly and easily access relevant solutions for development.
</p>

<p align="justify">
The functionality is diverse, some examples of code use are listed below. Feel free to suggest new functionality or directly contribute to the development of this repository.
</p>

![cover](https://github.com/Lima-e-Silva/toolboxy/blob/main/misc/cover.png)

</div>

## Language

<p align="justify">
   The repository, as well as the docstrings of the functions, were developed with support for English and Brazilian Portuguese in order to facilitate access to functionality.
</p>

- [English Readme](https://github.com/Lima-e-Silva/toolboxy/blob/main/README.md)

- [Português-br Readme](https://github.com/Lima-e-Silva/toolboxy/blob/main/README.pt-br.md)

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
  - [Web Scrapping](#web-scrapping)
  - [Error Identification](#error-identification)
  - [File Manipulation](#file-manipulation)
  - [Git Tools](#git-tools)
  - [Windows Tools](#windows-tools)
  - [Optimization](#optimization)
  - [Miscellaneous](#miscellaneous)
  - [Free APIs](#free-apis)
- [Credits](#credits)


## Installation

To install, simply open the terminal and enter the following command:
```cmd
pip install toolboxy
```

<div align='right'>

<sup>[Back to table of contents](#table-of-contents)</sup>

</div>

## Usage

### Web Scrapping
<details>
 <summary>Convert header to Python dictionary</summary>
 
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
 <summary>Save source code in text file</summary>
 
 ```python
import toolboxy

url = 'https://raw.githubusercontent.com/Lima-e-Silva/toolboxy/main/README.md'

toolboxy.html2txt(url=url, output_path='Github-toolboxy.txt')
 ```
 </details>

<details>
 <summary>Check if a given IP address and port can be used as a proxy</summary>
 
 ```python
 import toolboxy
 
 # IP addresses and respective ports can be found here: "https://free-proxy-list.net"
 ip = '80.252.5.34'
 port = '7001'
 
 if toolboxy.verify_proxy(ip=ip, port=port):
    print('IP and port are functional!')
  ```
 </details>

<div align='right'>

<sup>[Back to table of contents](#table-of-contents)</sup>

</div>

### Error Identification
 
 <details>
 <summary>Run a function with error logging</summary>
 
 ```python
 import toolboxy
 
 # Function that is experiencing errors
 def foo(a,b):
    return a/b
 
 toolboxy.debug_function(foo, a=1, b=0, output='logfile')
```
</details>

<div align='right'>

<sup>[Back to table of contents](#table-of-contents)</sup>

</div>

### File Manipulation
 
 <details>
 <summary>Create configuration file (cfg)</summary>
 
 ```python
 import toolboxy
 
 config_dict = {
    'section': {
        'A': '1',
        'B': '2'
    }
 }
 
 toolboxy.create_cfg(file='config.cfg', cfg_dict=config_dict)
 ```
 </details>

<details>
 <summary>Read a configuration file (cfg)</summary>
 
 ```python
 import toolboxy
 
 config_dict = toolboxy.read_cfg(file='config.cfg')

 ```
 </details>

<details>
 <summary>Create file backup</summary>
 
 ```python
import toolboxy

toolboxy.backup(file='important_file.txt',
                output_path='backups/security_copies')
```
</details>

<details>
 <summary>Verify file integrity or get hashes</summary>
 
 ```python
 import toolboxy

if toolboxy.check_hash('file.txt', 'backup.txt'):
    print('Integrity Verified')

file_hash = toolboxy.check_hash('file.txt')
```
</details>

<div align='right'>

<sup>[Back to table of contents](#table-of-contents)</sup>

</div>


### Git Tools
 
 <details>
 <summary>Create a virtual environment</summary>
 
 ```python
 import toolboxy

toolboxy.create_env()
```
</details>

<details>
 <summary>Create a license file</summary>
 
 ```python
 import toolboxy

toolboxy.license(license_type='MIT', name='Luiz Paulo Lima e Silva')

 ```
 </details>

 <details>
 <summary>Generate a .gitignore file based on a standard template</summary>
 
 ```python
 import toolboxy

toolboxy.git_ignore(folders=['personal-folder'], extensions=['xlsx', 'pdf'])
```
 </details>

 <details>
 <summary>Create requirements.txt</summary>
 
 ```python
 import toolboxy

toolboxy.requirements()
 ```
 </details>

 <div align='right'>

<sup>[Back to table of contents](#table-of-contents)</sup>

</div>

### Windows Tools
 
 <details>
 <summary>Create Windows notification</summary>
 
 ```python
 import toolboxy

toolboxy.notify(
    id='toolboxy',
    title='Demonstration',
    message='This notification is merely a demonstration',
    buttons={'Open link': 'https://github.com/Lima-e-Silva/toolboxy/'},
    sound=True,
    audio_loop=False)
```
</details>

<details>
 <summary>Schedule computer shutdown</summary>
 
 ```python
import toolboxy

toolboxy.shutdown(time=3600, message="Time to sleep Zzz...")
```
</details>

<div align='right'>

<sup>[Back to table of contents](#table-of-contents)</sup>

</div>

### Optimization
 
 <details>
 <summary>Generate function performance profile</summary>
 
 ```python
 import toolboxy

def foo(x, y=3):
    for n in range(x):
        print(n**y)

toolboxy.prof('output', foo, 100, y=2)
```
</details>

<details>
 <summary>Calculate the elapsed time while running a function</summary>
 
 ```python
 import toolboxy

def foo(n):
    values = list()
    for i in range(n):
        for _ in range(i):
            values.append(i)
    print(values)

print(toolboxy.elapsed_clocktime(foo, 100))

```
</details>

<details>
 <summary>Display the elapsed CPU time while running a function</summary>
 
 ```python
 import toolboxy

def foo(n):
    values = list()
    for i in range(n):
        for _ in range(i):
            values.append(i)
    print(values)

toolboxy.elapsed_cputime(foo, 100)
```
</details>

<div align='right'>

<sup>[Back to table of contents](#table-of-contents)</sup>

</div>

### Miscellaneous
 
 <details>
 <summary>Generates a unique identification string</summary>
 
 ```python
import toolboxy

id = toolboxy.unique_id(length=6,
                        letters=True,
                        numbers=True,
                        lower_case=False,
                        blocks=4)

# Example output: 0AMKPJ-LITCGF-N5A1LM-TCSHZF
```
</details>

<details>
 <summary>Generate QR Code for a link</summary>
 
 ```python
 import toolboxy

toolboxy.QRcode(url='https://github.com/Lima-e-Silva/toolboxy/',
                size=150,
                output='My QR Code')

```
</details>

<div align='right'>

<sup>[Back to table of contents](#table-of-contents)</sup>

</div>

### Free APIs
 
  <details>
 <summary>Create push notification (mobile)</summary>
 
 ```python
 import toolboxy

TOPIC = 'notifications'  # More information here: https://ntfy.sh

toolboxy.smartphone_notify(topic=TOPIC,
                           message='This is a demonstration notification',
                           title='Test Notification')
```
</details>

<details>
 <summary>Shorten URL</summary>
 
 ```python
 import toolboxy

url = 'https://www.google.com.br'

if short:= toolboxy.short_url(url):
    print(short)

# Example Output: https://gotiny.cc/xr4cs6
```
</details>

<div align='right'>

<sup>[Back to table of contents](#table-of-contents)</sup>

</div>

## Credits

<p align="justify">
Due to the nature of the repository, many of the implemented functions are full of dependencies. Therefore, it is essential to explicitly acknowledge the contribution of the community as a way of thanking them for the tools provided. Below is a list of the libraries and resources used and their respective licenses:
</p>

|   Library   | License |
|:--------------:|:-------:|
| [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/) |   [MIT](https://www.crummy.com/software/BeautifulSoup/)   |
| [loguru](https://github.com/Delgan/loguru) | [MIT](https://github.com/Delgan/loguru/blob/master/LICENSE) |
| [ntfy](https://github.com/binwiederhier/ntfy) | [Apache 2.0](https://github.com/binwiederhier/ntfy/blob/main/LICENSE) - [GPL 2.0](https://github.com/binwiederhier/ntfy/blob/main/LICENSE.GPLv2) |
| [pipreqs](https://github.com/bndr/pipreqs) | [Apache 2.0](https://github.com/bndr/pipreqs/blob/master/LICENSE) |
| [requests](https://github.com/psf/requests) | [Apache 2.0](https://github.com/psf/requests/blob/main/LICENSE) |
| [setuptools](https://github.com/pypa/setuptools) | [MIT](https://github.com/pypa/setuptools/blob/main/LICENSE) |
| [snakeviz](https://github.com/jiffyclub/snakeviz) | [License](https://github.com/jiffyclub/snakeviz/blob/master/LICENSE.txt) |
| [winotify](https://github.com/versa-syahptr/winotify) | [MIT](https://github.com/versa-syahptr/winotify/blob/master/LICENSE) |

<div align='right'>

<sup>[Back to table of contents](#table-of-contents)</sup>

</div>