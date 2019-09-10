# IMB PBS Cluster Computing 

### Table of Conents 
- Important Commands
- Checking for Software
- Using Cluster Software
- Installing Software
- Memory and Walltime
- Interactive Sessions
- Submitting a Job
- Checking Job Status 
- Moving Data On/Off the Cluster

### Important Commands
SSH into the Cluster server using `ssh [username]@delta.imb.uq.edu.au` and entering your password 

`qsub` is the most important command on the cluster - it controls how jobs are run 

`qsub -I` gets you an interactive shell, where you can run small programs 

`qsub -q normal` for normal sized jobs and `qsub -q bigmem` for jobs that need a lot of memory 

to see what software is available, run 	`module avail` 

### Checking to see what software is already installed
`module avail` prints all available software modules to the terminal 

load a module using `module load [module name]`

check your loaded modules using `module list`

see any changes the module will make to your environment with `module display [module name]`

**using the module with PBS** 
as long as the module is loaded on the node(s), it should be useable with `module load [module name]` in the script

**if the module hasn't been configured** but you can see it in the system, use 
`. /share/software/Modules/default/init/bash`
and then `module load` should work 

### Using Cluster Software in PBS Scripts 


### Installing your own software 

if you don't see the software you need in the modules listed, you'll need to install it yourself, in your own `/bin` directory 

download package to local machine (be sure to download the package for a linux system, and _make sure you don't have to be root user to install_)

move the installer package onto the cluster by using 
`scp /location/of/file/filename.txt [username]@delta.imb.uq.edu.au:/location/on/cluster/`
note: you need to be in your local machine when you do this, and you will be asked to input your password 

once installer package is on the cluster, ssh back on, and go through the steps to unpack and install it in your `home/[user]/bin` folder 
if you don't have a `/bin` folder, just create one with `mkdir bin` 

**IMPORTANT** make sure no other copies of this program exist on the cluster (as far as you can tell), particularly in your own files 

### Memory and Walltime 
The cluster has nodes, which are each made up of cpus (central processing units), which have a given amount of memory (in gigabytes) 
To set a different amount of memory than default: 
```
select=[insert number of nodes you'll need]:ncpus=[number of cpus]:mem=[amount of memory]
```
There are 11 nodes on the cluster, with cpus ranging from 16 to 36, and anywhere from 126GB to 1514GB of memory 
_MORE CPUS ON A NODE DOES NOT NECESSARILY MEAN MORE MEMORY_

If your job is going to take a lot of memory, it's also probably going to take a long time! 
When there's sufficient memory to perform the job, more memory will make it faster (citation needed).
The default amount of time is 4 hours. 

To change the amount of time use:
```
-l walltime=hr:min:sec 
```

### Running a Job in the Interactive Session  

Start the session using `qsub -I` for default parameters:
``` 
ncpus = 1
walltime = 4:00:00
mem = 4 gb
```

To change parameters, use `qsub [-l parameters you want changed] -I` 
Depending on what resources you ask for, it could take time for you interactive environment to start. 

Once in the interactive environment, you can run scripts just like you would from the command line, they're just being run on the cluster's resources instead (and not on the head node). 

The max for a single user's jobs on this queue / in this environment are: 
```
mem = 40 gb 
ncpus = 6
walltime = 24:00:00
```
Example: 
```
qsub -l select=2:ncpus=3:mem=10GB -I
```
Here we've submitted for an interactive environment with 2 nodes, 3 ncpus, and 10 GB of memory. 

For more information on time and memory, skip to the **Memory and Walltime** section.  

### Submitting a PBS Job to the Queue 

The cluster uses a pbs queueing system, which requires a `.pbs` script to run your program 

A `.pbs` script can be in any language, but bash is easiest 

It requires a specific heading, which tells the cluster how to run your job, and what language to read it in, but after that, you can use basic commands in whichever language you've chosen 

For example: 
```
#########
### Script: mafft_run.pbs 
#########
#PBS -N 08Aug19_mafft_alignment.fasta
#PBS -q normal
#PBS -A i.warner
#PBS -S /bin/bash
#PBS -r n 
#PBS -l select=1:ncpus=1:mem=35GB
#PBS -l walltime=12:00:00

cd /home/i.warner/bin

mafft --globalpair --maxiterate 1000 /shares/common/users/i.warner/FASTA_sequences/Ecoli_genomes_all.fasta > /shares/common/users/i.warner/output_mafft/Ecoli_genomes_aligned.fasta
```

`#` functions as normal but `#PBS` is a command for the cluster 
`-N` is what the output file will be named, and what the error messages will be called (with different extensions)
`-q` is the same as the `qsub -q` from earlier, which just tells the queue what kind of memory the job will require (for this job, it should have been `-q bigmem`) 
`-A` is the author of the job (that's you!) 
`-S` is the type of script you'll be running; in this case, I'm giving it a bash script, so I want it to read this using the bash program from the root `/bin` folder 
`-r` is reading capabilities; it's almost always `n`
`-l` is how much memory you'll need for your job, and how much time it will take
these are always in separate lines in the PBS script, but on the same line when given on the command line 

Once you have these parameters in place, you can give it commands in the scripting language you specified earlier (it takes python, perl, R, etc. - I just stick with bash)

Here, I changed the directory to _my_ `/bin` directory, where _my_ programs are located, and where I've installed programs as detailed in the **Installing Your Own Software** section. 

From here, I can execute my program (I could also have navigated to the directory where my files are located, to avoid typing out their long addresses). 

My program `mafft` takes the arguments `--globalpair` and `--maxiterate 1000`, and the input file `Ecoli_genomes_all.fasta` in the `/shares/common/users/i.warner/FASTA_sequences/` directory. 
I've also specified that I want my output (indicated by the carrot `>`) to go in the file `Ecoli_genomes_aligned.fasta` in the `/shares/common/users/i.warner/output_mafft/` directory 

Now that I've got my script, I want to submit it to run on the cluster. I can do that using 
``` 
qsub [any arguments different from what I specified in my .pbs file] pbsfilename.pbs 
```

The cluster will then print out a job #, which I can use to track the progress of my job. 

### Checking on Jobs 

Hang on to that job number! You'll need it to check on your job using `tracejob [job #]`

When you do that, it will print any errors, where the job is (whether it's being considered, assigned, modified, or run), and what's been done so far (same things).

If you get errors, it'll put them in the directory where you're running the program (so for me, they end up in my `/home/i.warner/pbs_scripts` directory)

Error messages can help you troubleshoot what's wrong with your .pbs script or your job more broadly - and they can be anything! 
Mine have ranged from telling me my program isn't properly installed to simply running out of memory on the cluster (easy fix, change your memory parameters, either in the script or on command line when you resubmit the job). 

To check on jobs in the queue, you can list all jobs, in all states, using 
```
qstat -1n
```
_note that's a 1 not an L_ 

To list all of a single user's jobs (likely yours unless you're nosey)
```
qstat -u [username] -1n
```

To list all queued jobs 
```
qselect -s Q |xargs qstat -1n
```
_note no space after the pipe_ 

To see all the queues that are active
```
qstat -Q
```

To check resource use during a job or within 5 minutes of the job finishing
```
qstat -f $jobID
```

**To alter jobs**

Use `qalter` (as in q-alter) to alter jobs. 
For example, to change the walltime of a job while it's running:
```
qalter -l walltime=72:00:00 [job ID]
```
_this doesn't seem to be working_ 

**To delete jobs**

Use `qdel [job ID]` to delete jobs, and `qdel -p [job ID]` to kill a job even when the cluster doesn't want to let you. 

You can also force jobs to run, move them to other nodes, put them on and release a hold, suspend and resume them. At this moment, we're just running basic jobs that we want to run as quickly as possible. 

### Moving Data on/off the Cluster
No matter where you're logged in, you'll be using the ```scp``` command 

To move files from your local machine to the cluster
```scp /path/to/local/file.txt login@delta.imb.uq.edu.au:/path/to/remote/directory```
you'll be asked for your password, and you should get a print message that looks like 
```file.txt 			100%  181KB  25.9MB/s  00:00```

To move files from the remote cluster to your local machine 
```scp login@delta.imb.uq.edu.au:/path/to/file.txt /Users/username/path/to/local/directory```
you'll be asked for your password again 
you should get the same type of print message, basically telling you the file has been moved 