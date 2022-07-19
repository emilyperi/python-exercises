def to_rna(dna_strand):
    # create mapping for dna to rna
    rna_map = {'A': 'U', 'G': 'C', 'C': 'G', 'T': 'A'}
    rna_strand = []

    for  char in dna_strand:
        # check if strand is only AGCT
        if char not in rna_map:
            raise ValueError("DNA strand must contain only A, G, C, T characters")
        
        rna_strand.append(rna_map[char])

    return "".join(rna_strand)
