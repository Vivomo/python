import _thread
from time import sleep, ctime


def loop0():
    print('start loop0 at:', ctime())
    sleep(4)
    print('end loop0 at:', ctime())


def loop1():
    print('start loop1 at:', ctime())
    sleep(2)
    print('end loop1 at:', ctime())


def main():
    print('starting at:', ctime())
    _thread.start_new_thread(loop0, ())
    _thread.start_new_thread(loop1, ())
    sleep(6)
    print('all end as', ctime())


if __name__ == '__main__':
    main()

