import socket

def fetch_data():
    # Create a socket object
    mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    try:
        # Connect to the server (data.pr4e.org) on port 80
        mysock.connect(('data.pr4e.org', 80))
        
        # Create HTTP GET request
        cmd = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\r\n\r\n'.encode()
        mysock.send(cmd)
        
        # Read and decode the response
        data = ''
        while True:
            received = mysock.recv(512)
            if len(received) < 1:
                break
            data += received.decode()
            
        # Close the socket
        mysock.close()
        
        # Split the response to separate headers and content
        # The response contains HTTP headers and actual content separated by \r\n\r\n
        header, content = data.split('\r\n\r\n', 1)
        print('--- Content ---')
        print(content)
        
    except Exception as e:
        print(f'Error: {e}')
        mysock.close()

if __name__ == '__main__':
    fetch_data()
