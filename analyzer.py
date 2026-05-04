 import csv

f=open('twelve.txt')

raw=f.readlines()

rawlines=[]

rawmark=[]

for lines in range(len(raw)):

	if raw[lines][0].isdigit():

		rawlines.append(raw[lines].split())

		rawmark.append(raw[lines+1].split())

for studentno in range(len(rawlines)):

	print('Sending Data:')

	print(rawlines[studentno])

	print(rawmark[studentno])

	print()

	

def subgradecount(rawlines,rawmark):

	global subcode

	subcode=[]

	for codel in rawlines:

		stucode=[]

		for i in codel[1::]:

			if i.isdigit():

				stucode.append(i)

		subcode.append(stucode)

	d={}

	for i in range(len(subcode)):

		for j in range(len(subcode[i])):

			if subcode[i][j] in d:

				d[subcode[i][j]]+=[rawmark[i][j*2+1]]

			else:

				d[subcode[i][j]]=[rawmark[i][2*j+1]]

	return d

	

def count(dict,dict_key):

	grades=['A1','A2','B1',"B2","C1","C2","D1","D2","E"]

	countdict={}

	for g in grades:

		countdict[g]=dict[dict_key].count(g)

	return countdict



D=subgradecount(rawlines,rawmark)



for code in D:

	print(f'{code} : {count(D,code)}')

	

def subPI(D, code):

	dic=count(D,code)

	PI=0

	wtage=8

	n=sum(dic.values())

	for grade in dic:

		PI+=(dic[grade]*wtage*100)/(n*8)

		wtage-=1

	return PI



print()

for pi in D:

	print(f'PI of subject {pi} is : {subPI(D,pi)}')

	

def namelist(rawlines):

	names=[]

	for lines in rawlines:

		j=" "

		for ele in lines[2::]:

			if ele.isalpha():

				j+=ele+' '

			elif ele.isdigit():

				break

		names.append(j.strip())

	return names

print(namelist(rawlines))

############################

def studentPI_list(D):

	l=[]

	grades=['A1','A2','B1',"B2","C1","C2","D1","D2","E"]

	PI=0

	for code in D:

		dic=count(D,code)

		w=8

		rawPI=0

		for g in grades:

			rawPI+=dic[g]*w

			w-=1

		PI+=(rawPI*100)/(sum(dic.values())*40)

	return PI

print(studentPI_list(D))

print(subcode)



###

'''

testlist={}

for n in range(len(subcode)):

	if tuple(subcode[n]) in testlist:

		testlist[tuple(subcode[n],)]+=(namelist(rawlines)[n],)

	else:

		testlist[tuple(subcode[n],)]=(namelist(rawlines)[n],)

print(testlist)

'''

###



finalline=[]

code=list(D.keys())

for line in range(len(rawlines)):

	l=[]

	l+=(rawlines[line][0:2])

	l.append(namelist(rawlines)[line])

	for i in range(len(code)):

		if code[i] in subcode[line]:

			idx=subcode[line].index(code[i])

			l.append(rawmark[line][idx*2])

		else:

			l.append('NA')

	mark_sum=0

	for mark in rawmark[line]:

		if mark.isdigit():

			mark_sum+=int(mark)

	percentage=100*mark_sum/500

	l.append(percentage)

	finalline.append(l)

	

cvf=open('g.csv','w')

writer=csv.writer(cvf)

head=['ROLL NO.','GENDER','NAME']

head=head+(code)+['PERCENTAGE']

writer.writerow(head)

for row in finalline:

	writer.writerow(row)



cvf2=open('analysis.csv','w')

writer=csv.writer(cvf2)

writer.writerow(['School PI', studentPI_list(D)])

writer.writerow(['SUBJECT WSE PI:'])

for pi in D:

	st='PI of '+str(pi)

	writer.writerow([st, subPI(D, pi)])
