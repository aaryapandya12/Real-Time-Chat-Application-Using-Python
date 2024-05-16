import socket 
import threading

active_clients =[] #List of all currently connected users 

#Function to listen for upcoming messages from a client
def listen_messages(client,username):
    
    while 1:
        message = client.recv(2048).decode('utf-8')
        if message != '':
            final_msg = username + '~' + message
            send_messages_to_all(final_msg)
        else:
            print(f"The message sent from client {username} is empty")
            

#Function to send message to a single client          
def send_message_to_client(client,message):
    client.sendall(message.encode())
        

#Function to send any new message to all the clients that are connected to the server
def send_messages_to_all(message):
    for user in active_clients:
        send_message_to_client(user[1],message)
#Function to Handle Clients
def client_handler(client):
    while 1:
        username = client.recv(2048).decode('utf-8')#2048 means maximum size of the message
        if username != '':
            active_clients.append((username,client))
            prompt_message = "SERVER~" + f"{username}added to the chat"
            send_messages_to_all(prompt_message)
            break
            
        else:
            print("Client Username is Empty")
    
    threading.Thread(target=listen_messages,args = (client,username,)).start()

def main():
    server = socket.socket()

    server.bind(('localhost',1234))
    print("Server is Connected Successfully")
        
    server.listen(5)
    
    while 1:
        client,address = server.accept()
        print(f"Connected to Client {address[0]} {address[1]} , username") 
        
        threading.Thread(target=client_handler,args =(client,)).start()

if __name__ == '__main__':
    main()