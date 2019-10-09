# parSNP Methods 

## Author: Isabel Warner
## Date: 09Oct2019

## Questions
 - is it possible to change the output file names, or do I have to write a separate script to batch edit them? 

## Error Messages 
_Sometime in September_ : 

```
For detailed documentation please see --> http://harvest.readthedocs.org/en/latest
-->Reading Genome (asm, fasta) files from /shares/common/users/i.warner/FASTA_sequences/..
  |->[OK]
-->Reading Genbank file(s) for reference (.gbk) /shares/common/users/i.warner/ref_genomes/BW25113-CP009273.1.gb..
  |->[OK]
-->Calculating MUMi..
  |->[SKIP]
**ERROR**
The following command failed:
>>/scratch/tmp/pbs.2235702.delta/_MEIjKtZSe/harvest -q -o /shares/common/users/i.warner/parsnp_output/parsnp.ggr -x /shares/common/users/i.warner/parsnp_output/parsnp.xmfa -g /shares/common/users/i.warner/ref_genomes/BW25113-CP009273.1.gb 
Please veryify input data and restart Parsnp. If the problem persists please contact the Parsnp development team.
**ERROR**

########################### Job Execution History #############################
JobId: 2235702.delta
UserName: i.warner
GroupName: Group-Henderson
JobName: 19Sept2019_parsnp.fasta
SessionId: 127010
ResourcesRequested: mem=250gb,ncpus=2,nice=0,place=free,walltime=75:00:00
ResourcesUsed: cpupercent=160,cput=00:01:32,mem=923492kb,ncpus=2,vmem=1239536kb,walltime=00:01:23
QueueUsed: normal
Account: i.warner
ExitStatus: 245
###############################################################################
Efficiencies

Walltime Efficiency:   0.0307 %
CPU time Efficiency:  55.4217 %
mem Efficiency:       0.3523 %
#####################################
```
Can't seem to find error message replicated anywhere online. Even parSNP forum doesn't have anything similar. 

## Runs on October 9th, 2019
Started by updating script to: 
```
#########
### Script: Parsnp_run.pbs 
#########
#PBS -N 09Oct2019_parsnp.fasta
#PBS -q normal
#PBS -A i.warner
#PBS -S /bin/bash
#PBS -r n 
#PBS -l select=2:ncpus=4:mem=250GB
#PBS -l walltime=100:00:00

cd /home/i.warner/bin/Parsnp-Linux64-v1.2/

./parsnp -g /shares/common/users/i.warner/ref_genomes/BW25113-CP009273.1.gb -d /shares/common/users/i.warner/FASTA_sequences/ -p 2 -o /shares/common/users/i.warner/parsnp_output
``` 

Verified correct genomes in FASTA_sequences and ref_genomes directories. Ran using qsub, got the following error: 
```
For detailed documentation please see --> http://harvest.readthedocs.org/en/latest
-->Reading Genome (asm, fasta) files from /shares/common/users/i.warner/FASTA_sequences/..
  |->[OK]
-->Reading Genbank file(s) for reference (.gbk) /shares/common/users/i.warner/ref_genomes/BW25113-CP009273.1.gb..
  |->[OK]
-->Calculating MUMi..
  |->[SKIP]
**ERROR**
The following command failed:
>>/scratch/tmp/pbs.2422078.delta/_MEIA9yKQi/harvest -q -o /shares/common/users/i.warner/parsnp_output/parsnp.ggr -x /shares/common/users/i.warner/parsnp_output/parsnp.xmfa -g /shares/common/users/i.warner/ref_genomes/BW25113-CP009273.1.gb 
Please veryify input data and restart Parsnp. If the problem persists please contact the Parsnp development team.
**ERROR**


########################### Job Execution History #############################
JobId: 2422078.delta
UserName: i.warner
GroupName: Group-Henderson
JobName: 09Oct2019_parsnp.fasta
SessionId: 10329
ResourcesRequested: mem=500gb,ncpus=8,nice=0,place=free,walltime=100:00:00
ResourcesUsed: cpupercent=102,cput=00:01:23,mem=894416kb,ncpus=8,vmem=1206932kb,walltime=00:01:14
QueueUsed: normal
Account: i.warner
ExitStatus: 245
###############################################################################
Efficiencies

Walltime Efficiency:   0.0206 %
CPU time Efficiency:  14.0203 %
mem Efficiency:       0.1706 %
#####################################
```

Still having the same issue with MUMi. 
