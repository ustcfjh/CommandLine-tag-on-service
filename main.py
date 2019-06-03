from __future__ import unicode_literals, print_function
from prompt_toolkit import prompt,PromptSession
from prompt_toolkit.lexers import PygmentsLexer
from pygments.lexers.sql import SqlLexer
from prompt_toolkit.styles import Style
from prompt_toolkit.completion import WordCompleter
from prompt_toolkit import print_formatted_text, HTML
from ImportTemplates import Templates
import os,sys
sys.path.append("..")

test=Templates('CommandTemplate.docx')
my_completer = WordCompleter(set(test.completer), ignore_case=True)

style = Style.from_dict({
    'completion-menu.completion': 'bg:#008888 #ffffff',
    'completion-menu.completion.current': 'bg:#00aaaa #000000',
    'scrollbar.background': 'bg:#88aaaa',
    'scrollbar.button': 'bg:#222222',
})


def main():
    session=PromptSession(completer=my_completer, complete_while_typing=False)
    view="[AC6508]"
    while True:
        try:
            text=session.prompt(view)
        except KeyboardInterrupt:
            continue
        except EOFError:
            break
        else:
            test.analyze(text)
    print('GoodBye!')

if __name__ == '__main__':
    main()
