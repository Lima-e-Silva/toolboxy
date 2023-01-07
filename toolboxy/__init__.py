try:
    from error_identification import *
    from file_manipulation import *
    from free_APIs import *
    from git_tools import *
    from optimization import *
    from web_scrapping import *
    from windows_tools import *

    from misc import *

except ModuleNotFoundError:
    from .error_identification import *
    from .file_manipulation import *
    from .free_APIs import *
    from .git_tools import *
    from .optimization import *
    from .web_scrapping import *
    from .windows_tools import *

    from .misc import *

if __name__ == '__main__':
    requirements()