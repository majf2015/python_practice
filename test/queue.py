stack = []

def appends():
    stack.append(raw_input('enter one string').strip().lower())

def pops():
    if len(stack) == 0:
        print 'stack is empty'
    else:
        print '%s' % stack.pop(0) , 'is removed form stack'
def views():
    print stack

dir = {'a' : appends, 'p' : pops, 'v' : views}
def menus():
    menu = '''
        a:appends
        p:pops
        v:views
        q:quit
        enter choice: '''
    while True:
        while True:
            try:
                choice = raw_input(menu).strip().lower()
            except(IndexError, KeyboardInterrupt,EOFError):
                choice = 'q'

            print 'you choice : %s' % choice
            if choice not in 'apvq':
                choice = 'q'
            else:
                break
        if choice == 'q':
            break

        dir[choice]()
menus()