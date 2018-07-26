import os;
import sys;
import re;
from threading import Thread;



class TheHarvester:
	
	
	def __init__ (self, domain, parse):
		self.domain = domain;
		self.parse=parse;
		os.system("mkdir "+domain);
		
	def googleFunction(self):
		a = "theharvester -d "+self.domain+" -l 500 -b google -h >> /root/Desktop/"+self.domain+"/google.txt";
		os.system(a);
		self.parse.parseDomainname("/root/Desktop/"+self.domain+"/google.txt",self.domain);

	def bingFunction(self):
		a = "theharvester -d "+self.domain+" -l 500 -b bing -h >> /root/Desktop/"+self.domain+"/bing.txt";
		os.system(a);
		self.parse.parseDomainname("/root/Desktop/"+self.domain+"/bing.txt",self.domain);

	def linkledinFunction(self):
		a = "theharvester -d "+self.domain+" -l 500 -b linkedin -h >> /root/Desktop/"+self.domain+"/linkedin.txt";
		os.system(a);
		self.parse.parseDomainname("/root/Desktop/"+self.domain+"/linkedin.txt",self.domain);

class DnsEnum:
		
	def __init__ (self, domain, parse):
		self.domain = domain;
		self.parse=parse;

	def dnsenumFunction(self):
		a = "dnsenum "+self.domain+" >> /root/Desktop/"+self.domain+"/dnsenum.txt";
		os.system(a);
		self.parse.parseDomainname("/root/Desktop/"+self.domain+"/dnsenum.txt",self.domain);

class ParseFile:

	def parseDomainname(self, file_name, domain):
		os.system("./domain.sh "+file_name+" "+domain+" >> /root/Desktop/"+domain+"/result.txt");
		lines = open("/root/Desktop/"+domain+"/result.txt", 'r').readlines();
		lines_set = set(lines);
		out  = open("/root/Desktop/"+domain+"/result.txt", 'w');

		for line in lines_set:
    			out.write(line);
		
#==================================================================================================================

print("Search infromation was start");

arguments = sys.argv[1];

parse = ParseFile();

p1 = TheHarvester(arguments, parse);
p2 = DnsEnum(arguments, parse);

parse = ParseFile();

threadGoogle = Thread(target=p1.googleFunction);
threadBing = Thread(target=p1.bingFunction);
threadLinkedin = Thread(target=p1.linkledinFunction);
threadDnsEnum = Thread(target=p2.dnsenumFunction);

threadGoogle.start();
threadBing.start();
threadLinkedin.start();
threadDnsEnum.start();


threadGoogle.join();
threadBing.join();
threadLinkedin.join();
threadDnsEnum.join();


print("Search infromation was finish");




