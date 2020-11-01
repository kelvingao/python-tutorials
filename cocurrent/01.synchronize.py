import time

def foo():
    print('42')
    time.sleep(1)
    print('1337')

def main():
    for _ in range(5):
        foo()

if __name__ == "__main__":
    start = time.time()
    main()
    end = time.time()
    print('Total Time: ' + str(end - start) + 's.')
