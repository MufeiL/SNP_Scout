## Preprocessing Workflow

**[Data Source](https://www.internationalgenome.org/data-portal/data-collection/30x-grch38)** 

### SAMtools
Most steps of our preprocessing use SAMtools. Instructions for installing SAMtools can be found [here](http://www.htslib.org/download/) on the SAMtools website.

### Input CRAM/BAM files:
We used alignments from three samples (out of 3202 available samples) in the format of CRAM files from the 1000 Genomes 30x on GRCh38 project. 
Link to each sample CRAM file: 
* [NA12778](https://ftp.sra.ebi.ac.uk/vol1/run/ERR323/ERR3239484/NA12778.final.cram)
* [NA12889](https://ftp.sra.ebi.ac.uk/vol1/run/ERR323/ERR3239489/NA12889.final.cram)
* [NA18544](https://ftp.sra.ebi.ac.uk/vol1/run/ERR323/ERR3239496/NA18544.final.cram)

These files are pretty large on their own, so we chose to extract a region of chromosome 17 (68765882-69416314) that we know has a decent amount of exons and therefore a higher change of getting more reads in our smaller cram files.

Below is our example terminal command for downloading the region of chromosome 17 for the NA12778 sample cram file:

```samtools view -h https://ftp.sra.ebi.ac.uk/vol1/run/ERR323/ERR3239484/NA12778.final.cram chr17:68765882-69416314 > NA12778_chr17.cram```

### Converting CRAM files to BAM files using samtools
Below we use samtools 

