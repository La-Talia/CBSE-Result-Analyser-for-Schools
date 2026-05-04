#PROJECT::: CBSE RESULT ANALYSER
#RAXIT GUPTA
import csv
f=open('twelve.txt')
raw=f.readlines()
raw_lines=[]
rawmark=[]

for lines in range(len(raw)):
	if raw[lines][0].isdigit():
		raw_lines.append(raw[lines].split())
		rawmark.append(raw[lines+1].split())

rawlines=[]
for line in raw_lines:
	if len(line)!=0:
		if line[-1].isdigit():
			rawlines.append(line[:-1:])
		else:
			rawlines.append(line)

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

			if len(rawmark[i])!=2*len(subcode[i]):
				continue
			else:
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

def subPI(D, code):
	dic=count(D,code)
	PI=0
	wtage=8
	n=sum(dic.values())
	for grade in dic:
		PI+=(dic[grade]*wtage*100)/(n*8)
		wtage-=1
	return PI

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
def studentPI_list(rawmark):
	l=[]
	PI=0
	for i in rawmark:
		l.append(i[1::2])
	for filter in l:
		if filter==[]:
			l.remove([])
	for line in l:
		points=0
		for i in line:
			if i=='A1':
				points+=8
			elif i=='A2':
				points+=7
			elif i=='B1':
				points+=6
			elif i=='B2':
				points+=5
			elif i=='C1':
				points+=4
			elif i=='C2':
				points+=3
			elif i=='D1':
				points+=2
			elif i=='D2':
				points+=1
		if len(l)!=0:
			points=points/len(line)
		if points>7:
			PI+=8
		elif points>6:
			PI+=7
		elif points>5:
			PI+=6
		elif points>4:
			PI+=5
		elif points>3:
			PI+=4
		elif points>2:
			PI+=3
		elif points>1:
			PI+=2
		elif points>0:
			PI+=1
	PI=PI*100/(len(l)*8)
	return PI

def stusubs(rawlines):
	stu_subjects={}
	for line in rawlines:
		templ=[]
		for code in line[1::]:
			if code.isdigit():
				templ.append(code)
		stu_subjects[line[0]]=templ
	return stu_subjects
finalline=[]

code=list(D.keys())
def final(lines,mark):
	for line in range(len(lines)):
		l=[]
		l+=(lines[line][0:2])
		l.append(namelist(lines)[line])
		for i in range(len(code)):
			if len(mark[line])==0:
				l.append(None)
			else:
				if code[i] in subcode[line]:
					idx=subcode[line].index(code[i])
					l.append(mark[line][idx*2])
				else:
					l.append(None)
		mark_sum=0
		for m in mark[line]:
			 if m.isdigit():
			 	mark_sum+=int(m)
		percentage=mark_sum/(len(subcode[line]))
		l.append(percentage)
		finalline.append(l)
	return finalline
finalline=final(rawlines,rawmark)

def numpass(rawlines):
	c=0
	for line in rawlines:
		if line[-1]=='PASS':
			c+=1
	return c

subjects = {
    "001": "ENGLISH ELECTIVE-N",
    "002": "HINDI ELECTIVE",
    "003": "URDU ELECTIVE",
    "022": "SANSKRIT ELECTIVE",
    "027": "HISTORY",
    "028": "POLITICAL SCIENCE",
    "029": "GEOGRAPHY",
    "030": "ECONOMICS",
    "031": "CARNATIC MUSIC VOC",
    "034": "HIND.MUSIC VOCAL",
    "035": "HIND.MUSIC MEL.INS",
    "036": "HIND MUSIC.INS.PER",
    "037": "PSYCHOLOGY",
    "039": "SOCIOLOGY",
    "040": "PHILOSOPHY",
    "041": "MATHEMATICS",
    "042": "PHYSICS",
    "043": "CHEMISTRY",
    "044": "BIOLOGY",
    "045": "BIOTECHNOLOGY",
    "046": "ENGG. GRAPHICS",
    "048": "PHYSICAL EDUCATION",
    "049": "PAINTING",
    "050": "GRAPHICS",
    "051": "SCULPTURE",
    "052": "APP/COMMERCIAL ART",
    "053": "FASHION STUDIES",
    "054": "BUSINESS STUDIES",
    "055": "ACCOUNTANCY",
    "056": "DANCE-KATHAK",
    "057": "DANCE-BHARATNATYAM",
    "059": "DANCE-ODISSI",
    "061": "DANCE-KATHAKALI",
    "064": "HOME SCIENCE",
    "065": "INFORMATICS PRAC.",
    "066": "ENTREPRENEURSHIP",
    "067": "MULTIMEDIA & WEB T",
    "068": "AGRICULTURE",
    "069": "CR WRTNG TR STUDY",
    "070": "HERITAGE CRAFTS",
    "071": "GRAPHIC DESIGN",
    "072": "MASS MEDIA STUDIES",
    "073": "KNOW TRAD & PRAC.",
    "074": "LEGAL STUDIES",
    "075": "HUMAN RIGHTS & G S",
    "076": "NAT. CADET CORPS",
    "078": "THEATRE STUDIES",
    "079": "LIBRARY & INFO SC.",
    "083": "COMPUTER SCIENCE",
    "101": "ENGLISH ELECTIVE-C",
    "104": "PUNJABI",
    "105": "BENGALI",
    "106": "TAMIL",
    "107": "TELUGU",
    "108": "SINDHI",
    "109": "MARATHI",
    "110": "GUJARATI",
    "111": "MANIPURI",
    "112": "MALAYALAM",
    "113": "ODIA",
    "114": "ASSAMESE",
    "115": "KANNADA",
    "116": "ARABIC",
    "117": "TIBETAN",
    "118": "FRENCH",
    "120": "GERMAN",
    "121": "RUSSIAN",
    "123": "PERSIAN",
    "124": "NEPALI",
    "125": "LIMBOO",
    "126": "LEPCHA",
    "189": "TELUGU - TELANGANA",
    "193": "TANGKHUL",
    "194": "JAPANESE",
    "195": "BHUTIA",
    "196": "SPANISH",
    "198": "MIZO",
    "205": "BENGALI W/O PR.",
    "241":"APPLIED MATHEMATICS",
    "301": "ENGLISH CORE",
    "302": "HINDI CORE",
    "303": "URDU CORE",
    "322": "SANSKRIT CORE",
    "604": "OFFCE PROC.& PRAC.",
    "605": "SECY.PRAC & ACCNTG",
    "606": "OFF. COMMUNICATION",
    "607": "TYPOGRAPHY &CA ENG",
    "608": "SHORTHAND ENGLISH",
    "609": "TYPOGRAPHY &CA HIN",
    "610": "SHORTHAND HINDI",
    "622": "ENGINEERING SCI.",
    "625": "APPLIED PHYSICS",
    "626": "MECH. ENGINEERING",
    "627": "AUTO ENGG. - II",
    "628": "AUTOSHOP RPR&PR-II",
    "632": "AC & REFRGTN-III",
    "633": "AC & REFRGTN-IV",
    "657": "BIO-OPTHALMIC - II",
    "658": "OPTICS-II",
    "659": "OPHTHALMIC TECH.",
    "660": "LAB MEDCN-II (MLT)",
    "661": "CLNCL BIOCHEM(MLT)",
    "662": "MICROBIOLOGY (MLT)",
    "666": "RADIATION PHYSICS",
    "667": "RADIOGRAPHY-I (GN)",
    "668": "RADIOGRAPHY-II(SP)",
    "728": "HLT ED,C & PR & PH",
    "729": "B CONCEPT OF HD&MT",
    "730": "FA & EMER MED CARE",
    "731": "CHILD HLTH NURSING",
    "732": "MIDWIFERY",
    "733": "HEALTH CENTRE MGMT",
    "734": "FOOD PROD-III",
    "735": "FOOD PRODUCTION-IV",
    "736": "FOOD SERVICES-II",
    "737": "FOOD BEV CST & CTR",
    "738": "EVOL&FORM OF MM-II",
    "739": "CR&CM PR IN MM-II",
    "740": "GEOSPATIAL TECH",
    "741": "LAB MEDICINE - II",
    "742": "CL BIOCHEM & MB-II",
    "743": "RETAIL OPER - II",
    "744": "RETAIL SERVICES-II",
    "745": "BEAUTY & HAIR - II",
    "746": "HOLISTIC HEALTH-II",
    "747": "LIB SYS & RES MGMT",
    "748": "INFO STORAGE & RET",
    "749": "INTGRTD TRANS OPRN",
    "750": "LOG OP & SCMGMT-II",
    "751": "BAKERY - II",
    "752": "CONFECTIONERY",
    "753": "FRONT OFFICE OPRNS",
    "754": "ADV FRONT OFF OPRN",
    "756": "INTRO TO HOSP MGMT",
    "757": "TR AGN & TOUR OP B",
    "762": "B HORTICULTURE -II",
    "763": "OLERICULTURE - II",
    "765": "FLORICULTURE",
    "766": "BUS.OP & ADMN - II",
    "774": "FABRIC STUDY",
    "775": "BASIC PATTERN DEV.",
    "776": "GARMENT CONST.-II",
    "777": "TRAD IND TEXTILE",
    "778": "PRINTED TEXTILE",
    "779": "TEXTILE CHEM PROC",
    "780": "FIN ACCOUNT - II",
    "781": "COST ACCOUNTING",
    "782": "TAXATION - II",
    "783": "MARKETING-II",
    "784": "SALESMANSHIP-II",
    "785": "BANKING-II",
    "786": "INSURANCE-II",
    "787": "ELECTRICAL MACHINE",
    "788": "ELECTRICAL APPLIAN",
    "789": "OP & MNT OF COM DV",
    "790": "TR SHOOTING & MEE",
    "793": "CAPITAL MKT OPERNS",
    "794": "DERIVATIVE MKT OPR",
    "795": "DATABASE MGMT APP",
    "796": "WEB APPLICATION-II"
}

subjects_x = {
    "002": "HINDI COURSE-A",
    "003": "URDU COURSE-A",
    "004": "PUNJABI",
    "005": "BENGALI",
    "006": "TAMIL",
    "007": "TELUGU",
    "008": "SINDHI",
    "009": "MARATHI",
    "010": "GUJARATI",
    "011": "MANIPURI",
    "012": "MALAYALAM",
    "013": "ODIA",
    "014": "ASSAMESE",
    "015": "KANNADA",
    "016": "ARABIC",
    "017": "TIBETAN",
    "018": "FRENCH",
    "020": "GERMAN",
    "021": "RUSSIAN",
    "023": "PERSIAN",
    "024": "NEPALI",
    "025": "LIMBOO",
    "026": "LEPCHA",
    "031": "CARNATIC MUSIC VOC",
    "032": "CAR. MUSIC MEL INS",
    "034": "HIND.MUSIC VOCAL",
    "035": "HIND.MUSIC MEL.INS",
    "036": "HIND MUSIC.PER.INS",
    "041": "STANDARD MATHEMATICS",
    "049": "PAINTING",
    "064": "HOME SCIENCE",
    "076": "NATIONAL CADET COR",
    "085": "HINDI COURSE-B",
    "086": "SCIENCE-THEORY",
    "087": "SOCIAL SCIENCE",
    "089": "TELUGU - TELANGANA",
    "090": "SCIENCE WITHOUT PR",
    "092": "BODO",
    "093": "TANGKHUL",
    "094": "JAPANESE",
    "095": "BHUTIA",
    "096": "SPANISH",
    "098": "MIZO",
    "099": "BAHASA MELAYU",
    "101": "ENGLISH COMM.",
    "122": "COMM. SANSKRIT",
    "131": "RAI",
    "132": "GURUNG",
    "133": "TAMANG",
    "134": "SHERPA",
    "154": "ELEM. OF BUSINESS",
    "165": "FOUNDATION OF I T",
    "166": "INFO. & COMM. TECH",
    "184": "ENGLISH LNG & LIT.",
    "241":"BASIC MATHEMATICS",
    "254": "ELEM BOOK-K & ACCY",
    "303": "URDU COURSE-B",
    "354": "e-PUBLISHING -ENG",
    "401": "DYNAMICS OF RET(O)",
    "402": "INFO TECHNOLOGY(O)",
    "403": "SECURITY(O)",
    "404": "AUTOMOBILE TECH(O)",
    "405": "INTR TO FMG (O)",
    "406": "INTR TO TOURISM(O)",
    "407": "BEAUTY & WELLN(O)",
    "417": "ARTIFICIAL INTELLIGENCE",
    "454": "e-PUBLISHING -HIN",
    "461": "DYNAMICS OF RET(C)",
    "462": "INFO TECHNOLOGY(C)",
    "463": "SECURITY(C)",
    "464": "AUTOMOBILE TECH(C)",
    "465": "INTR TO FMG (C)",
    "466": "INTR TO TOURISM(C)",
    "467": "BEAUTY & WELLN(C)"
}
submarks={}
for codeindex in range(len(code)):
	templist=[]
	for marks in finalline:
		templist.append(marks[3::][codeindex])
	submarks[code[codeindex]]=templist
filtered_submarks={}
for c in code:
	line=submarks[c]
	while None in line:
		line.remove(None)
	filtered_submarks[c]=list(map(int,line))

cvf=open('student_wise_analysis.csv','w')
writer=csv.writer(cvf)
head=['ROLL NO.','GENDER','NAME']
if '301' in code:
	classname=12
	for i in code:
		head.append(subjects[i])
if '184' in code:
	classname=10
	for i in code:
		head.append(subjects_x[i])
head.append('PERCENTAGE')
writer.writerow(head)
for row in finalline:
	writer.writerow(row)
cvf.close()

cvf2=open('subject_wise_analysis.csv','w')
writer=csv.writer(cvf2)
glist=['A1','A2','B1',"B2","C1","C2","D1","D2","E"]
head=['CODE','SUBJECT','NO. OF STUDENTS','APPREARED','ABSENT','PASS','FAIL','PASS PERCENT','P.I.']+glist+[ 'HIGHEST SCORE', 'LOWEST SCORE', 'AVERAGE SCORE', 'TOPPER\'s NAME' ]
writer.writerow(head)
if '301' in code:
	sub=subjects
elif '184' in code:
	sub=subjects_x
for i in code:
	no_of_students=0
	for c in subcode:
		if i in c:
			no_of_students+=1
	fail=0
	for grade in D[i]:
		if grade=='E':
			fail+=1
	data=[i, sub[i], no_of_students,sum(count(D,i).values()),0-sum(count(D,i).values())+no_of_students, (sum(count(D,i).values())-fail),fail,((sum(count(D,i).values())-fail)*100)/sum(count(D,i).values()), subPI(D,i)]+list(count(D,i).values())+[max(filtered_submarks[i]),min(filtered_submarks[i]), sum(filtered_submarks[i])/len(filtered_submarks[i]), finalline[filtered_submarks[i].index(max(filtered_submarks[i]))][2]]
	writer.writerow(data)
cvf2.close()

streamlist=[]
remark=[]
for i in range(len(stusubs(rawlines))) :
	if '042' in stusubs(rawlines)[rawlines[i][0]]:
		streamlist.append('SCIENCE')
		remark.append(rawlines[i][-1])
	elif '054' in stusubs(rawlines)[rawlines[i][0]]:
		streamlist.append('COMMERCE')
		remark.append(rawlines[i][-1])
	elif '029' in stusubs(rawlines)[rawlines[i][0]]:
		streamlist.append('HUMANITIES')
		remark.append(rawlines[i][-1])
if classname==12:
	cvf3=open('stream_wise_analysis.csv','w')
	writer=csv.writer(cvf3)
	writer.writerow(['STREAM', 'TOTAL STUDENTS', 'TOTAL APPEARED', 'PASS', 'ABSENT', 'COMPARTMENT', 'ESSENTIAL REPEAT', 'PASS PERCENT', 'P.I.', 'HIGHEST MARKS', 'AVERAGE MARKS', 'STREAM TOPPER'])
	for stream in ['SCIENCE', 'COMMERCE', 'HUMANITIES']:
		passcount=0
		comp=0
		abs=0
		repeat=0
		sw_rawlines=[]
		sw_rawmarks=[]
		sw_finalline=[]
		for i in range(len(streamlist)):
			if streamlist[i]==stream:
				sw_rawlines.append(rawlines[i])
				sw_rawmarks.append(rawmark[i])
				sw_finalline.append(finalline[i])
				if remark[i]=='PASS':
					passcount+=1
				elif remark[i]=='COMP':
					comp+=1
				elif remark[i]=='ABST':
					abs+=1
				elif remark[i]=='REPEAT':
					repeat+=1
		sw_D=subgradecount(sw_rawlines, sw_rawmarks)
		sw_PI=studentPI_list(sw_rawmarks)
		percentlist=[]
		for line in sw_finalline:
			percentlist.append(line[-1])
		writer.writerow([stream, len(sw_finalline), len(sw_finalline)-abs, passcount, abs, comp, repeat, (passcount*100)/len(sw_finalline), sw_PI, max(percentlist), sum(percentlist)/len(percentlist), sw_finalline[percentlist.index(max(percentlist))][2]])
	cvf3.close()

cvf4=open('overall_analysis.csv','w')
writer=csv.writer(cvf4)
passcount,comp,abs,repeat=0,0,0,0
percentl=[]
for i in finalline:
	percentl.append(i[-1])
for i in remark:
	if i=='PASS':
		passcount+=1
	elif i=='COMP':
		comp+=1
	elif i=='ABST':
		abs+=1
	elif i=='REPEAT':
		repeat+=1
writer.writerow(['NO. OF STUDENTS', len(finalline)])
writer.writerow(['APPEARED', len(finalline)-abs])
writer.writerow(['PASSED', passcount])
writer.writerow(['COMPARTMENT',comp])
writer.writerow(['REQUIRED REPEAT', repeat])
writer.writerow(['ABSENT', abs])
writer.writerow(['SCHOOL P.I.', studentPI_list(rawmark)])
writer.writerow(['HIGHEST PERCENTAGE',max(percentl)])
writer.writerow(['AVERAGE MARKS', sum(percentl)/len(percentl)])
writer.writerow(['FIRST TOPPER', finalline[percentl.index(max(percentl))][2]])
finalline.remove(finalline[percentl.index(max(percentl))])
percentl.remove(percentl[percentl.index(max(percentl))])
writer.writerow(['SECOND TOPPER', finalline[percentl.index(max(percentl))][2]])
finalline.remove(finalline[percentl.index(max(percentl))])
percentl.remove(percentl[percentl.index(max(percentl))])
writer.writerow(['THIRD TOPPER', finalline[percentl.index(max(percentl))][2]])
finalline.remove(finalline[percentl.index(max(percentl))])
percentl.remove(percentl[percentl.index(max(percentl))])
cvf4.close()
print("Result successfully analysed")
print("Four csv files:\n 1. student_wise_analysis.csv \n 2. subject_wise_analysis.csv \n 3. steam_wise_abalysis.csv \n 4. overall_analysis.csv \n has been created at the folder where this program was ran.")
