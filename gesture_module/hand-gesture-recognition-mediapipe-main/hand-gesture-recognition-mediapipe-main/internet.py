import socket
import wikipedia
def check_internet_connection():
    # print("calles")
    try:
        sock = socket.create_connection(("www.google.com", 80))
        # print(sock)
        if sock is not None:
            # print('Clossing socket')
            sock.close
        return True
    except OSError:
        return False

def check_on_wikipedia(query):
    if check_internet_connection():
        query = query.lower()
        query = query.replace("who is","")
        query = query.replace("do you","")
        query = query.replace("know","")
        query = query.replace("about","")
        query = query.replace("tell me","")
        query = query.replace("can you","")
        query = query.replace("meant by","")
        query = query.strip()

        try:
            return wikipedia.summary(query,sentences = 2)
        except Exception as e:
            return False
    else:
        return "Internet is not connected"