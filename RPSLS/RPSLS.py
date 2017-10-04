# Rock Paper Scissors Lizard Spock Game
# Game Designer : Sam Kass
# Mini Project Idea : Coursera

from random import randint
import webbrowser


def rules():
    print('======= Rules and Regulations =======')
    print('Rock CRUSHES Scissor')
    print('Rock CRUSHES Lizard')
    print('Paper COVERS Rock')
    print('Paper DISPROVES Spock')
    print('Scissor CUTS Paper')
    print('Scissor DECAPITATES Lizard')
    print('Lizard POISONS Spock')
    print('Lizard EATS Paper')
    print('Spock SMASHES Scissor')
    print('Spock Vaporises Rock')
    print('All TIEs with same.')


def what_happened(user, comp):
    nuser = name_to_num(user)
    ncomp = name_to_num(comp)
    if (nuser is 0 and ncomp is 4) or (nuser is 4 and ncomp is 0):
        print('Rock CRUSHES Scissor')
    elif (nuser is 0 and ncomp is 3) or (nuser is 3 and ncomp is 0):
        print('Rock CRUSHES Lizard')
    elif (nuser is 2 and ncomp is 0) or (nuser is 0 and ncomp is 2):
        print('Paper COVERS Rock')
    elif (nuser is 2 and ncomp is 1) or (nuser is 1 and ncomp is 2):
        print('Paper DISPROVES Spock')
    elif (nuser is 2 and ncomp is 4) or (nuser is 4 and ncomp is 2):
        print('Scissor CUTS Paper')
    elif (nuser is 3 and ncomp is 4) or (nuser is 4 and ncomp is 3):
        print('Scissor DECAPITATES Lizard')
    elif (nuser is 3 and ncomp is 1) or (nuser is 1 and ncomp is 3):
        print('Lizard POISONS Spock')
    elif (nuser is 3 and ncomp is 2) or (nuser is 2 and ncomp is 3):
        print('Lizard EATS Paper')
    elif (nuser is 1 and ncomp is 4) or (nuser is 4 and ncomp is 1):
        print('Spock SMASHES Scissor')
    elif (nuser is 1 and ncomp is 0) or (nuser is 0 and ncomp is 1):
        print('Spock Vaporises Rock')
    else:
        print(user + TIES + comp)


def num_to_name(num):
    if num == 0:
        cname = 'rock'
    elif num == 1:
        cname = 'spock'
    elif num == 2:
        cname = 'paper'
    elif num == 3:
        cname = 'lizard'
    elif num == 4:
        cname = 'scissors'
    return cname


def name_to_num(name):
    if name.lower() == 'rock':
        cnum = 0
    elif name.lower() == 'spock':
        cnum = 1
    elif name.lower() == 'paper':
        cnum = 2
    elif name.lower() == 'lizard':
        cnum = 3
    elif name.lower() == 'scissors':
        cnum = 4
    return cnum


def rpsls():
    print('====== RPSLC ======')
    print('Choose among Rock, Paper, Scissor, Lizard or Spock ?')
    try:
        name = raw_input()
    except NameError:
        name = None
    if name is None:
        name = input()
    player = name_to_num(name)
    comp = randint(0, 4)
    comp_name = num_to_name(comp)

    print('You ->', name.title())
    print('Computer ->', comp_name.title())

    what_happened(name, comp_name)

    if (comp + 1) % 5 is player or (comp + 2) % 5 is player:
        print('You Won !!!')
    elif comp is player:
        print('You Tried Well, But its a TIE')
    else:
        print('Hard Luck, Computer Won !!')

    print()
    main()


def main():
    print('====== Menu ======')
    print('1. Play')
    print('2. See Source Code')
    print('3. Rules')
    print('4. Rules dictation by Sheldon Lee Cooper')
    print('5. Exit')
    inp = int(input('Enter Choice :'))
    if inp is 1:
        rpsls()
    elif inp is 3:
        rules()
    elif inp is 4:
        webbrowser.open('https://goo.gl/kR2653')
    elif inp is 5:
        exit()
    elif inp is 2:
        webbrowser.open('https://goo.gl/4TStoZ')
    if inp is not 5:
        main()


if __name__ == "__main__":
    main()
