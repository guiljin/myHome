from multiprocessing import Process, Queue
import os, time, random


def write(q):
    print("Process to write: %s" % os.getpid())
    for value in ['A', 'B', 'C']:
        print "Put %s to queue..." % value
        q.put(value)
        time.sleep(random.randint(10, 25))


def read(q):
    print("Process to read: %s" % os.getpid())
    while True:
        value = q.get(True)
        print "Get %s from queue." % value


if __name__ == "__main__":
    print("Main process: %s" % os.getpid())
    q = Queue()
    pw = Process(target=write, args=(q,))
    pr = Process(target=read, args=(q,))
    pw.start()
    print pw.pid
    pr.start()
    print pr.pid
    pw.join()
    pr.terminate()
