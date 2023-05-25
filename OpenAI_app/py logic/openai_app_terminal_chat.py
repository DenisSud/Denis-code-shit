import openai

openai.api_key = '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'


def generate_text(messages):
    response = openai.ChatCompletion.create(
        model='gpt-3.5-turbo',
        messages=messages,
    )

    return response#[0]["message"]["content"]


messages = []
while True:
    # Prompt for the model to generate text
    prompt = input()
    if prompt == "":
        break
    messages.append({"role": "user", "content": prompt})
    # Generate text based on the prompt
    generated_text = generate_text(messages)
    messages.append({"role": "assistant", "content": generated_text})
    # Print the generated text
    print(generated_text)
