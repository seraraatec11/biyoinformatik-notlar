from Bio import SeqIO

for kayit in SeqIO.parse("ornekler.fasta", "fasta"):
    print("Ad:", kayit.id)
    print("Dizi:", kayit.seq)
    print("Uzunluk:", len(kayit.seq))
    print("---")
