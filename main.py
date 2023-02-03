import openai
from config import *


def sen
openai.api_key = API_KEY
# задаем модель и промпт
model_engine = "text-davinci-003"
prompt = "how to insert json file into Postgresql using python"

# задаем макс кол-во слов
max_tokens = 128

# генерируем ответ
completion = openai.Completion.create(
    engine=model_engine,
    prompt=prompt,
    max_tokens=1024,
    temperature=0.5,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0
)

# выводим ответ
print(completion.choices[0].text)