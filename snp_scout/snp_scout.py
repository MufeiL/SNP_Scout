import argparse

def reference_matching(matches): #check if matches are the same as reference base
  for char in matches:
    if char not in (',', '.'):
      return False
  return True

#function to perform variant calling
def snp_scout(m_file):
  with open(m_file, "r") as f:
    for line in f:
      columns = line.strip().split('\t') #split line into columns
      chromosome = columns[0]
      position = columns[1]
      reference_base = columns[2]
      #coverage = columns[3]
      matches = columns[4]
      #states = columns[5]
      if matches == True:
        continue
      else:
        pass

#function to parse user-given arguments
def main():
  parser = argparse.ArgumentParser(prog = "SNP Scout", description = "Command-line script to perform variant calling")

  #Add required inputs
  parser.add_argument("mpileup", help = "SAMtools mpileup file", type = str)

  args = parser.parse_args()
  pileup_file = args.mpileup #obtain name of pileup file
