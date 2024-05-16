import argparse

#function to perform variant calling
def snp_scout(m_file, var_freq, min_cov, out_file = None):
    output_handle = None
    if out_file:
        output_handle = open(out_file, "w")
        header = "\t".join(["CHROM", "POS", "REF", "ALT", "FORMAT", "SAMPLE1"]) + "\n"
        output_handle.write(header)
    else:
        print("\t".join(["CHROM", "POS", "REF", "ALT", "FORMAT", "SAMPLE1"]))
    
    with open(m_file, "r") as f:
        for line in f:
            if "#" not in line: #skip header lines
                columns = line.strip().split('\t') #split line into columns
                chromosome = columns[0]
                position = columns[1]
                reference_base = columns[2]
                coverage = int(columns[3])
                reads = columns[4]

                # Count alternate alleles
                alt_alleles = [base.upper() for base in reads if base.upper() not in (',', '.', '!', '$', '^') and base.upper() != reference_base.upper()]

                # Calculate variant frequency
                tot_var = sum(1 for base in reads if base not in (',', '.', '!', '$', '^')) #total variants per line
                freq = tot_var / max(1, coverage)
                if freq >= var_freq and coverage >= min_cov: #to consider for variant calling
                    alt_allele_str = ','.join(alt_alleles) if alt_alleles else "N/A" #get alt allele
                    
                    if alt_allele_str == reference_base: #get genotype (assuming we only have 1 alt base)
                        gt = "0/0"
                    elif alt_allele_str != reference_base and (',' in reads or '.' in reads):
                        gt = "0/1"
                    else:
                        gt = "1/1"

                    if output_handle:
                        output_handle.write(f"{chromosome}\t{position}\t{reference_base}\t{alt_allele_str}\tGT\t{gt}\n")
                    else:
                        print(f"{chromosome}\t{position}\t{reference_base}\t{alt_allele_str}\tGT\t{gt}")
    if output_handle:
        output_handle.close()

#function to parse user-given arguments
def main():
    parser = argparse.ArgumentParser(prog = "SNP Scout", description = "Command-line script to perform variant calling")
    
    #Add inputs
    parser.add_argument("mpileup", help = "SAMtools mpileup file", type = str)
    parser.add_argument("-m", "--min_var_freq", help = "Minimum variant frequency", type = float, default = 0.01)
    parser.add_argument("-c", "--min_coverage", help = "Minimum read depth", type = float, default = 8)
    parser.add_argument("-o", "--out", help = "Write output to file", type = str)
    
    args = parser.parse_args()
    pileup_file = args.mpileup #name of pileup file
    var_freq = args.min_var_freq
    min_cov = args.min_coverage
    out_file = args.out #name of output file (if included)
    snp_scout(pileup_file, var_freq, min_cov, out_file)

main()
