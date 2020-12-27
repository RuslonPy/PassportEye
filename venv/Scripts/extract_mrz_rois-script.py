#!D:\Django\passporteye\venv\Scripts\python.exe
# EASY-INSTALL-ENTRY-SCRIPT: 'PassportEye==2.1.0','console_scripts','extract_mrz_rois'
__requires__ = 'PassportEye==2.1.0'
import re
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw?|\.exe)?$', '', sys.argv[0])
    sys.exit(
        load_entry_point('PassportEye==2.1.0', 'console_scripts', 'extract_mrz_rois')()
    )
