import sys
# ABOUT: input fasta and output a fastq formated file with systematic mutations in the reads to assess mapping behavior of PhIPseq reads.

# python make_fastq.py oligos-ref_host_virus_acc_gene_AA_dups_v3.fasta 


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
        name = "".join([">",pep,"|","pos:NA","|","-".join(["NA","NA"])])
    print(name)
    print(seq)
    print("+")
    fake_quality = "J" * int(len(seq))
    print(fake_quality)   # We may want to be more sophisticated with this later.
    for base in range(len(seq)):
        bases = ["A", "T", "C", "G"]
        bases.remove(seq[base])  
        seq = list(seq)
        fake_mutation = bases[0] 
        
        name = "".join([">",pep,"|","pos:",str(base+1),"|","-".join([seq[base],fake_mutation])])
        print(name)
        
        seq[base] = fake_mutation
        print("".join(seq))
        
        print("+")
        fake_quality = "J" * int(len(seq))  
        print(fake_quality)   # This is simplistic, but fastq requires quality scores so I just add J.
