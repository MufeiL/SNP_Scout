# Benchmarking Commands
The below steps will demonstrate how to install `VarScan`, run the program on the child mpileup file from Lab 1, and store the results.

To download `VarScan`:
```
curl -L https://sourceforge.net/projects/varscan/files/VarScan.v2.3.9.jar/download > VarScan.jar
```
To bring up the help message after installation:
```
java -jar VarScan.jar
java -jar VarScan.jar mpileup2snp -h
```
Run VarScan on the child mpileup (to turn off the default: set p value to 1, quality score to 0, strand filter to 0):
```
java -jar VarScan.jar mpileup2snp NA12878_child.mpileup --p-value 1 --min-avg-qual 0 --strand-filter 0 --min-var-frequency 0.2 --min-freq-for-hom 0.8 --min_coverage 8 --min_reads2 2 --output-vcf 1 --variants > bench_child_hom.vcf
```
We also want to run `SNP Scout` with the same parameters to match `VarScan`:
```
-m --min_var_freq 0.2
-f --min_freq_for_homo 0.8
-c --min_coverage 8
-r --min_reads2 2
```
The actual command is given by the below command. Note that you may have to change the file paths if running on a personal device.
```
snp_scout -m 0.2 -f 0.8 -c 8 -r 2 -o test_child_hom.txt NA12878_child.mpileup
```
