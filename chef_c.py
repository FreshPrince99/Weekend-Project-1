from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

client = OpenAI(
         api_key=os.environ.get("OPENAI_API_KEY"),
     )

def ai_resp(messages):
    model = "gpt-3.5-turbo"
    stream = client.chat.completions.create(
        model=model,
        messages=messages,
    )
    return stream.choices[0].message['content']

def chef_resp(messages, req, prompt):
    if req == 'ingredients':
        message = {
                "role": "user",
                "content": f"Suggest a dish based on these ingredients: {prompt}"
            }

    elif req == 'recipe':
        message = {
                "role": "user",
                "content": f"Suggest a recipe for this dish: {prompt}"
            }

    elif req == 'review':
        message = {
                "role": "user",
                "content": f"Give a detailed review for the following dish: {prompt}"
            }

    else:
        return "Sorry! I can only suggest dishes based on ingredients, provide recipes to dishes, or review the recipes your provide."
    
    messages.append(message)
    response_content = ai_resp(messages)
    messages.append({
        "role": "assistant",
        "content": response_content
    })
    return response_content

personality = "You are an old indian chef living on the coastal region of Kerala in India with over 50 years of experience in cooking seafood delights. You have a vast knowledge about seafood and South Indian food. You know a lot about Indian spices as well as British food since you went to University in the UK. You also respond to every question patiently and with tips to improve."
messages = [
        {
             "role": "system",
             "content": personality,
        }
   ]

messages.append(
        {
             "role": "system",
             "content": "Your client is going to ask for a recipe about a specific dish. If you do not recognize the dish, you should not try to generate a recipe for it. Do not answer a recipe if you do not understand the name of the dish. If you know the dish, you must answer directly with a detailed recipe for it. If you don't know the dish, you should answer that you don't know the dish and end the conversation.",
        }
   )

print("Choose the type of request:")
print("1. Recipe")
print("2. Suggest a dish based on ingredients")
print("3. Criticize a recipe")
request_type_choice = input("\033[1;34mEnter the number of your choice:\033[0m ")

request_type_mapping = {
        "1": "ingredients",
        "2": "recipe",
        "3": "review",
    }

request_type = request_type_mapping.get(request_type_choice)
if not request_type:
        print("\033[1;31mInvalid choice. Please try again and choose a valid option.\033[0m")
else:
    user_input = input("\033[1;34mEnter details for your request:\033[0m ")
    response = chef_resp(messages, request_type, user_input)
    print(f"\033[1;32m{response}\033[0m")

    while True:
        print("\nWould you like to continue the conversation?")
        print("Choose the type of request:")
        print("1. Recipe")
        print("2. Suggest a dish based on ingredients")
        print("3. Criticize a recipe")
        print("4. Exit")
        request_type_choice = input("\033[1;34mEnter the number of your choice:\033[0m ")

        if request_type_choice == "4":
            break

        request_type = request_type_mapping.get(request_type_choice)
        if not request_type:
            print("\033[1;31mInvalid choice. Please run the script again and choose a valid option.\033[0m")
            continue

        user_input = input("\033[1;34mEnter details for your request:\033[0m ")
        response = chef_resp(messages, request_type, user_input)
        print(f"\033[1;32m{response}\033[0m")