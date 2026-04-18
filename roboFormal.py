import ollama
import pyperclip
import pyautogui

resposta = ollama.chat(
    model='reescritor-formal',
    messages=[{'role':'user','content':pyperclip.paste()}],
)
pyperclip.copy(resposta.message.content)
pyautogui.hotkey('ctrl','v')
