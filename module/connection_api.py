from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
from vk_api.longpoll import VkLongPoll, VkEventType
from config import config as cfg
import vk_api
def connect_by_API(access_token: str, is_group: bool, group_id: int = None): # Функция для подключения к API
    response, error = None, None; LongPoll = None
    try:
        if is_group:
            LongPoll = VkBotLongPoll(vk_api.VkApi(token=access_token), group_id=group_id)
        else:
            LongPoll = VkLongPoll(vk_api.VkApi(token=access_token))
    except Exception as ErrorMessage:
        response = False; error = ErrorMessage
    else:
        response = True
    finally:
        return {'success': response, 'error_msg': error, 'LongPoll': LongPoll}
    
def main(): # Фукнкиця для проверки подлючения API
    data = [['Prescott', cfg['token'], cfg['id_group'], True]]
    for validate in data:
        request = connect_by_API(validate[1], validate[3], validate[2] if validate[3] else None)
        print('Подлючение к {} прошло {}'.format(validate[0], 'успешно!' if request['success'] else 'не успепшно!!!\n{}'.format(request['error_msg'])))

session = vk_api.VkApi(token=cfg['token'], api_version=5.212)

vk_bot = session.get_api()

if __name__ == '__main__':
    main()
