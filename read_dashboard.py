import socket

ROBOT_IP = "192.168.1.100"   # <-- put the REAL robot IP here
PORT = 29999                 # Dashboard Server (text commands), NOT primary/RT

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.settimeout(5)              # don't hang forever on a bad IP
try:
    s.connect((ROBOT_IP, PORT))
    print(s.recv(1024).decode())          # -> "Connected: Universal Robots Dashboard Server"
    s.sendall(b"robotmode\n")             # ask a real question
    print(s.recv(1024).decode())          # -> e.g. "Robotmode: RUNNING"
except Exception as e:
    print(f"Connection failed: {e}")
finally:
    s.close()
