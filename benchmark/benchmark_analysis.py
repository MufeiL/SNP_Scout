def read_positions(file_path):
    # Reads the positions from the given file and returns them as a set
    positions = set()
    with open(file_path, 'r') as f:
        for line in f:
            if line.startswith("#"):
                continue
            columns = line.strip().split('\t')
            positions.add(columns[1])
    return positions

# sensitivity 
# if reads in snp_scout and also in varscan, add snp_scout reads into a list then compute the percentage
def sensitivity(path1, path2):
    snp_scout_positions = read_positions(path1)
    varscan_positions = read_positions(path2)

    true_positives = snp_scout_positions.intersection(varscan_positions)
    sensitivity = len(true_positives) / len(snp_scout_positions) if snp_scout_positions else 0
    return sensitivity * 100 
    

# specificity
# if reads in snp_scout that's NOT in varscan, add the negatives into a list and compute the percentage
def specificity(path1, path2):
    snp_scout_positions = read_positions(path1)
    varscan_positions = read_positions(path2)

    true_negatives = snp_scout_positions.difference(varscan_positions)
    specificity = len(true_negatives) / len(snp_scout_positions) if snp_scout_positions else 0
    return specificity * 100 

def main():
    path1 = '/Users/mufeili/Desktop/cse182/snp_scout/test_child_hom_copy.txt'
    path2 = '/Users/mufeili/Desktop/cse182/snp_scout/varscan_out_copy.txt'

    sens = sensitivity(path1, path2)
    spec = specificity(path1, path2)

    print('sensitivity = ' + str(sens) + '%')
    print('specificity = ' + str(spec) + '%')


if __name__ == "__main__":
    main()

