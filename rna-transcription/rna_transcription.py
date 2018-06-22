def to_rna(dna_strand):

    listStrand = list(dna_strand)
    newDna = ''

    for letter in listStrand:
        if letter == 'G':
            newDna += 'C'
        elif letter == 'C':
            newDna += 'G'
        elif letter == 'T':
            newDna += 'A'
        elif letter == 'A':
            newDna += 'U'
        else:
            raise ValueError("This contains the wrong letter!")


    return newDna
