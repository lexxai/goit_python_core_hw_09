


def parse_input(command_line: str) -> tuple[str, list]:
    for command in COMMANDS:
        if command_line.lower().startswith(command):
            args = command_line.lstrip(command).strip().split(" ",1)
            args = (s.strip() for s in args)
            return command, args
    return command_line.lower(),()


def input_error(func):
    def wrapper(*args):

        parameters = FUNCTIONS_ARGS.get(func.__name__,FUNCTIONS_ARGS["default"])   

        #print(" Before ",func.__name__,args,len(args),parameters)

        if not args[0] or (len(args) < parameters):
            return "Sorry, not enough parameters. Use help for more information."
        try:
            res = func(*args)
        except (KeyError, ValueError, IndexError):
            return "Sorry, the settings may be incorrect. Please use the help for more information."
        except Exception as e:
            return "**** Exception other" + e
        else:
            #print(" After")
            return res
    return wrapper    


@input_error
def handler_add(user=None, phone=None, *args) -> str:
    #print("handler_add")
    user_data[user] = phone
    return "Done"

    # if user is None:
    #     return "the user name is not entered"

    # if phone is None:
    #     return "user phone number is not entered"
    
    # if not phone.isdecimal():
    #     return "the user's phone number is entered incorrectly"

    # if user not in user_data:
    #     user_data[user] = phone
    #     return f"Phone of user ({user}) was added"
    # else:
    #     return f"User ({user}) already present, maybe want to change ?"

@input_error
def handler_change(user=None, phone=None, *args) -> str:
    #print("handler_change")
    user_data[user]
    user_data[user] = phone
    return "Done"

    # if user is None:
    #     return "the user name is not entered"

    # if phone is None:
    #     return "user phone number is not entered"
    
    # if not phone.isdecimal():
    #     return "the user's phone number is entered incorrectly"

    # if user in user_data:
    #     user_data[user] = phone
    #     return f"Phone of user ({user}) was changed"
    # else:
    #     return f"User({user}) not found, maybe want to add it at first ?"

@input_error
def handler_phone(user=None, *args) -> str:

    return user_data[user]

    # if user is None:
    #     return "the user name is not entered"

    # if user in user_data:
    #     return user_data.get(user)
    # else:
    #     return f"User({user}) not found, maybe want to add it at first ?"



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
FUNCTIONS_ARGS = {
    "default": 2,
    "handler_phone": 1
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

COMMANDSF = {
    handler_hello: "hello",
    handler_add: "add",
    handler_change: "change",
    handler_phone : "phone",
    handler_show_all: "show all",
    handler_help: "help"
}

user_data = {}

def main():
    print("Bot init")
    while True:
        user_input = input("Enter your command:")
        if user_input.lower() in COMMAND_EXIT:
            print("Good bye")
            break
        else:
            command, args = parse_input(user_input)
            #print(command, args)
            try:
                result=COMMANDS[command](*args)
            except KeyError:
                 print("Your command is not recognized, try to enter other command")
            else:
                if result:
                    print(result)

        #print("user_data",user_data)

if __name__ == "__main__":
    main()