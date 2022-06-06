# Pre-camp Setup

To set up before CHAMP camp arrives, please follow all the instructions on this page!

## Respond to the Survey

Before camp, please respond to the [pre-summer survey](https://forms.gle/oRHwgrfLXKWGufjSA)!


## Computing Setup

Please follow all the instructions below, *before* you get to camp. 
If you have **any trouble at all** please email one of the co-ordinators! 

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
* Install the C-compiler by running `sudo apt install gcc`.

#### Everyone
* Open a *terminal* (Mac/Linux: open application called "Terminal", Windows: Start Menu -> "Ubuntu [VERSION NUMBER]"). You'll need this for many of the steps below.

* Test that you can log into NRAO: 
  * In your terminal type: `ssh <username>@login.aoc.nrao.edu` (replace your username). If there's an error message, please email a co-ordinator.
 
* Install Python using Anaconda. Open your terminal and type the following according to which OS you're on. You'll have to answer a few questions by typing and hitting ENTER after running the following command. Use the default response for everything, *except* say "yes" for initializing conda:
  * `curl -o ~/install_conda.sh https://raw.githubusercontent.com/HERA-Team/CHAMP_Bootcamp/main/Precamp/install_conda_envs.sh`
  * `sh ~/install_conda.sh`
  
* Install GitKraken:
  * Go here: https://www.gitkraken.com/download and download for your system (on Windows, download the Windows version).
  * Make sure it opens (don't have to add any profile info yet, just make sure it opens)

* Install VS Code for your OS (Windows version on Windows): https://code.visualstudio.com/Download 
  * Make sure it opens.

* Create a GitHub account (if you don't already have one)
  * Go to https://github.com and click Sign Up.

* Download data needed for the shell lesson: https://swcarpentry.github.io/shell-novice/data/shell-lesson-data.zip
  * Unzip the folder and place it in your desktop.
