import requests

class BotHandler():

	def __init__(self, token):
		self.token = token
		self.api_url = "https://api.telegram.org/bot{}/".format(token)

	def get_updates(self, offset=None, timeout=50):
        method = 'getUpdates'
        params = {'timeout': timeout, 'offset': offset}
        resp = requests.get(self.api_url + method, params)
        result_json = resp.json()['result']
        return result_json

    def send_message(self, chat_id, text):
        params = {'chat_id': chat_id, 'text': text}
        method = 'sendMessage'
        resp = requests.post(self.api_url + method, params)
        return resp

    def get_last_update(self):
        get_result = self.get_updates()

		if len(get_result) > 0:
            last_update = get_result[-1]
        else:
            last_update = get_result[len(get_result)]

		return last_update

# ------ TOKEN ------
token = '466425736:AAHFy55FZHxJ4pbPYEpOEF9gc5DdaLCqmCU'
# -------------------

# ------ RESPUESTAS ------
euca = 'en la iglesia a las 21:00'
palabra = 'en la sala Virgen de Montserrat a las 21:00 el martes'
convi = 'en Can Fisa del 24 al 26 de Noviembre'
avisos = 'El siguiente grupo de tema debería estar preparando!'
grupos = 'Lista de grupos'
temas = 'Lista de temas'
# ------------------------

# ------ PASSWORD ------
passwrd = '1348'
# ----------------------

# ------ COMANDOS ------
comandos = {'/euca': euca, '/palabra':palabra, '/convi':convi, '/avisos':avisos, '/grupos':grupos, '/temas':temas, '/lista':lista, '/master':master}
# ----------------------

# ------ BOT ------
respo_bot = BotHandler(token)
# -----------------

def euca(chat_id, chat_name):
	msg = 'Hola '+chat_name+', la eucaristia sera '+euca
	respo_bot.send_message(chat_id, msg)

def palabra(chat_id, chat_name):
	msg = 'Hola '+chat_name+', la palabra será '+palabra
	respo_bot.send_message(chat_id, msg)

def convi(chat_id, chat_name):
	msg = 'Hola '+chat_name+', la siguiente convivencia será '+convi
	respo_bot.send_message(chat_id, msg)

def avisos(chat_id, chat_name):
	msg = 'Hola '+chat_name+', estos son los avisos que ha dejado el responsable:\n'+avisos
	respo_bot.send_message(chat_id, msg)

def main():
	while True:
		respo_bot.get_updates()

	last_update = respo_bot.get_last_update()
	last_chat_text = last_update['message']['text']
	last_chat_id = last_update['message']['chat']['id']
	last_chat_name = last_update['message']['chat']['first_name']

	if last_chat_text in comandos:
		comandos[last_chat_text](last_chat_id, last_chat_name)


if __name__ == '__main__':  
    try:
        main()
    except KeyboardInterrupt:
        exit()