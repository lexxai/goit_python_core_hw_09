


def parse_input(command_line: str) -> tuple[str, list]:
    for command in COMMANDS:
        if command_line.lower().startswith(command):
            args = command_line.lstrip(command).strip().split(" ",2)
            return command, args
    return command_line.lower(),[]
    # pars = command_line.split()
    # if len(pars) > 1:
    #     return pars[0].lower(), pars[1:]
    # else:
    #     return command_line.lower(),[]

def input_error(func):
    def inner(*args):
        #print(" Before")
        try:
            res = func(*args)
        except (KeyError, ValueError, IndexError)   as e:
            print("**** Exception fix",e)
        except Exception as e:
            print("**** Exception other",e)
        else:
            #print(" After")
            return res
    return inner

@input_error
def handler_add(user=None, phone=None) -> str:
    #print("handler_add")

    if user is None:
        return "the user name is not entered"

    if phone is None:
        return "user phone number is not entered"
    
    if not phone.isdecimal():
        return "the user's phone number is entered incorrectly"

    if user not in user_data:
        user_data[user] = phone
        return f"Phone of user ({user}) was added"
    else:
        return f"User ({user}) already present, maybe want to change ?"

@input_error
def handler_change(user=None, phone=None, *args) -> str:
    #print("handler_change")

    if user is None:
        return "the user name is not entered"

    if phone is None:
        return "user phone number is not entered"
    
    if not phone.isdecimal():
        return "the user's phone number is entered incorrectly"

    if user in user_data:
        user_data[user] = phone
        return f"Phone of user ({user}) was changed"
    else:
        return f"User({user}) not found, maybe want to add it at first ?"

@input_error
def handler_phone(user=None, *args) -> str:

    if user is None:
        raise Exception('input', "user missed")

    if user in user_data:
        return user_data.get(user)
    else:
        return f"User({user}) not found, maybe want to add it at first ?"


@input_error
def handler_show_all(*args) -> str:
    if len(user_data.keys()):
        result = []
        for user, phone in user_data.items():
            result.append(f"user: {user}, phone: {phone}")
        return "\n".join(result)
    else:
        return "No users found, maybe you want to add them first?"

# def handler_hello(*args) -> str:
#     return "How can I help you?"

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
    "hello": lambda *args: "How can I help you?",
    "add": handler_add,
    "change": handler_change,
    "phone": handler_phone ,
    "show all": handler_show_all,
    "help": handler_help
}
COMMANDS_HELP = {
    "hello": "Just hello",
    "add": "add user and phone",
    "change": "change user's phone",
    "phone": "show user's phone" ,
    "show all": "show all user's phone",
    "help": "List of commands  and their description",
    "exit": "exit of bot",
    "close": "exit of bot" ,
    "good bye": "exit of bot"
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