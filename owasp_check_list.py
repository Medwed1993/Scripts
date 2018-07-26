import os;
import sys;
import re;
import subprocess


arguments = sys.argv[1];

print("==================");
print("= WAF is decting =");
print("==================");
os.system("cd ~/wafw00f/wafw00f/bin && ./wafw00f https://"+arguments);


print("\n==============================================================================================");
print("= Testing for Weak SSL/TSL Ciphers, Insufficient Transport Layer Protection (OTG-CRYPST-001) =");
print("=============================================================================================="); 
os.system("sslscan "+arguments);


print("\n========================================================");
print("= Enumerate Applications on Webserver (OTG-INFO-004) =");
print("========================================================"); 
os.system("nmap -PN -sT -sV -p0-65535 "+arguments);

print("\n========================================================");
print("= Test HTTP Strict Transport Security (OTG-CONFIG-007) =");
print("========================================================"); 
os.system("curl -s -D- https://"+arguments+" | grep Strict");


print("\n====================================================");
print("= Testing for HTTP Verb Tampering (OTG-INPVAL-003) =");
print("===================================================="); 
os.system("./verb_tempering.sh "+arguments);


print("\n\n=======================================================================");
print("= Discover the Supported Methods - Test HTTP Methods (OTG-CONFIG-006) =");
print("======================================================================="); 
os.system("nmap -p 443 --script http-methods "+arguments);

print("\n=======================================================");
print("= Fingerprint Web Application Framework (OTG-INFO-008) =");
print("========================================================"); 
os.system("whatweb -a 3 "+arguments);

print("\n================================================");
print("= Test RIA cross domain policy (OTG-CONFIG-008) =");
print("================================================="); 
os.system("wget http://"+arguments+"/crossdomain.xml");
print("\n");
os.system("wget http://"+arguments+"/clientaccesspolicy.xml");
