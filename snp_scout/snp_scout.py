import argparse

#function to perform variant calling
def snp_scout(m_file, var_freq, min_cov, min_reads2, min_homo, out_file = None):
    output_handle = None
    if out_file:
        output_handle = open(out_file, "w")
        header = "\t".join(["#CHROM", "POS", "ID", "REF", "ALT", "FILTER", "INFO", "FORMAT", "SAMPLE1"]) + "\n"
        output_handle.write(header)
    else:
        print("\t".join(["#CHROM", "POS", "ID", "REF", "ALT", "FILTER", "INFO", "FORMAT", "SAMPLE1"]))
    
    nucs = ['A', 'T', 'C', 'G'] #nucleotide bases
    
    with open(m_file, "r") as f:
        for line in f:
            if "#" not in line: #skip header lines
                columns = line.strip().split('\t') #split line into columns
                chromosome = columns[0] #name of chrom
                position = columns[1] #position on chrom
                reference_base = columns[2].upper() #reference base
                coverage = int(columns[3]) #read depth
                reads = columns[4] #actual reads

                # Get alternate alleles
                alt_alleles = set(base.upper() for base in reads if base.upper() != reference_base.upper() and base.upper() in nucs)
                het = 0 #labels for what type of sample/gt we have
                homo = 0
                wt = 0
                filt = "fail" #filter
                # Calculate variant frequency
                tot_var = sum(1 for base in reads if base.upper() != reference_base.upper() and base.upper() in nucs) #total variants per line
                freq = tot_var / max(1, coverage) #variant frequency
                if freq >= var_freq and coverage >= min_cov and tot_var >= min_reads2: #to consider for variant calling
                    filt = "PASS"
                    alt_allele_str = ','.join(alt_alleles) if alt_alleles else "N/A" #get alt allele(s)
                    
                    if alt_allele_str == reference_base: #get genotype
                        gt = "0/0" #homozygous
                        wt +=1
                    elif alt_allele_str != reference_base and (',' in reads or '.' in reads) and freq < min_homo:
                        gt = "0/1" #heterozygous
                        het +=1
                    else:
                        gt = "1/1" #homozygous for alt
                        homo +=1
                    
                    info_str = f"WT={wt};HET={het};HOM={homo}" #string for info header
                    #WT=0;HET=0;HOM=3
                    if output_handle:
                        output_handle.write(f"{chromosome}\t{position}\t.\t{reference_base}\t{alt_allele_str}\t{filt}\t{info_str}\tGT:SDP:FREQ\t{gt}:{coverage}:{freq*100}%\n")
                    else:
                        print(f"{chromosome}\t{position}\t.\t{reference_base}\t{alt_allele_str}\t{filt}\t{info_str}\tGT:SDP:FREQ\t{gt}:{coverage}:{freq*100}%")
    if output_handle:
        output_handle.close()

#function to parse user-given arguments
def main():
    parser = argparse.ArgumentParser(prog = "SNP Scout", description = "Command-line script to perform variant calling")
    
    #Add inputs
    parser.add_argument("mpileup", help = "SAMtools mpileup file", type = str)
    parser.add_argument("-m", "--min_var_freq", help = "Minimum variant frequency", type = float, default = 0.01)
    parser.add_argument("-c", "--min_coverage", help = "Minimum read depth", type = float, default = 8)
    parser.add_argument("-r", "--min_reads2", help = "Minimum supporting reads for variants", type = int, default = 2)
    parser.add_argument("-f", "--min_freq_for_homo", help = "Minimum frequency for homozygotes", type = float, default = 0.75)
    parser.add_argument("-o", "--out", help = "Write output to file", type = str)
    
    args = parser.parse_args()
    pileup_file = args.mpileup #name of pileup file
    var_freq = args.min_var_freq
    min_cov = args.min_coverage
    min_reads2 = args.min_reads2
    min_homo = args.min_freq_for_homo
    out_file = args.out #name of output file (if included)
    snp_scout(pileup_file, var_freq, min_cov, min_reads2, min_homo, out_file)

if __name__ == "__main__":
    main()
