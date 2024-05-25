
![Static Badge](https://img.shields.io/badge/language-python-780000) ![Static Badge](https://img.shields.io/badge/language-JupyterNotebook-FDF0D5) ![Static Badge](https://img.shields.io/badge/license-UCSD-C1121F) ![Static Badge](https://img.shields.io/badge/tools-VarScan-669BBC) 

# SNP Scout

This is a demonstration project for CSE 185. `SNP Scout` implements a simpler version of the SNP caller available through VarScan. See the [VarScan](https://varscan.sourceforge.net/using-varscan.html) page for more details.  
# Install Instructions
No additional libraries are required for installation. 
To install `SNP Scout`, access the directory where you want to install the tool and use the following command:
```
git clone https://github.com/MufeiL/SNP_Scout 
```
Then, change into the `SNP_Scout` directory and install the tool. You can use the following commands:
```
cd SNP_Scout
```
```
pip install .
```
If your installation was successful, typing ``snp_scout --help`` should print a helpful message. Otherwise, you may need to specify the path for the package. You can do this with the following command:
```
export PATH=$PATH:/home/$USER/.local/bin
```
Note that if you close the terminal and re-open it at a later time, you may need to re-export the path with the above command in order to run the tool.
# Basic Usage
The basic usage of `SNP Scout` is given by the following:
```
snp_scout [-m min freq] [-c min coverage] [-r min reads2] [-f min homo freq] [-o output file] mpileup file
```
To run `SNP Scout` on a small test dataset, use the following command in the `SNP_Scout` directory:
```
snp_scout example-files/test_short_mpileup.txt -c 1 -r 1
```
This should produce the following output:
```
#CHROM	POS	ID	REF	ALT	FILTER	INFO	FORMAT	SAMPLE1
chrTEST	10	.	C	G	PASS	WT=0;HET=1;HOM=0	GT:SDP:FREQ	0/1:2:50.0%
chrTEST	13	.	A	T	PASS	WT=0;HET=0;HOM=1	GT:SDP:FREQ	1/1:1:100.0%
```
Note that if you are in another directory, you will need to change the path for the above mpileup file in order to run the example test.
# SNP Scout Options
The only required input to `SNP Scout` is a SAMtools pileup file. Users can specify additional options below:
* `-m`, `--min_var_freq`: minimum variant allele frequency threshold. By default, 0.01 is used.
* `-c`, `--min_coverage`: minimum read depth at a position to make a call for variants. By default, 8 is used.
* `-r`, `--min_reads2`: minimum supporting reads at a position to call variants. By default, 2 is used.
* `-f`, `--min_freq_for_homo`: minimum frequency to call homozygote. By default, 0.75 is used.
* `-o`, `--out`: write output to the specified file. Otherwise, output is written to the terminal.   
# File Format 
The output file format is the same as the VarScan variant calling method. See the [VarScan](https://varscan.sourceforge.net/using-varscan.html) page for more details.
# Contributors 
This repository was generated by Sally Ha, Mufei Li, and Margaret Jones with inspiration from the [CSE185 Project Demo](https://github.com/gymreklab/cse185-demo-project/tree/main). For suggestions or corrections, please submit a pull request!
