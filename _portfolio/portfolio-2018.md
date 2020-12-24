---
title: "IBaCoP (IPC-2018)"
excerpt: "
IBaCoP family of planning
portfolios submitted to the International Planning Competition 2018. Our portfolios are improved versions of the planners submitted to the last IPC-2014. IBaCoP-2018 is configured following a Pareto efficiency approach for selecting
planners and then giving the same execution time for the selected planners. IBaCoP2-2018 decides for each problem the
sub-set of planners to use. This decision is based on predictive
models trained with domain/problems from previous IPCs.
Both 2018 portfolios compete in the sequential satisficing and
agile tracks."
collection: portfolio
---
We trained a predictive model for a (yes/no) classification task using Rotation Forrest (Rodriguez, Kuncheva, and
Alonso 2006). The model tries to encode whether a given
planner will solve the planning task or not. IBaCoP2-2018
is the result of querying this model and selecting the five
planners with the best “positive” prediction confidence.


Planners:
<!--- img src='https://ai2-s2-public.s3.amazonaws.com/figures/2017-08-08/1c09279a3d5659785890042fe906dcfeccff1c20/20-Figure3-1.png'--->

• jasper 
• mercury
• BFS(F) 
• SIW 
• FDSS-2
• probe 
• yashp2-mt
• lama-2011
• lamar
• arvand 

Planner abstract: https://icenamor.github.io/files/IBaCoP_2018.pdf

Source-code: git clone https://bitbucket.org/isabelcenamorg/ibacop2-2018-final-version.git

