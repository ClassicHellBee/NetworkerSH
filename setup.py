import time
import sys
import os
import itertools # Not already in use
import gzip # Not already in use

start = False

if(sys.argv[1] == '-h'):
    time.sleep(0.7)
    print('Displaying options:')
    time.sleep(1)
    print('[-h]: Show all the options')
    print('[-run]: To make simple nmap scan')
    print('[-start]: To make advanced nmap scan')
    print('[-ifconfig]: To show your device config')
    print('[-iwconfig]: To show the wireless config')
    print('[-runconfig]: To config the run file')
    print('[-startconfig]: To config the start file')
    print('[-websitescan]: To scan a website')
    print('[-websiteconfig]: To config the website file')
    print('[-i]: To install the dependences')
    print('[-ssh]: To make ssh connection')
    print('[-sshconfig]: To config the ssh connection')
    print('[-service] + stop/start: To start/stop a ssh transference')
    print('[-itermux]: To install the dependences for termux users')

elif(sys.argv[1] == '-run'):
    os.system('bash network.sh')

elif(sys.argv[1] == '-start'):
    os.system('bash networkadv.sh')

elif(sys.argv[1] == '-ifconfig'):
    os.system('bash ifcnfg.sh')

elif(sys.argv[1] == '-iwconfig'):
    os.system('bash iwcnfg.sh')

elif(sys.argv[1] == '-runconfig'):
    os.system('nano network.sh')

elif(sys.argv[1] == '-startconfig'):
    os.system('nano networkadv.sh')

elif(sys.argv[1] == '-websitescan'):
    time.sleep(1)
    print('Redirecting to bash file...')
    time.sleep(0.6)
    os.system('bash website.sh')

elif(sys.argv[1] == '-websiteconfig'):
    os.system('nano website.sh')

elif(sys.argv[1] == '-i'):
    os.system('bash install.sh')

elif(sys.argv[1] == '-ssh'):
    time.sleep(1)
    os.system('bash securesh.sh')

elif(sys.argv[1] == '-sshconfig'):
    os.system('nano securesh.sh')

elif(sys.argv[1] == '-service'):
    if(sys.argv[2] == 'start'):
        start = True
    elif(sys.argv[2] == 'stop'):
        start = False
    else:
        print(' ')

while(start == True):
    service = True

else:
    service = False

if(service == True):
    os.system('bash service.sh')

else:
    print(' ')

if(sys.argv[1] == '-itermux'):
    os.system('bash itermux.sh')

else:
    print(' ')
