import argparse

#function to perform variant calling
def snp_scout(m_file):
  pass

#function to parse user-given arguments
def main()
parser = argparse.ArgumentParser(prog = "SNP Scout", description = "Command-line script to perform variant calling")

#Add required inputs
parser.add_argument("mpileup", help = "SAMtools mpileup file", type = str)

args = parser.parse_args()
pileup_file = args.mpileup #obtain name of pileup file
