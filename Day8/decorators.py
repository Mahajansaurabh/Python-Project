def decorate_greeting(function):

    def another_function(word):

        print('Hello')
        function(word)
        print('Goodbye')

    return another_function()


def uppercase(text):
    print(text.upper())


def lowercase(text):
    print(text.lower())

decorate_upperase = decorate_greeting(uppercase)

decorate_upperase('saur')

