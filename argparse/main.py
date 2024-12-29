import argparse
import os
import shutil

def create(args):
    try:
     createfile = args.create[0]
     with open(createfile, 'x'):
        pass
     print('File created')
    except:
     print('Unexpected error')

def modify(args):
    try:
     modifyfile = args.modify[0]
     editdata = args.modify[1]
     with open(modifyfile, 'r+') as editfile:
        editfile.write(editdata)
     print('File modified')
    except:
     print('Unexpected error')

def delete(args):
    try:
     deletefile = args.delete[0]
     os.remove(deletefile)
     print('File deleted')
    except:
     print('Unexpected error')

def copy(args):
   try:
    copyfile = args.copyfile[0]
    copyto = args.copyfile[1]
    shutil.copy(copyfile, copyto)
   except:
    print('Unexpected error')


parser = argparse.ArgumentParser(description = 'PyTwK')

parser.add_argument('--create', type = str, nargs = 1, metavar = 'createfile', help = 'Create file')
parser.add_argument('--modify', type = str, nargs = 2, metavar = ('modifyfile', 'editdata'), help = 'Modify file')
parser.add_argument('--delete', type = str, nargs = 1, metavar = 'deletefile', help = 'Delete file')
parser.add_argument('--copy', type = str, nargs = 2, metavar = ('copyfile', 'copyto'), help = 'Copy file')

args = parser.parse_args()

if args.create != None:
    create(args)
elif args.modify != None:
    modify(args)
elif args.delete != None:
    delete(args)
elif args.copy != None:
    copy(args)