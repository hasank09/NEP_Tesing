
import socket

# ip = '195.230.110.49'
# port = 8000

ip = '45.79.112.203'
port = 4242

def test_tcp_connection(ip_test, port_test):

    try:
        # Creare il socket per la connessione TCP
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:

            s.settimeout(5)
            print(f"Trying to connect to {ip_test}:{port_test}...")

            s.connect((ip_test, port_test))
            print(f"Connection to {ip_test}:{port_test} succeeded!")



    except socket.timeout:
        print(f"Connection to {ip_test}:{port_test} timed out.")
    except socket.error as e:
        print(f"Failed to connect to {ip_test}:{port_test}: {e}")


test_tcp_connection(ip,port)

