from openai import OpenAI



model = "/data1/glm-4-9b-chat"
client = OpenAI(api_key="aaa",base_url="http://221.229.101.198:8000/v1")
completions = client.chat.completions.create(
    model=model,

    messages=[{"role": "user", "content": "1 + 1 = ?"}],

    stream=False,
)

for choice in completions.choices:
    print(choice.message.content)
