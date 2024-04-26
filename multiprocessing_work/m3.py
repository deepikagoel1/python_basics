import multiprocessing
import time

def sender(conn):
    while True:
        msgs = input("Write a message to send to receiver")
        conn.send(msgs)
        
        #   conn.close()
        print("\n Sender Messages {}".format(msgs), end = "\n\n")
        time.sleep(10)

def receiver(conn):
    while True:
        try:
            msg = conn.recv()
        except Exception as e:
            print(e)
            break
        print("\n Received Message {}".format(msg), end = "\n\n")
        time.sleep(10)


if __name__ == "__main__":

    sender_conn, receiver_conn = multiprocessing.Pipe()
    p1 = multiprocessing.Process(target = sender, args = (receiver_conn,))
    p2 = multiprocessing.Process(target = receiver, args = (sender_conn,))

    p1.start()
    p2.start()

    p1.join()
    p2.join()