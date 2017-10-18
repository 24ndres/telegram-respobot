import requests

class BotHandler:

    def __init__(self, token):
        self.token = token
        self.api_url = "https://api.telegram.org/bot{}/".format(token)

    def get_updates(self, offset=None, timeout=10):
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

    def get_last_update(self, offset):
        get_result = self.get_updates(offset)
        
        if len(get_result) > 0:
            last_update = get_result[-1]
        else:
            #last_update = get_result[len(get_result)]
            last_update = None

        return last_update

greet_bot = BotHandler('466425736:AAHFy55FZHxJ4pbPYEpOEF9gc5DdaLCqmCU')

def main():
    new_offset = None

    while True:

        last_update = greet_bot.get_last_update(offset=new_offset)

        if last_update:
                
            last_update_id = last_update['update_id']
            last_chat_text = last_update['message']['text']
            last_chat_id = last_update['message']['chat']['id']
            last_chat_name = last_update['message']['chat']['first_name']

            if last_chat_text.lower() == '/euca':
                msg = 'La siguiente eucaristía es el sábado a las 21:00 en la Iglesia.'
            elif last_chat_text.lower() == '/palabra':
                msg = 'La siguiente celebración de la palabra es el martes en la sala Virgen de Montserrat a las 21:00.'
            elif last_chat_text.lower() == '/convi':
                msg = 'La siguiente convivencia será la de inicio en Can Fisa del 24.11 por la mañana al 26.11 por la tarde.'
            elif last_chat_text.lower() == '/avisos':
                msg = 'El grupo que prepara el siguiente tema debería haber empezado ya.'
            elif last_chat_text.lower() == '/grupos':
                msg = 'Grupo 1: Isabel Ochoteco, Elena Borrell, Pablo Martín, Luís, Diego Pérez. \nGrupo 2: Maria Sellas, Sofia Z, Dimas, Alejandro M, Maria Gonzalez. \nGrupo 3: Manuel Infiesta, Raquel S, Rocio, Joaquim, Alegria.\nGrupo 4: Elías M, Tomás, Andrés M, Sara, Pati A.\nGrupo 5: Alvaro C, Isabel Torres, Andrés Z, Javier, Blanca A.\nGrupo 6: Ana Manén, Paloma, David Aznar, Jose, Maria Ferreres, Vicky.\nGrupo 7: Maria Villaro, Moisés, Ramón Mª, Emma, Marta, Ana Navarro, David Prat.\nGrupo 8: Alvaro Roca, Míriam, Borja, Blanca Moina, Mateo, Clara Campillo.\nGrupo 9: Marcos, Teresa, Guillem Prat, Cristina Laucirica, Lucia Prat.'
            elif last_chat_text.lower() == '/temas':
                msg = 'Camino por el desierto: Mateo Manén, Elías Marín, Blanca Adell, Sofía Zaragoza, Tomás Pérez.\nConquista de la tierra prometida: Maria Ferreres, Joaquin Sellas, Patricia Adell, Lucia Prat, Pablo Martín.\nDavid y el reino: Paloma García, Isabel Torres, Borja Laucirica, Blanca Moina, Marta Benavides.\nExilio: Javier Infiesta, Dimas Valdés, Luís Ochoteco, María González, Cristina Laucirica.\nProfetas: Ana Manén, Manuel Infiesta, Emma Valdés, Clara Campillo, Alvaro Cendoya.\nLos orígenes (la creación, el mal y el pecado): Vicky Hunter, Maria Villaró, Alegria Barba, David Aznar, Jose Berman.\nEl Mesías: Moisés Corbacho, Raquel Serrat, David Prat, Lucia Prat, Maria Sellas.'
            elif last_chat_text.lower() == '/lista':
                msg = 'Disculpa, está opción aun no está disponible.'
            elif last_chat_text.lower() == '/sobreti':
                msg = 'Hola '+last_chat_name+', soy un Bot de telegram. Solo puedo responer a comandos programados. Mi desarrollador es: @andres_marin, puedes ver más sobre el en https://www.linkedin.com/in/andresmarinabad/'
            else:
                msg = 'Disculpa, no me has dado la instrucción correcta.'

            greet_bot.send_message(last_chat_id, msg)

            new_offset = last_update_id + 1

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        exit()