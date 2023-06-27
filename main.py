user_data = {}


def parse_input(command_line: str) -> tuple[str, list]:
    pars = command_line.split()
    if len(pars) > 1:
        return pars[0].lower(), pars[1:]
    else:
        return command_line.lower(),[]

def input_error(func):
    def inner(user="", phone=""):
        print(" Before")
        print(func(user, phone))
        print(" After")
    return inner

@input_error
def handler_add(user, phone):
    #print("handler_add")
    if user not in user_data:
        user_data[user] = phone
        return f"Phone of user ({user}) was added"
    else:
        return f"User ({user}) already present, maybe want to change ?"

@input_error
def handler_change(user, phone):
    #print("handler_change")
    if user in user_data:
        user_data[user] = phone
        return f"Phone of user ({user}) was changed"
    else:
         return f"User({user}) not found, maybe want to add it at first ?"

@input_error
def handler_phone(user, _=""):
    if user in user_data:
        return user_data.get(user)
    else:
        return f"User({user}) not found, maybe want to add it at first ?"


def show_all(_1="",_2=""):
    if len(user_data.keys()):
        result = []
        for user, phone in user_data.items():
            result.append(f"user: {user}, phone: {phone}")
        return "\n".join(result)
    else:
        return "No users found, maybe you want to add them first?"



COMMANDS = {
    "add": handler_add,
    "change": handler_change,
    "phone": handler_phone ,
}

def main():
    COMMAND_EXIT=("good bye", "close", "exit")
    COMMAND_HELLO="hello"
    COMMAND_SHOW_ALL="show all"
    print("Bot init")
    while True:
        user_input = input("Enter your command:")
        command, args = parse_input(user_input)
        if command in COMMAND_EXIT:
            print("Good bye")
            break
        elif command == COMMAND_HELLO:
            print("How can I help you?")
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