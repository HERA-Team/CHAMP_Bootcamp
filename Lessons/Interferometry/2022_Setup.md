## Setup for Interferometry and Synthesis Imaging Tutorial
**2022 CHAMP Camp**

To run the Imaging tutorial, you will first need to login to the NRAO server and launch CASA. 

**Step 0: Patches!**
ssh into the nrao login node

```ssh <myname>@login.aoc.nrao.edu```

run this:

```cp ~djacobs/XTerm .```

**Step 1: Login**

Launch fastX: https://fastx.aoc.nrao.edu:3443/auth/ssh

Your screen should look like this: 

<img src="Setup/login.png" alt="Login screen" width="500px" align="center" style="width:500px; align:center;"/>

Enter your username and password and click "Log in". 

**Step 2: Launch Session**

Now that you are logged in, you need to launch a session by clicking the "Launch" button. 

<img src="Setup/fastX_home.png" alt="Home screen" width="600px" align="center" style="width:600px; align:center;"/>

This will pull up a number of different possible session types you can launch. You want to select "xterm on herapost-master" and then click the "Launch button". 

<img src="Setup/launch.png" alt="Launch screen" width="600px" align="center" style="width:600px; align:center;"/>

This should prompt a new window to open in your browser which displays a terminal window. 

<img src="Setup/terminal.png" alt="Terminal screen" width="500px" align="center" style="width:500px; align:center;"/>

**Step 3: Find data**

The data file you will be using should already be available in your current directory. Navigate with `cd` into the "VLA_Imaging_Tutorial" folder and `ls` to see the files. 

<img src="Setup/find_data.png" alt="Data folder" width="700px" align="center" style="width:700px; align:center;"/>

**Step 4: Launch CASA**

To launch CASA, simply type `casa` into the command line. This will open the `casa` enviornment in your terminal window. It will also open a "Log Messages" window, but you can minimize that as it is not important now. 

<img src="Setup/casa_launch.png" alt="CASA launch" width="700px" align="center" style="width:700px; align:center;"/>

**Data**
Your data are located in 
```/lustre/aoc/projects/hera/<myusername>/VLA_Imaging_Tutorial/```

run ```cd /lustre/aoc/projects/hera/<myusername>/VLA_Imaging_Tutorial/```
then
```casa``



**Finished!**

You are now ready to start the [Tutorial](HERA_CHAMP_Interferometry_tutorial.md)!
