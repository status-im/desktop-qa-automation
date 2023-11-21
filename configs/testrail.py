import os
from datetime import datetime

CI_BUILD_URL = os.getenv('BUILD_URL', '')

RUN_NAME = os.getenv('TESTRAIL_RUN_NAME', '')
PROJECT_ID = os.getenv('TESTRAIL_PROJECT_ID', '')
URL = os.getenv('TESTRAIL_URL', '')
USR = os.getenv('TESTRAIL_USR', '')
PSW = os.getenv('TESTRAIL_PSW', '')

# Because of an issue with generating a timestamp on the CI side and adding it as a parameter on the test job:
if RUN_NAME.strip() == 'Nightly regression':
    RUN_NAME += f' {datetime.now():%Y.%m.%d}'
