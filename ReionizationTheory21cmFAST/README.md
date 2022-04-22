# Reionization Theory and 21cmFAST

This session will recap on some cosmology from [Lesson 1](Lesson1_21cmCosmo), and go
into more detail about the theory of reionization -- the role of Hydrogen in the 
Universe, the spin-flip (21cm) transition, sources of (re)ionization, and the history
of structure formation.

To bring these ideas to life, we will concurrently introduce and demonstrate the
state-of-the-art simulator [21cmFAST](https://github.com/21cmFAST/21cmFAST) to produce
views into the Universe at different stages of its formation.

The presentation slides can be found [here](https://docs.google.com/presentation/d/1jWLQjym993eqXkbzp5phoTTw6hALMFRjHyJcjaA5xqA/edit?usp=sharing).

During the presentation, we will be creating a Jupyter notebook to generate and view the 
outputs of 21cmFAST. A template copy of this notebook is in this repo [here](reionization_theory_tute.ipynb).
A [solutions notebook](reionization_theory_tute_solutions.ipynb) is also available, but
we strongly recommend you use that only *after* the tutorial for reference.

The notebook should use the `21cmfast` conda environment that should be installed
already on your NRAO account. If you plan to run the lesson locally, do

```
conda env create -f Precamp/21cmfast_env.yml
```

to install the 21cmfast environment first.

