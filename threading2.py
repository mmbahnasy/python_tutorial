import threading, time

class DataObject:
    def __init__(self):
        self.resource = 0
        self._lock = threading.Lock()

    def locked_update(self, name):
        print(f"Thread {name}: starting update")
        print(f"Thread {name} about to lock")
        with self._lock:
            print(f"Thread {name} has lock")
            local_copy = self.resource
            local_copy += 1 # do more processing
            time.sleep(0.1)
            self.resource = local_copy
            print(f"Thread {name} about to release lock")
        print(f"Thread {name} after release")
        print(f"Thread {name}: finishing update")


def main():
    db = DataObject()
    threads = []
    for i in range(2):
        t = threading.Thread(target=DataObject.locked_update, args=(db, f"OP{i}"))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

if __name__ == "__main__":
    main()

