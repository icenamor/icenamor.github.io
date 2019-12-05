---
title: "TemPorAl (IPC-2018)"
excerpt: "Temporal Portfolio Algorithm<br/>"
collection: portfolio
---

First Temporal Planning Portfolio submitted to the satisficing temporal track of the International Planning Competition 2018. 
This portfolio performs a static equal time assignment of the available time to each of
the portfolio components, which where empirically selected
from the state-of-the art temporal planners.

Selected Planners 
<!--- img src='https://ai2-s2-public.s3.amazonaws.com/figures/2017-08-08/1c09279a3d5659785890042fe906dcfeccff1c20/20-Figure3-1.png'--->

•   ITSAT

•   yahsp2/yahsp2-mt

•   TFD

•   yahsp3/yahsp3-mt

--------------------

International Planning Competition [IPC-2018](https://ipc2018-temporal.bitbucket.io/)

## How do I install Singularity on my machine?
> You can install Singularity locally with the following commands (See the Singularity quick start guide for more details):

                                                
>> 
``` sudo apt install automake
git clone https://github.com/singularityware/singularity.git
cd singularity
git checkout 2.4
./autogen.sh
./configure --prefix=/usr/local
make
sudo make install                         
```

## How can I test my containers?

``` 
   git clone https://bitbucket.org/ipc2018-temporal/team3.git -r ipc-2018-temp-sat
   sudo singularity build planner.img demo-submission/Singularity
   mkdir rundir
   cp path/to/domain.pddl rundir
   cp path/to/problem.pddl rundir
   RUNDIR="$(pwd)/rundir"
   DOMAIN="$RUNDIR/domain.pddl"
   PROBLEM="$RUNDIR/problem.pddl"
   PLANFILE="$RUNDIR/sas_plan"
   singularity run -C -H $RUNDIR planner.img $DOMAIN $PROBLEM $PLANFILE                        
```

Singularity configuration:
--

 The Singularity file should be change if you like to create the container:
 
Bootstrap: docker
``` 
From: ubuntu:16.04
g++-5\
gcc-5\
``` 

* [PlannerSingularity](https://drive.google.com/open?id=1FonR2VO5OaB2fbdCWqN8IRLCJZ-GVAY_)



