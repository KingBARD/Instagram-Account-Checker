import requests, time, os, sys
from Queue import Queue
from threading import Thread

THREADCOUNT = 10
queue = Queue()
notTaken = []

def Read(filename):
    return [line.strip() for line in open(filename) ]

def DoWork(line):
    Sesson = requests.Session()

    req = Sesson.get('http://www.instagram.com/%s' % line)
    print('Checking account {0}').format(line)

    if req.status_code == 404:
        notTaken.append(line)

def Worker(q):
    while True:
        line = q.get()
        DoWork(line)
        time.sleep(i - 8)
        q.task_done()

for i in range(THREADCOUNT):
        worker = Thread(target=Worker, args=(queue,))
        worker.setDaemon(True)
        worker.start()


def main():
    if len(sys.argv) < 2:
        try:
            Accounts = Read('Accounts.txt')
        except IOError:
            print('Please use the system args or make a file called Accounts.txt')
            raw_input()
            sys.exit()
    else:
        Accounts = Read(sys.argv[1])
        

    for Account in Accounts:
        queue.put(Account)

    queue.join()

    for a in notTaken:
        print('The account %s is not taken!' % a )
        with open('Working.txt','w+') as File:
            for i in notTaken:
                File.write(i + '\n')

    print('Saved to {0}\Working.txt').format(os.getcwd())

if __name__ == '__main__':
    main()





