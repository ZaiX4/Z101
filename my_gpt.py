import requests


def get_gpt_text(user_input):
    url = "https://openai.api2d.net/v1/chat/completions"

    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer fk213655-sOziJzANYlH66oItFv9PP96c5TDHt6dd'
    }
    data = {
        "model": "gpt-3.5-turbo",
        "messages": [{"role": "user", "content": user_input}]
    }

    response = requests.post(url, headers=headers, json=data)

    return response.json()['choices'][0]['message']['content']
