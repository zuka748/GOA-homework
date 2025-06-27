def validate_hello(greeting):
    greetings_list = ["hello", "ciao", "salut", "hallo", "hola", "ahoj", "czesc"]
    greeting = greeting.lower() 
    for i in greetings_list:
        if i in greeting:
            return True
    return False
