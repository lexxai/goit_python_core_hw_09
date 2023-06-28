

def parse_input(command_line: str) -> tuple[str, list]:
    for command in COMMANDS:
        if command_line.lower().startswith(command):
            args = command_line.lstrip(command).strip().split(" ",1)
            args = (s.strip() for s in args)
            return command, args
    return command_line.lower(),()


def input_error(func):
    def wrapper(*args):
        try:
            return func(*args)
        except (KeyError, ValueError, IndexError):
            return "Sorry, there are not enough parameters or their value may be incorrect. "\
                   "Please use the help for more information."
        except Exception as e:
            return "**** Exception other" + e
    return wrapper    


@input_error
def handler_add(*args) -> str:
    user = args[0]
    phone = args[1]
    user_data[user] = phone
    return "Done"


@input_error
def handler_change(*args) -> str:
    user = args[0]
    user_data[user]
    phone = args[1]
    user_data[user] = phone
    return "Done"


@input_error
def handler_phone(*args) -> str:
    user = args[0]
    return user_data[user]


def handler_show_all(*args) -> str:
    if len(user_data.keys()):
        result = []
        for user, phone in user_data.items():
            result.append(f"user: {user}, phone: {phone}")
        return "\n".join(result)
    else:
        return "No users found, maybe you want to add them first?"


def handler_hello(*args) -> str:
    return "How can I help you?"


def handler_help(*args) -> str:
    command = " ".join(args)
    if not command:
        commands = [i for i in COMMANDS.keys()]
        commands.extend(COMMAND_EXIT)
        return "List of commands: " + ", ".join(commands)
    else:
        if command in COMMANDS_HELP:
            return COMMANDS_HELP[command]
        else:
            return f"Help of this command '{command}' not ready yet"


COMMAND_EXIT=("good bye", "close", "exit")

COMMANDS = {
    "hello": handler_hello,
    "add": handler_add,
    "change": handler_change,
    "phone": handler_phone ,
    "show all": handler_show_all,
    "help": handler_help
}

COMMANDS_HELP = {
    "hello": "Just hello",
    "add": "Add user and phone. Required username and phone.",
    "change": "Change user's phone. Required username and phone.",
    "phone": "Show user's phone. Required username." ,
    "show all": "Show all user phone numbers.",
    "help": "List of commands  and their description.",
    "exit": "Exit of bot.",
    "close": "Exit of bot." ,
    "good bye": "Exit of bot."
}

user_data = {}

def main():
    print("Bot init")
    while True:
        try:
            user_input = input("Enter your command:")
        except KeyboardInterrupt:
            break
        if user_input.lower() in COMMAND_EXIT:
            break
        else:
            command, args = parse_input(user_input)
            try:
                result=COMMANDS[command](*args)
            except KeyError:
                 print("Your command is not recognized, try to enter other command. "
                       "To get a list of all commands, you can use the 'help' command")
            else:
                if result:
                    print(result)
    print("\nGood bye")

if __name__ == "__main__":
    main()