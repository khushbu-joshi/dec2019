import socket,time
target_ip="192.168.43.63"
target_port=1233

#now we are creating UDP socket --this is for all sender & receiver
#           ipv4    , UDP
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

#this is only for receiver
#s.bind((target_ip,target_port))
#while True:
    #print(s.recvfrom(100))
    #time.sleep(2)
    #
#this is for senders
while True:
    msg=input("please enter your msg : ")
#we have to encode string to byte like object in python3
    newmsg=msg.encode('ascii')
print(newmsg)
#now we can send to target
    s.sendto(newmsg,(target_ip,target_port))
    #print(s.recvfrom(100))
