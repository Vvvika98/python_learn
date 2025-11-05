def to_rna(dna_strand):
    #1 неверное 
    # result = ""
    # for nucleotide in dna_strand:
    #     if nucleotide == "G":
    #         result = dna_strand.replace("G","C")
    #     if nucleotide == "C":
    #         result = dna_strand.replace("C", "G")
    #     if nucleotide == "T":
    #         result = dna_strand.replace("T", "A")
    #     if nucleotide == "A":
    #         result = dna_strand.replace("A", "U")
    #     return result


    # 2
    # result = dna_strand.maketrans("GCTA", "CGAU")
    # return dna_strand.translate(result)

    return dna_strand.translate(dna_strand.maketrans("GCTA", "CGAU"))

    # 4
    # rna = ""
    # tranc = { "G" : "C",
    #           "C" : "G",
    #           "T" : "A",
    #           "A" : "U"  }

    # for nucleotide in dna_strand:
    #     rna += tranc[nucleotide]
    # return rna





print((to_rna("ACGTGGTCTTAA")))    #"UGCACCAGAAUU"