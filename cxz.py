import random
def main():
    create_code_list()
    encode()

def create_code_list():
    import random
    user = int(input('Enter a number: '))
    random.seed(user)
    letter = 'abcdefghijklmnopqrstuvwxyz'
    drn = (random.sample(range(0,26),len(letter)))
    print (drn)
    return drn

def encode():
    letter = 'abcdefghijklmnopqrstuvwxyz'
    string = input('Enter a string: ')
    string_list = list(string)
    c = {}
    for i in range(len(string_list)):
        c[string_list[i]] = letter[i]
    
        

main()    
