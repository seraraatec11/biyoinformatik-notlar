from Bio.Seq import Seq

dna=Seq("ATGCTTACGGATCTAGCTA")

print("DNA dizisi:", dna)
print("Uzunluk:", len(dna))
print("tamamlayıcı:", dna.complement())
print("ters tamamlayıcı:", dna.reverse_complement())
print("rna'ya çevir:", dna.transcribe())
print("proteine çevir:", dna.translate())
