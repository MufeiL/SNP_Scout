import argparse

#function to perform variant calling
def snp_scout(m_file, var_freq, min_cov, out_file = None):
    output_handle = None
    if out_file:
        output_handle = open(out_file, "w")
        header = "\t".join(["Chr", "Pos", "Ref", "Alt"]) + "\n"
        output_handle.write(header)
    else:
       print("Chr" + "\t" + "Pos" + "\t" + "Ref" + "\t" + "Alt")
    
    with open(m_file, "r") as f:
        for line in f:
            #print("line: ", line)
            if "#" not in line:
                columns = line.strip().split('\t') #split line into columns
                chromosome = columns[0]
                position = columns[1]
                reference_base = columns[2]
                coverage = int(columns[3])
                reads = columns[4]

                # Count alternate alleles
                alt_alleles = [base for base in reads if base not in (',', '.', '!', '$', '^') and base != reference_base]
                # Calculate variant frequency
                tot_var = sum(1 for base in reads if base not in (',', '.', '!', '$', '^')) #total variants per line
                freq = tot_var / max(1, coverage)
                if freq >= var_freq and coverage >= min_cov:
                    alt_allele_str = ','.join(alt_alleles) if alt_alleles else "N/A"
                    if output_handle:
                        output_handle.write(f"{chromosome}\t{position}\t{reference_base}\t{alt_allele_str}\n")
                    else:
                        print(f"{chromosome}\t{position}\t{reference_base}\t{alt_allele_str}")
    if output_handle:
        output_handle.close()

#function to parse user-given arguments
def main():
    parser = argparse.ArgumentParser(prog = "SNP Scout", description = "Command-line script to perform variant calling")
    #Add required inputs
    parser.add_argument("mpileup", help = "SAMtools mpileup file", type = str)
    parser.add_argument("--min_var_freq", help = "Minimum variant frequency", type = float, default = 0.2)
    parser.add_argument("--min_coverage", help = "Minimum read depth", type = float, default = 0.8)
    parser.add_argument("-o", "--out", help = "Write output to file", type = str)
    
    args = parser.parse_args()
    pileup_file = args.mpileup #name of pileup file
    var_freq = args.min_var_freq
    min_cov = args.min_coverage
    out_file = args.out #name of output file (if included)
    snp_scout(pileup_file, var_freq, min_cov, out_file)

main()
