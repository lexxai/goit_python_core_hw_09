user_data = {}


def parse_input(command_line: str) -> tuple[str, list]:
    pars = command_line.split()
    if len(pars) > 1:
        return pars[0].lower(), pars[1:]
    else:
        return command_line.lower(),[]

def input_error(func):
    def inner(*args):
        print(" Before")
        try:
            res = func(*args)
        except Exception as e:
            print("**** Exception ",e)
        else:
            print(" After")
            return res
    return inner

@input_error
def handler_add(user=None, phone=None):
    #print("handler_add")

    if user is None:
        raise Exception('input', "user missed")

    if phone is None:
        raise Exception('input', "phone missed")

    if user not in user_data:
        user_data[user] = int(phone)
        return f"Phone of user ({user}) was added"
    else:
        return f"User ({user}) already present, maybe want to change ?"

@input_error
def handler_change(user=None, phone=None):
    #print("handler_change")

    if user is None:
        raise Exception('input', "user missed")

    if phone is None:
        raise Exception('input', "phone missed")

    if user in user_data:
        user_data[user] = int(phone)
        return f"Phone of user ({user}) was changed"
    else:
        return f"User({user}) not found, maybe want to add it at first ?"

@input_error
def handler_phone(user=None):

    if user is None:
        raise Exception('input', "user missed")

    if user in user_data:
        return user_data.get(user)
    else:
        return f"User({user}) not found, maybe want to add it at first ?"


@input_error
def show_all():
    if len(user_data.keys()):
        result = []
        for user, phone in user_data.items():
            result.append(f"user: {user}, phone: {phone}")
        return "\n".join(result)
    else:
        return "No users found, maybe you want to add them first?"

def handler_hello():
    return "How can I help you?"


COMMANDS = {
    "hello": handler_hello,
    "add": handler_add,
    "change": handler_change,
    "phone": handler_phone ,
}

def main():
    COMMAND_EXIT=("good bye", "close", "exit")
    COMMAND_SHOW_ALL="show all"
    print("Bot init")
    while True:
        user_input = input("Enter your command:")
        command, args = parse_input(user_input)
        if command in COMMAND_EXIT:
            print("Good bye")
            break
        elif user_input.lower() == COMMAND_SHOW_ALL:
            print(show_all())
        else:
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