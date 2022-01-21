# python program to rename media files for tv shows
# Author: Devon Hope

# Korra Example
# The.Legend.of.Korra.S01E01-E02.720p.HDTV.x264-HWE
# E01-E02.mkv

import os
import importlib
import pip
from datetime import datetime
import shutil

video_ext = [] # ['.mpg','.mkv','.mp4','.avi']
ext_len = 4

# dev variables
dev_mode = 0
test_folder = '/var/services/video/TV_Test/'
og_folder = '/var/services/video/TV Shows/'

# choice lists
yes = ['y','yes']
no = ['n','no']

# auto install with pip any needed packages
def import_with_auto_install(package):
    try:
        print('PACKAGE: '+ package + '.....INSTALLED\n ')
        return importlib.import_module(package)
    except:
        print('PACKAGE: '+ package + '.....INSTALLING\n ')
        pip.main(['install',package])

    return importlib.import_module(package)

# the point of the script
def explain():
    # explain
    print('-------------------------------------------------------------\n')
    print('MASS FILE EDITOR\n')
    print('\tA tool developed to change the name of a large number of\n\
    \tfiles without having to manually edit them individually.\n\
    \n\tThe tool is focused on removing a beginning section of the name\n \
    \tand an ending section. The sections are defined by the number of characters\n\
    \tfrom the beginning of the string to the end of the section. It will ask\n\
    \tfor these values below, as well as a path to the folder containing\n\
    \tthe files, a file extension, and beginning text identifier that is commonly\n\
    \tfound at the beginning of each name.')

    print('\n\nEXAMPLE:\n')
    print('filenames:\n\
    \t30 Rock (2005) - S01E01 - NAME01 (bitrate or someshit 1080p).mkv\n\
    \t30 Rock (2005) - S01E02 - NAME02 (bitrate or someshit 1080p).mkv\n\
    \t30 Rock (2005) - S01E03 - NAME03 (bitrate or someshit 1080p).mkv\n')

    print('input:')
    print('\tpath: \'C:\\some\\path\\to\\your\\files\'')
    print('\textension: \'.mkv\'')
    print('\tfront string: \'30 Rock (2005) - \'')
    print('\tback string: \' (bitrate or someshit 1080p)\'')

    print('\noutput:')
    print('\tE01 - NAME01.mkv\n\
    \tE02 - NAME02.mkv\n\
    \tE03 - NAME03.mkv\n')

    print('-------------------------------------------------------------\n')

# clean the input from the user
# currently only supports filename cleaning
def cleaninput(a):
    # clean input
    print('\ncleaning input...')
    slash = '\\'
    # find slash direction (for different os)
    # assume windows, \
    if (not slash in a[0]):
        slash = '/'

    print('OS determined...')
    if (not slash in a[0][-1]):
        print('cleaning path...')
        a[0] = a[0] + slash

    a.append(slash)

    print('input cleaned...\n')

    return a

# ask for specified attributes to rename
# files with
def ask():
    print('\n-------------------------------------------------------------\n')
    # ask for necessities
    path = input('Path to folder: ')
    search_ext = input('\nFile Extension: ')
    search_front = input('\nFront String: ')
    search_back = input('\nBack String: ')
    print('\n-------------------------------------------------------------\n')

    answers = [path, search_ext, search_front, search_back]
    answers = cleaninput(answers)

    return answers

# a general function for yes no
# proceed questions
def proceed():
    ch = input('\nProceed? (y/n) ')
    if not ch in yes:
        quit()
    else:
        return True

# print specified attributes
def printask(a):
    print('\nARE THESE CORRECT?\n')
    print('Path:\n\t' + a[0])
    print('File Extension:\n\t'+a[1])
    print('Front String:\n\t'+a[2])
    print('Back String:\n\t'+a[3])

# user chooses to run rename or not
def choose(a):
    # confirm choices
    choice=input('y/n? ')

    if(choice.lower() in yes):
        run(a)
        quit()

    while(not choice.lower() in yes):
        a = ask()
        printask(a)

        print('\ny/n? ')
        choice=input()

        if(choice.lower() in yes):
            run(a)
            quit()

# find and rename all files with selected attributes
# under specified folder path
def run(a):
    # structure of a
    # a = [path, ext, str front, str back, slash]

    # find front and back character lengths
    # new structure of a
    # a = [path, ext, str front, str back, slash, len front, len back]
    a.append(len(a[2]))
    a.append(len(a[3]) + len(a[1]))

    # get folders
    print('\nSearching ' + a[0] + '.....\n')

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
                print('old file: ' + f)

                if (a[2] in f and a[1] in f):
                    new_f = f[a[5]:]
                    new_f = new_f[:-a[6]]
                    new_f = new_f+a[1]
                    print('new file: ' + new_f+'\n')
                    f_path = a[0]+di+a[4]
                    os.rename(f_path+f,f_path+new_f)
                    c+=1

# find file extensions for video files in folder
def findext(a, imports):
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
        #print('\nlooking through: '+di+'\n')
        for root, dirs, files in os.walk(a[0]+di):
            if (files):
                for f in files:
                    new_ext = f[-ext_len:]
                    if (new_ext[0] == '.'):
                        if (not new_ext in video_ext):
                            # determine if video file
                            full_file = root+a[1]+f
                            get_type = imports[0].guess(full_file)

                            if get_type:
                                if 'video' in get_type.mime:
                                    # add ext to video ext
                                    video_ext.append(new_ext)

                        if (not new_ext in ext and new_ext in video_ext):
                            ext.append(new_ext)

    print('\nvideo extensions found:')
    for e in ext:
        print('\t'+e)

    return folders[0]

# find similar start strings
def common_start(sa, sb):
    """ returns the longest common substring from the beginning of sa and sb """
    def _iter():
        for a, b in zip(sa, sb):
            if a == b:
                yield a
            else:
                return

    common_st = ''.join(_iter())

    end_of_str = 'e'

    for i in range(9):
        if(common_st.endswith(end_of_str.lower(), len(common_st)-2, len(common_st))):
            common_st = common_st[:-1]
        if(common_st.endswith(end_of_str.upper(), len(common_st)-2, len(common_st))):
            common_st = common_st[:-1]
        if(common_st.endswith(end_of_str.lower()+str(i), len(common_st)-2, len(common_st))):
            common_st = common_st[:-2]
        if(common_st.endswith(end_of_str.upper()+str(i), len(common_st)-2, len(common_st))):
            common_st = common_st[:-2]

    return common_st

# find similar end strings
def common_end(sa, sb):
    """ returns the longest common substring from the end of sa and sb """
    # reverse strings
    sa = sa[::-1]
    sb = sb[::-1]
    def _iter():
        for a, b in zip(sa,sb):
            if a == b:
                yield a
            else:
                return

    common_end = ''.join(_iter())
    #print('\n\nCEND BEFORE EXT: '+common_end)
    # remove extension
    if (common_end[-ext_len:] in video_ext):
        common_end = common_end[:-ext_len]
        #print('CEND NEW: '+common_end+'\n\n')

    return common_end

# find common strings in four filenames within each
# folder that is searched
def findStrings(files):
    # loop through files and select two files from each folder
    # get first four names for common strings
    # compare length of returned strings
    f1 = f_start = 0
    s1 = s2 = s3 = s4 = str1 = str2 = end1 = end2 = final_str = final_end = ''
    found_str = False
    found_end = False
    ext = ''
    for f in files:
        if found_str:
            break
        if (f[-ext_len:] in video_ext):
            ext = f[-ext_len:]
            # find beginning string
            if (f1 == f_start):
                #print('\nFile: '+f)
                s1 = f
            elif (f1 == f_start+1):
                s2 = f
            elif (f1 == f_start+2):
                s3 = f
            elif (f1 == f_start+3):
                s4 = f
                # find first string
                str1 = common_start(s1, s2)
                str2 = common_start(s3, s4)
                end1 = common_end(s1,s2)
                end2 = common_end(s3,s4)

                #print('\nSTR1: '+str1+'\nSTR2: '+str2+'\nEND1: ' \
                #        +end1+'\nEND2: '+end2+'\n')

                if (not str1 or not str2):
                    # if either are empty
                    found_str = True
                    str1 = ''
                    str2 = ''

                if (not end1 or not end2):
                    found_end = True
                    end1 = ''
                    end2 = ''

                if (str1 != str2):
                    if f_start + 4 < len(files):
                        f_start += 4
                else:
                    final_str = common_start(str1,str2)
                    #print('FINAL START: '+final_str)
                    found_str = True

                if end1 != end2:
                    if f_start + 4 < len(files):
                        f_start += 4
                else:
                    final_end = common_end(end1,end2)
                    #print('FINAL END: '+final_end+'\n\n')
                    found_end = True

            else:
                final_str = common_start(str1,str2)
                final_end = common_end(end1,end2)
                found_str = True
                found_end = True

            f1 += 1

    if final_str and len(final_str) > 1 or \
        final_end and len(final_end) > 1:
        #print('\nROOT: '+root[28:])
        #print('final string: '+final_str)
        return [final_str, final_end, ext]

def autoRename(a, folders):
    print('\nStarting AutoRename...\n')

    a.append('')
    a.append('')
    a.append('')
    a.append('')
    a.append('')
    slash = a[1]
    # for dev mode save to file
    dir = os.getcwd()+a[1]+'log_rename'
    if not os.path.isdir(dir):
        os.makedirs(dir)
    now = datetime.now()
    date_time = now.strftime("%d-%m-%Y_%H-%M-%S")
    log_file = dir+a[1]+'log_rename_'+date_time+'.txt'
    fo = open(log_file, 'w')
    fo.write('DEV LOG\n\n\n')

    for di in folders:
        for root, dirs, files in os.walk(a[0]+di):
            if files and len(files) > 3:
                # get first & last string
                strings = findStrings(files)

                if strings:
                    # prepare answers
                    a[1] = strings[2]
                    a[2] = strings[0]
                    a[3] = strings[1]
                    a[4] = slash
                    a[5] = len(strings[0])
                    a[6] = len(strings[1]) + len(strings[2])

                    '''
                    print('\nanswers:')
                    for c, i in enumerate(a):
                        #if c == 2:
                            # for dev mode save to file
                            #fo.write('\nFS: '+i+'\n')
                            #fo.write('Root: '+root+'\n')
                        print('\ta['+str(c)+']'+str(i))
                    '''

                    #rename
                    for f in files:
                        #print('\nold file: ' + f)
                        if (a[1] in f):
                            new_f = f
                            if (a[2] in new_f):
                                new_f = new_f[a[5]:]
                            if (a[3] in new_f):
                                new_f = new_f[:-a[6]]

                            new_f = new_f+a[1]
                            #print('new file: ' + new_f+'\n')
                            f_path = root+a[4]
                            # comment out the line below to double check
                            # the renamed files before renaming them
                            os.rename(f_path+f,f_path+new_f)
                            fo.write('\nFile: '+f+'\nRenamed: '+new_f+'\n\n')
                            c+=1

    fo.close()


def autoMode(imports):
    print('\n-------------------------------------------------------------\n')
    print('\nEntering Auto Mode...\n')

    if dev_mode:
        print('\n\nDEV MODE\n\n')
        #print('\nCREATING TEST FOLDERS...\n')
        #createTestFolders(imports[1])
        path = test_folder
        print('\nTEST FOLDER: '+path)
        if proceed():
            pass
    else:
        # get path
        path = input('Path to folder: ')

    a = cleaninput([path])

    # find all video file extensions
    folders = findext(a, imports)

    # loop through each folder and find similar texts
    # then rename
    autoRename(a, folders)
    print('\n-------------------------------------------------------------\n')

    quit()

def createTestFolders(ap):
    # loop through og folder and find only the
    # first file to copy into TV_Test folder
    from alive_progress import alive_it

    epi_limit = 4
    c = 0
    i = 0
    show_limit = 5
    for root, dirs, files in alive_it(os.walk(og_folder)):
        if (i > show_limit):
            break
        if files:
            # progress alive bar
            for f in files:
                if c == epi_limit:
                    c=0
                    break

                # create copy dir structure
                path = test_folder+root.replace(og_folder,'')
                if not os.path.isdir(path):
                    os.makedirs(path)

                # copy file to path
                src = os.path.join(root,f)
                dst = os.path.join(path,f)
                if not os.path.isfile(dst):
                    shutil.copy(src,dst)

                c+=1
        i += 1

def quit():
    print('\n-------------------------------------------------------------\n')
    print('\n\nQUITING...\n')
    exit()

def main(imports):
    explain()

    amc = input('Auto Mode (y/n)? ')
    if(amc == 'y' or amc == 'Y'
        or amc == 'yes' or amc == 'Yes'
        or amc == 'YES'):

        autoMode(imports)
    else:
        a = ask()
        printask(a)
        choose(a)


if __name__ == "__main__":
    try:
        ft = import_with_auto_install('filetype')
        ap = import_with_auto_install('alive_progress')
        main([ft,ap])
    except KeyboardInterrupt:
        quit()
