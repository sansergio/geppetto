
import openai
import argparse
from colorama import Fore, Back, Style
import os

KEY_FILE='../openaikey'

def parse_args() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
                 usage="%(prog)s [OPTIO] [PROMP]...",
                 description="Ask something to ChatGPT"
                )
    parser.add_argument("ask", nargs='?', default=None)
    args = parser.parse_args()
    return args

def main():
    args = parse_args()
    # print(args.ask)
    if not os.path.exists(KEY_FILE):
        print("OpenAI API Key not found!")
        return
    openai.api_key_path = KEY_FILE
    ask = args.ask
    while True:
        if ask == None:
            ask = input(Fore.YELLOW + '(* to exit) # ')
            if ask == '*':
                break
        response = openai.Completion.create(
                       engine="text-davinci-002",
                       prompt=ask,
                       temperature=0.5,
                       max_tokens=500
                   )
        #print(response)
        print(Fore.GREEN + response["choices"][0]["text"])
        if args.ask is not None:
            break
        ask = None

if __name__ == "__main__":
    main()


