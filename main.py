from module.connection_api import main
from server.index import bot

from threading import Thread # pip install threading
import gspread
### pip install gspread

### Руководство по google sheets: https://dvsemenov.ru/google-tablicy-i-python-podrobnoe-rukovodstvo-s-primerami/
### VK_api: https://dev.vk.com/ru/method/

# Указываем путь к JSON
gc = gspread.service_account(filename='testtable-406222-01effc6715d5.json')


main()
Thread(target=bot).start()