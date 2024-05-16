import threading 
import socket 

def listen_for_messages_from_server(client):
    while 1:
        message = client.recv(2048).decode('utf-8')
        if message != '':
            username = message.split("~")[0]
            content = message.split("~")[1]
            
            print(f"[{username}] {content}")
        else:
            print("Message received from client is empty")
            
            
def send_message_to_server(client):
    
    while 1:
        message = input("Message:")
        
        if message != '':
            client.sendall(message.encode())
        else:
            print("Empty Message")
            exit(0)

def communicate_to_server(client):
    
    username = input("Enter Username: ")
    if username != '':
        client.sendall(username.encode())
        
    else:
        print("Username Cannot be empty")
        exit(0)
        
    threading.Thread(target=listen_for_messages_from_server,args=(client,)).start()
    
    send_message_to_server(client)

def main():
    client = socket.socket()
    client.connect(('localhost',1234))
    print("Successfully Connected to Server")
    
    communicate_to_server(client)

if __name__ == '__main__':
    main()