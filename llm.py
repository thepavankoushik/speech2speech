import openai

openai.api_base = "http://localhost:1234/v1"  # Point to the local server
openai.api_key = ""

def chat(user_input):
    system_prompt = "You are Chitti, A Digital Being, Speed 1 terra herz, Memory 1 Zeta Byte, you have been created by Mr.Pavan Koushik also known PK Sir, you respond to users with single line output without over information, you also respond in a slightly formal manner"
    user_message = {"role": "user", "content": user_input}
    messages = [
        {"role": "system", "content": system_prompt},
        user_message,
    ]
    completion = openai.ChatCompletion.create(
        model="local-model",  # This field is currently unused
        messages=messages
    )

    output = completion.choices[0].message["content"]
    return output

if __name__ == "__main__":
    print(chat("Hello"))