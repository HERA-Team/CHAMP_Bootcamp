# Pre-camp Setup

The following are for students participating in CHAMP Camp who are not
explicitly CHAMP scholars, as well as instructors wishing to test their
installation at NRAO.

## Respond to the Survey

Before camp, please respond to the [pre-summer survey](https://docs.google.com/forms/d/1Iu_2P_mhiLYTOgoT8unPBoZX1CWTpwktb8WNQ-N3xW8/edit?usp=sharing)!

## Set up conda environments

The CHAMP students will have two pre-built environments based on the YAML files
in this directory: one for 21cmFAST and the other for HERA data processing. (The
CASA environment YAML is not currently used.) To install the environments using
conda, do:

```bash
$ conda env create -f 21cmfast_env.yml
$ conda env create -f hera_env.yml
```

This will create environments named `21cmfast` and `hera`, respectively, which
should be used for testing notebooks. To add these as kernels which can be used
in JupyterHub, do:

```bash
$ conda activate 21cmfast
$ ipython kernel install --user --name 21cmfast
$ conda deactivate
$ conda activate hera
$ ipython kernel install --user --name hera
$ conda deactivate
```

## Run CASA in a VNC Session at NRAO

For those students and instructors wishing to run CASA, please follow [the
instructions outlined in this document](./casa_vnc.pdf). If the instructions are
unclear or do not produce the expected results, please contact
[plaplant@berkeley.edu.](mailto:plaplant@berkeley.edu).
