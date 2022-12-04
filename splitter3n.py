import sys, os


print ("""  
 [#] Create By ::
 
  __  __        ____  _____  _  _______  ___   ___  
 |  \/  |      |  _ \|  __ \| |/ /  __ \|__ \ / _ \ 
 | \  / |_ __  | |_) | |  | | ' /| |__) |  ) | (_) |
 | |\/| | '__| |  _ <| |  | |  < |  _  /  / / > _ < 
 | |  | | |_   | |_) | |__| | . \| | \ \ / /_| (_) |
 |_|  |_|_(_)  |____/|_____/|_|\_\_|  \_\____|\___/ 
                                                                                                        
                             Lists Splitter
""")
	


def run(yList, maxi, exp):
	sites = open(yList,'r')
	number = 1
	counter = 1
	for site in sites :
		try :
			site = site.strip()
			if counter <= maxi:
				open('list-'+str(number)+'.txt', 'a').write(site+'\n')
				counter = counter + 1
			else :
				os.system("start cmd /c " + exp + ' list-'+str(number)+'.txt')
				number = number + 1
				open('list-'+str(number)+'.txt', 'a').write(site+'\n')
				counter = 2
		except :
			pass
	os.system("start cmd /c " + exp + ' list-'+str(number)+'.txt')
	print ('\n   ./Done')

yList = str(input('   Your List --> : '))
maxi = int(input('   Maximum of every list --> : '))
exp = str(input('   Your Exploiter --> : '))
run(yList, maxi, exp)