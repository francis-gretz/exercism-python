def to_rna(dna_strand):
    tab = str.maketrans("CGTA", "GCAU")

    return dna_strand.translate(tab)
