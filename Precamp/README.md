# Pre-camp Setup

To set up before CHAMP camp arrives, please follow all the instructions on this page!

## Respond to the Survey

Before camp, please respond to the [pre-summer survey](https://forms.gle/oRHwgrfLXKWGufjSA)!


## Computing Setup

### Get Your NRAO account
Most of the computing work you'll do will be done on an external computer at the National Radio Astronomy Observatory (NRAO). 

* Request an account, following the instructions [here](https://docs.google.com/document/d/1tgLMCI7nQDjuXnoZWTcUSUT5vXq2XcJKiHoyboGHMBo/edit?usp=sharing).


### Setup your laptop
You'll also set up your own system to have the software required to follow most of the tutorials. If you're a windows user, follow the Windows instructions first, then go onto the instructions for everyone.

#### Windows Users

* Install Windows Subsystem for Linux (WSL) 2 following [these instructions](https://docs.microsoft.com/en-us/windows/wsl/install). You should install the (default) Ubuntu distribution. Follow all default instructions.
* Make sure you can open a WSL terminal (Start Menu -> "Ubuntu [VERSION NUMBER]")
* Setup your username and password on WSL: https://docs.microsoft.com/en-us/windows/wsl/setup/environment#set-up-your-linux-username-and-password (just that section)
* Make it easy to access your windows-drive documents: run `ln -s /mnt/c/Users/<YOUR WINDOWS USERNAME>/ windows-home`. Now you can access all your windows home files through `windows-home/`.

#### Everyone
* Open a terminal (Mac/Linux: open application called "Terminal", Windows: Start Menu -> "Ubuntu [VERSION NUMBER]"). You'll need this for many of the steps below.

* Test that you can log into NRAO: 
** In your terminal type: `ssh <username>@login.aoc.nrao.edu` (replace your username). If there's an error message, please email a co-ordinator.

* Install Python using Anaconda:

** Download Miniconda from here: https://docs.conda.io/en/latest/miniconda.html. Choose the 64-bit version for your OS. If you're on Windows, choose the Linux 64-bit installer (because we're going to use it through WSL). On MacOS, choose the "bash" version. Save to your "Downloads" folder.

** Run the miniconda installer: 
*** Mac: In your terminal, type `cd ~/Downloads; sh Miniconda3-latest-MacOSX-x86_64.sh`. Answer any questions it asks you to.
*** WSL: In your terminal, type `cd ~/widows-home/Downloads; sh Miniconda3-latest-Linux-x86_64.sh`.  Answer any questions it asks you to.
*** Linux: In your terminal, type `cd ~/Downloads; sh Miniconda3-latest-Linux-x86_64.sh`. Answer any questions it asks you to.

* Download the hera environment definition: right click [this link](https://github.com/HERA-Team/CHAMP_Bootcamp/blob/main/Precamp/hera_env.yml) and save to your Downloads folder.
* Install the Python packages you'll need. Do all of these steps in your terminal:
** Create a HERA conda environment: 
*** Linux/Mac: `conda env create -f ~/Downloads/hera_env.yml`
*** WSL: `conda env create -f ~/windows-home/Downloads/hera_env.yml`

* Install GitKraken:
** Go here: https://www.gitkraken.com/download and download for your system (on Windows, download the Windows version).
** Make sure it opens (don't have to add any profile info yet, just make sure it opens)

* Create a GitHub account (if you don't already have one)
** Go to https://github.com and click Sign Up.

