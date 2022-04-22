**HERA CHAMP Camp**

**Lesson 7**

**Interferometry and Synthesis Imaging**

Goal of the afternoon: Obtain a basic familiarity with radio interferometry.

Instructor: Danny Jacobs

**Outline**

**Hour 1**

Lecture with a few slides.

<img src="https://github.com/HERA-Team/CHAMP_Bootcamp/blob/master/Lesson7_Interferometry/SNR_G55.png" alt="SNR" width="400px" align="right" style="width:100px; align:right;"/>

Goals:

- interferometry measures Fourier modes of the sky
- the number and distribution of the modes comes from baseline samples of the uv plane.
- the Fourier Transform of the baseline distribution is the shape of the image point spread function.
- The relationship between geometric delay and the relationship this bears to resolution.

[Notes](http://hera.pbworks.com/w/file/117911112/1271_001.pdf)


**Imaging Workshop**

Here we will image some VLA data of a supernova remnant.  Progressively add data to see how the image quality improves, seeing in practice the effects of uv coverage by increasing the number of antennas, and then the amount of time.

Caveat: We will be using CASA, an imaging package developed by the National Radio Astronomy Observatory for use with radio telescopes like the VLA.  Because of the unique nature of HERA, many collaboration members do not use CASA.

Caveat: We are using VLA data because HERA is still under construction, we're still working out how to calibrate it.

Caveat: The VLA data here are stored in 'ms'; files. Other formats you will see in the collaboration are _uvfits_ which will end in '.fits' and _miriad_

which will end in '.uv'; (or, more likely, with a more complicated filename like .uvcRRE)

Lets leave the real world behind for a moment and use nicely calibrated data to make images of something cool.

**Prequel**
A note about how to read code in the tutorial 

This is what a bash command might look like.  The goal is to give a command you can copy and paste and into which program it goes. Note that the terminal part `bash $` or `casa >` will probably look different on your machine depending on your setup. You don't paste in that part.
```
bash $  ls   # Comments are indicated with the '#'. You don't need to copy that part.
. .. test_directory
bash $ casa  # Start casa
casa <1>: help  # run the help command in casa.
```


**Setup and get data**
Set up and run casa. Get data
```
bash $ cd ~   #make a directory.  Note that you'll need about 
bash $ mkdir imaging_workshop
bash $ cd imaging_workshop  
bash $ wget http://casa.nrao.edu/Data/EVLA/SNRG55/SNR_G55_10s.calib.tar.gz  #download some calibrated VLA data.
bash $ tar -xvzf SNR_G55_10s.calib.tar.gz
```
The goal of this tutorial is to examine the various ways &quot;aperture synthesis&quot; can be affected.  The quality of an image has a direct relationship to the amount and kind of samples of the fourier plane.

**UV density/ antennas**

Adding VLA antennas.  Start with a single baseline.
```
bash$ casa
#Make a uv plot of a single baseline (it will be kind of silly)
casa <1>: plotms(vis='SNR_G55_10s.calib.ms', selectdata=True, timerange='05:48:18~05:48:28', spw='1:32', antenna='0&4', xaxis='U', yaxis='V')
#make a single baseline image
casa <2>: tclean(vis='SNR_G55_10s.calib.ms', imagename='SNR_G55_10s.2ant',weighting='natural',imsize=540,cell='8arcsec',niter=0,interactive=False, antenna='0&4', timerange='05:48:18~05:48:28', spw='1:32')
casa <3>: viewer('SNR_G55_10s.2ant.psf')#look at the psf
casa <4>: viewer('SNR_G55_10s.2ant.image')#look at the image
```
Now 10 antennas.
```
#make a uv plot of 10 antennas

casa <1>: plotms(vis='SNR_G55_10s.calib.ms', selectdata=True, timerange='05:48:18~05:48:28', spw='1:32', antenna='0~10&', xaxis='U', yaxis='V')
#Make an image with 10 antennas
casa <2>: tclean(vis='SNR_G55_10s.calib.ms', imagename='SNR_G55_10s.10ant',weighting='natural',imsize=540,cell='8arcsec',niter=0,interactive=False,antenna='0~10&', timerange='05:48:18~05:48:28', spw='1:32')
casa <3>: viewer('SNR_G55_10s.10ant.psf')#look at the psf
casa <4>: viewer('SNR_G55_10s.10ant.image')#look at the image
```
The full array!

#make a uv plot with all antennas
```
casa <1>: plotms(vis='SNR_G55_10s.calib.ms', selectdata=True, timerange='05:48:18~05:48:28', spw='1:32', xaxis='U', yaxis='V')
#Make an image with all antennas
casa <2>: tclean(vis='SNR_G55_10s.calib.ms', imagename='SNR_G55_10s.allant',weighting='natural',imsize=540,cell='8arcsec',niter=0,interactive=False, timerange='05:48:18~05:48:28', spw='1:32')
casa <3>: viewer('SNR_G55_10s.allant.psf')#look at the psf
casa <4>: viewer('SNR_G55_10s.allant.image')#look at the image
```


**Time**
```
#lets increase the amount of time data from 10 seconds to 9 hours
casa <1>: plotms(vis='SNR_G55_10s.calib.ms', selectdata=True, spw='1:32', antenna='0&4', xaxis='U', yaxis='V')
casa <2>: tclean(vis='SNR_G55_10s.calib.ms', imagename='SNR_G55_10s.alltime',weighting='natural',imsize=540,cell='8arcsec',niter=0,interactive=False, spw='1:32')
casa <3>: viewer('SNR_G55_10s.alltime.psf')#look at the psf
casa <4>: viewer('SNR_G55_10s.alltime.image')#look at the image
```
**Clean**

Deconvolves or removes the psf.

#pause for a short explanation of what clean is
```
casa <1>: tclean(vis='SNR_G55_10s.calib.ms', imagename='SNR_G55_10s.clean',weighting='natural',imsize=540,cell='8arcsec',niter=1000,interactive=True, spw='1:32')
casa <2>: viewer('SNR_G55_10s.clean.psf')#look at the  **dirty image**
casa <3>: viewer('SNR_G55_10s.clean.image')#look at the  **cleaned image**
casa <4>: viewer('SNR_G55_10s.clean.residual')#look at the  **residual image**
```


**Source material for imaging workshop**

[https://casaguides.nrao.edu/index.php/VLA\_CASA\_Imaging](https://casaguides.nrao.edu/index.php/VLA_CASA_Imaging)

[https://casaguides.nrao.edu/index.php?title=VLA\_Continuum\_Tutorial\_3C391](https://casaguides.nrao.edu/index.php?title=VLA_Continuum_Tutorial_3C391)
