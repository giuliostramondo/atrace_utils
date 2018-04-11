Application Access Generation and Schedule utilities
===================================================
This repository contains tools to generate synthetic parallel application access traces and to schedule those applications access trace on PolyMem.

Requirements
============
These scripts use Python 2.7, with the following libraries:
* Pulp
* Enum
* matplotlib


Synthetic Parallel Access Trace Generations
==========================================
The python tool "generate_access_traces.py" is used to generate synthetic parallel access trace.

It is used with the following parameters:
```
usage: generate_access_traces.py [-h] -r -s -M -N -o

Tool to generate 2D linear access traces.

positional arguments:
  -r          number of elements to read in sequence
  -s          number of elements to skip in sequence
  -M          Number of columns in the 2D data structure
  -N          Number of rows in the 2D data structure
  -o          number of elements to skip at the beginning

optional arguments:
  -h, --help  show this help message and exit
```

The tool outputs a file containing a list of parallel accesses with .atrace extension. This file can be used as input to the scheduling tool.

Examples of access traces generated using this tool are in the ./patterns folder.

PolyMem scheduling tool
=============================
The python tool "schedule_atrace.py" is used to schedule an application parallel access trace on PolyMem.

It is used with the following parameters:

```
usage: schedule_atrace.py [-h] atrace scheme

Tool to schedule a given access trace.

positional arguments:
  atrace      path to the file containing the access trace to schedule
  scheme      prf scheme to use for scheduling the access trace (ReRo, ReCo,
              RoCo, ReTr)

optional arguments:
  -h, --help  show this help message and exit
```

The tool outputs a file containg a close to minimal schedule ( with .schedule extension ), which can be directly loaded in PolyMem to access application data.

Examples of schedules obtained using this tool and synthetic traces in the ./patterns/ folder, are in the ./schedules folder.
