import sys
# ABOUT: input fasta and output a fastq formated file with systematic mutations in the reads to assess mapping behavior of PhIPseq reads.

# python make_fastq.py oligos-ref_host_virus_acc_gene_AA_dups_v3.fasta 


read_len = 100
step_size = 100

D={}
for line in open(sys.argv[1]):
        i=line.strip().split()
        if line[0]==">":
                c=i[0].strip(">")
                D[c]=[]
                continue
        D[c] = line.strip()


contig_list = {}
for pep in D:
    seq = D[pep]
    for base in range(len(seq)):
        bases = ["A", "T", "C", "G"]
        #print(seq)
        #print(base)
        #print(seq[base])
        bases.remove(seq[base])  
        seq = list(seq)
        fake_mutation = bases[0] 
        
        name = "".join([">",pep,"_","pos:",str(base+1),",","_".join([seq[base],fake_mutation])])
        print(name)
        
        seq[base] = fake_mutation
        print("".join(seq))
        
        print("+")
        fake_quality = "J" * int(len(seq))
        print(fake_quality)   # This is simplistic
        #break
    #seq_list = [seq[i:i+read_len] for i in xrange(0, len(seq), step_size)] # len(seq) allows for the last read to be less than 100bp
    #count=0
    #for fragment in seq_list:
    #    count+=1
    #    print(name)
    #    print(fragment)
    #    print "+"
