import threading, time

class DataObject:
    def __init__(self):
        self.resource = 0

    def locked_update(self, name):
        print(f"Thread {name}: starting update")
        local_copy = self.resource
        local_copy += 1 # do more processing
        time.sleep(0.1)
        self.resource = local_copy
        print(f"Thread {name}: finishing update with resource value = {self.resource}")


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

