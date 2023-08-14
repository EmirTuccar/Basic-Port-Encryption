
import os

print("\n*************************************")
print("*")
print("*       Emir Zekeriya Tuccar  ")
print("*  Basic Port Encryption by sequence  ")
print("*")
print("******************************************")


my_list = []

def secret():
    port = int(input("Which Port do you want to encrypt: "))

    giris = input("How much input you want to set for encryption:")

    for i in range (int(giris)):
        my_list.append(int(input("Enter a port value: ")))

	
    print(my_list)

    os.system("sudo iptables -I INPUT -p tcp --dport %2d -j DROP;"%(int(port)))

    os.system("sudo iptables -I INPUT -p tcp --dport %2d -j DROP;"%(int(my_list[0])))
    os.system("sudo iptables -I INPUT -p tcp --dport %2d -j DROP;"%(int(my_list[1])))
    os.system("sudo iptables -I INPUT -p tcp --dport %2d -j DROP;"%(int(my_list[2])))
    

    
    os.system("sudo iptables -I INPUT -p tcp --dport %2d -m recent --rcheck --seconds 30 --name PORTKNOCK -j ACCEPT;"%(int(port)))
        
    os.system("sudo iptables -I INPUT -p tcp --dport %2d -m recent --set --name PORTKNOCK -j DROP;"%( int(my_list[0])))
    os.system("sudo iptables -I INPUT -p tcp --dport %2d -m recent --rcheck --seconds 10 --name PORTKNOCK -j DROP;"%( int(my_list[1])))
    os.system("sudo iptables -I INPUT -p tcp --dport %2d -m recent --rcheck --seconds 10 --name PORTKNOCK -j ACCEPT;"%( int(my_list[2])))

if __name__== "__main__":
	secret()

