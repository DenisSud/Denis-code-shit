import openai
import pyautogui
import pyperclip
import time

time.sleep(5)
openai.api_key = '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'
# Get the active window handle
active_window = pyautogui.getActiveWindow()
cursor_position = pyautogui.position()
pyautogui.hotkey("ctrl", "c")
prompt = pyperclip.paste()


def print_at_cursor(responce):
    pyautogui.write(responce, interval=0.01)


def generate_text(prompt):
    response = openai.ChatCompletion.create(
        model='gpt-3.5-turbo',
        messages=[{"role": "user", "content": str(prompt)}],
        max_tokens=50,  # Set the maximum length of the generated text
        temperature=0.6,  # Controls the randomness of the output
    )

    return response


# context = []
generated_text = generate_text(prompt)
# context.append(str(prompt + ": " + generated_text))
print_at_cursor(generated_text)
# hi
