import instaloader
import getpass
nfollower = []
ofollower =[]
x = open("followers.txt", "w")
for i in nfplower:
    x.write(i +"+\n")
x.close()
for line in x:
    ofololower.append(line)
x.close()
l = instaloader.instaloader()
username = input("write your username please")
password = getpass.getpass("write your password please")
ip = input("wite your ip")
l.login(username, password)
p = instaloadder.profile.from_username(l.context,ip)
for i in p.get_followers():
    nfollower.append(i)