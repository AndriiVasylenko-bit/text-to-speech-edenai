import json
import os
import time
from dotenv import load_dotenv
import requests


def text_to_speech(text="Привіт друг!"):
    load_dotenv()
    # print(os.getenv('API_KEY'))
    headers = {"Authorization": f"Bearer {os.getenv('API_KEY')}"}
    url = 'https://api.edenai.run/v2/audio/text_to_speech'

    payload = {
        'providers': 'openai',
        'language': 'uk',
        'option': 'MALE',
        'openai': 'uk_onyx',
        'text': f'{text}'
    }

    response = requests.post(url, json=payload, headers=headers)
    result = json.loads(response.text)
    unx_time = int(time.time())

    # with open(f'{unx_time}.json', 'w') as file:
    #     json.dump(result, file, indent=4, ensure_ascii=False)

    audio_url = result.get('openai').get('audio_resource_url')
    r = requests.get(audio_url)

    with open(f'{unx_time}.wav', 'wb') as file:
        file.write(r.content)

def main():
    text_to_speech(
        text='Міжнародне співробітництво у сфері безпеки є ключовим елементом в забезпеченні стабільності та захисту громадян')


if __name__ == '__main__':
    main()
