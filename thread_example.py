import threading
import time
import random

def threadfunc(id, waitTime):
    for i in range(10):
        print(f"Inside thread {id}, step: {i}")
        time.sleep(waitTime)

def main():
    threads = []
    print("inside main")
    for id in range(5):
        thread = threading.Thread(target=threadfunc, args=(id, 0.1), daemon=True)
        threads.append(thread)
        thread.start()
    for thread in threads:
        thread.join()
    print("****End of main.")


if __name__ == "__main__":
    main()

