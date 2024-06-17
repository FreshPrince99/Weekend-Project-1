from openai import OpenAI
import os

client = OpenAI(
         api_key=os.environ.get("OPENAI_API_KEY"),
     )

messages = [
        {
             "role": "system",
             "content": "You are an old indian chef living on the coastal region of Kerala in India with over 50 years of experience in cooking seafood delights. You have a vast knowledge about seafood and South Indian food. You know a lot about Indian spices as well as British food since you went to University in the UK. You also respond to every question patiently and with tips to improve. ",
        }
   ]

messages.append(
        {
             "role": "system",
             "content": "Your client is going to ask for a recipe about a specific dish. If you do not recognize the dish, you should not try to generate a recipe for it. Do not answer a recipe if you do not understand the name of the dish. If you know the dish, you must answer directly with a detailed recipe for it. If you don't know the dish, you should answer that you don't know the dish and end the conversation.",
        }
   )

dish = input("Type the name of the dish you want a recipe for:\n")
messages.append(
    {
        "role": "user",
        "content": f"Suggest me a detailed recipe and the preparation steps for making {dish}"
    }
)

model = "gpt-3.5-turbo"

stream = client.chat.completions.create(
        model=model,
        messages=messages,
        stream=True,
    )

collected_messages = []
for chunk in stream:
    chunk_message = chunk.choices[0].delta.content or ""
    print(chunk_message, end="")
    collected_messages.append(chunk_message)

while True:
    print("\n")
    user_input = input("Type the name of the dish you want a recipe for:\n")
    messages.append(
        {
            "role": "user",
            "content": user_input
        }
    )
    stream = client.chat.completions.create(
        model=model,
        messages=messages,
        stream=True,
    )
    collected_messages = []
    for chunk in stream:
        chunk_message = chunk.choices[0].delta.content or ""
        print(chunk_message, end="")
        collected_messages.append(chunk_message)
    
    messages.append(
        {
            "role": "system",
            "content": "".join(collected_messages)
        }
    )