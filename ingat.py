import os, sys, time
from urllib2 import *
from platform import system

os.system("clear")
print
kunci = raw_input("Masukkan Dulu Kuncinya Bos: ")
if kunci == 'tuman gans':
   print
   print "Guud Anjeng"
print
print "==========================="
print "===Author : Tuman=========="
print "==Team : 22XploiterCrew===="
print "=Thanks To all Member 22XC="
print "==========================="
time.sleep(1)
print
print "\033[1m\033[32m[+]\033[36m Whois lookup"
time.sleep(0.1)
print "\033[32m[+] \033[36mDNS lookup"
time.sleep(0.1)
print "\033[32m[+]\033[36m Reverse DNS lookup"
time.sleep(0.1)
print "\033[32m[+]\033[36m GeoIP lookup"
time.sleep(0.1)
print "\033[32m[+] \033[36mReverse IP lookup"
time.sleep(0.1)
print "\033[32m[+] \033[36mHttp Response"
time.sleep(0.1)
print "\033[32m[+] \033[36mPing"
time.sleep(0.1)
print "\033[32m[+] \033[36mPage Link"
time.sleep(0.1)
print "\033[32m[+] \033[36mNmap"
time.sleep(0.1)
print "\033[32m[+] \033[36mTraceroute"
print
print
ip = raw_input("Masukkan domain: ")
def reverseip():
              print
              os.system("Reverse IP")
              print
              os.system("curl https://api.hackertarget.com/reverseiplookup/?q=" + ip)
def ping():
              print
              os.system("figlet Ping Attack")
              print
              os.system("curl https://api.hackertarget.com/nping/?q=" + ip)
def http():
              print
              os.system("figlet Http Headers")
              print
              os.system("curl api.hackertarget.com/httpheaders/?q=" + ip)
def plink():
              print
              os.system("figlet Page Link")
              print
              os.system("curl https://api.hackertarget.com/pagelinks/?q=" + ip)
def nmap():
              print
              os.system("figlet Nmap")
              print
              os.system("curl https://api.hackertarget.com/nmap/?q=" + ip)
def dns():
             print
             os.system("figlet Dns Lookup")
             print
             os.system("curl https://api.hackertarget.com/dnslookup/?q=" + ip)
def whois():
             print
             os.system("figlet Whois")
             print
             os.system("curl https://api.hackertarget.com/whois/?q=" + ip)
def geoip():
             print
             os.system("figlet Geo IP")
             print
             os.system("curl https://api.hackertarget.com/geoip/?q=" + ip)
def  trace():
             print
             os.system("figlet Traceroute")
             print
             os.system("curl https://api.hackertarget.com/mtr/?q=" + ip)
print
ping()
http()
plink()
nmap()
dns()
whois()
geoip()
trace()
reverseip()
sys.exit()
