
import argparse
import os
import platform

Parser = argparse.ArgumentParser()
Parser.add_argument('-on', action='store_true')
Parser.add_argument('-off', action='store_true')
Parser.add_argument('-save', action='store_true')
Parser.add_argument('-load', action='store_true')

Args = Parser.parse_args()

if platform.system() == 'Linux':
    Path = '/etc/hosts'
elif platform.system() == 'Windows':
    Path = 'C:\Windows\System32\Drivers\etc\hosts'

Loopback = '127.0.0.1 '

BlockedSites = open('sites2block.conf', 'r')

BlockedSites = list(BlockedSites.read().split('\n'))

if Args.save == True:
    DefaultConfiguration = open('default.conf', 'w+')
    DefaultConfiguration.write(open(Path).read())

if Args.load == True:
    File = open(Path, 'w+')
    File.write(open('default.conf', 'r').read())

elif Args.on == True:
    File = open(Path, 'a')
    for x in BlockedSites:
        print('blocked:', x, end='\n')
        File.write(Loopback + x + '\n')
        File.write(Loopback + 'www.' + x + '\n')

elif Args.off == True:
    print('Are you sure??? Hmmmm?')
    for x in range(0, 3):
        print('type three times phrase: I will survive nnn')
        if str(input(str(x+1) + ': ')) != 'I will survive nnn':
            print('wrong string')
            exit(3)

    File = open(Path, 'w+')
    DefaultConfiguration = open('default.conf', 'r')
    File.write(DefaultConfiguration.read())

