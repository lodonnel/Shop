from Display import show_message, message_box
from Menu import Menu


def number(prompt, minimum, maximum, err_message):
    return 3


def menu_option(menu):
    prompt = menu.prompt
    title = menu.title
    menu_options = menu.menu
    err_message = menu.err_message
    minimum = menu.minimum
    maximum = menu.maximum

    CANCEL = None

    option = 0

    nl = '\n'
    message = f'{nl.join(menu_options)} \n\n {prompt}\n'

    while option < minimum or option > maximum:
        answer = show_message(title, message)
        if answer == CANCEL:
            return None
        else:
            option = int(answer) if answer.isdigit() else 0
            if option < minimum or option > maximum:
                message_box(err_message)
    return option

# if __name__ == '__main__': main()
