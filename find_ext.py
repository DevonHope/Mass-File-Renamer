# find all extensions in folders

import os

def ask():
    #print('Path to folder: ')
    path = input('Path to folder: ')

    # clean input
    print('\ncleaning input...')

    slash = '\\'
    # find slash direction (for different os)
    # assume windows, \
    if (not slash in path):
        slash = '/'

    print('OS determined...')

    if (not slash in path[-1]):
        print('cleaning path...')
        path = path + slash
        print('new path: \n\t'+path)

    print('input cleaned...\n')

    answers = [path, slash]

    return answers

def findext(a):
    ext = []
    ext_len = 4

    folders = []
    c = 0
    for root, dirs, files in os.walk(a[0]):
        if (c == 1):
            break
        folders.append(dirs)
        c+=1

    print('Folders found:')
    for f in folders[0]:
        print('\t'+f)

    for di in folders[0]:
        print('\nlooking through: '+di+'\n')
        for root, dirs, files in os.walk(a[0]+di):
            for f in files:
                new_ext = f[-ext_len:]
                if (new_ext[0] == '.'):
                    if (not new_ext in ext):
                        ext.append(new_ext)
                        print('added ext: '+new_ext)

    print('extensions found:')
    for e in ext:
        print('\t'+e)

def main():
    a = ask()
    findext(a)

if __name__ == '__main__':
    main()
