#Tharaka Jayalath
#Assignment
#Oct 17, 2017
#Genomes of (1)Agrobacterium_rhizogenes, (2)Lactobacillus_siliginis and (3)Lactobacillus_similis

#subroutines

def gccontent(seq):
	return((seq.count('G')+ seq.count('C'))/len(seq))

def startcodon(seq):
	return(seq[0:3])
	
def stopcodon (seq):
	return(seq[-3:])
	
def avggc(seq):
	avg=0
	for line in seq:
		avg+=gccontent
	avg=avg/len(seq)
	return avg




	

count=0	
gene=0
seq=''
idline=''
set=0
#Please replace your infile name below
inf=open('seq.txt', 'r')

outfile=open('seq_out.txt','w')

for line in inf:
	line=line.strip()
	if line[0]=='>':
		oldid=idline
		idline=line[0:19]
		
		if set==1:
			mygccontent=gccontent(seq)
			mystartcodon=startcodon(seq)
			mystopcodon=stopcodon(seq)
			count+=1
			gene+=len(seq)
			print(oldid, len(seq), mygccontent, startcodon, stopcodon,'\n')
			outfile.write(oldid+','+mystartcodon+','+mystopcodon+','+str(len(seq))+','+str(mygccontent)+'\n')
			
			
		seq=''
	else:
		seq+=line
		set=1	
inf.close()


#Last sequence

if set==1:
	mygccontent=gccontent(seq)
	mystartcodon=startcodon(seq)
	mystopcodon=stopcodon(seq)
	myavggc=avggc(seq)
	count+=1
	gene+=len(seq)
	print(oldid, len(seq), mygccontent, startcodon, stopcodon,'\n')
	outfile.write(oldid+','+mystartcodon+','+mystopcodon+','+str(len(seq))+','+str(mygccontent)+'\n')

print('The total number of genes is:',str(count))
print("Average GC content of the sequences is", avggc)

outfile.close()

#Making the dictionaries
inf2=open('seq_out.txt', 'r')
outfile2_gc=open('seq_gclist.txt','w')

start=[]
start_co={}
stop=[]
stop_co={}
gc=[]
gc_co={}

for line in inf2:
	line=line.strip()
	fields=line.split(',')
	
	start.append(fields[1])
	stop.append(fields[2])
	gc.append(fields[4])
	

	
print('\n'+'The distribution of start codon'+'\n')
for item in start:
	if item in start_co.keys():
		start_co[item]+=1
	else:
		start_co[item]=1
for k, v in start_co.items():
	print ('Codon', k, ' appears ', v, ' times.')	
	
print('\n'+'The distribution of stop codon'+'\n')
	
for item in stop:
	if item in stop_co.keys():
		stop_co[item]+=1
	else:
		stop_co[item]=1
for k, v in stop_co.items():

	print ('Codon', k, ' appears ', v, ' times.')	
	
#GC content file
for index in range(0,len(gc)):	
	outfile2_gc.write(gc[index]+'\n')


outfile2_gc.close()