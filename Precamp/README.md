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

#### Everyone
* Open a terminal (Mac/Linux: open application called "Terminal", Windows: Start Menu -> "Ubuntu [VERSION NUMBER]"). You'll need this for many of the steps below.

* Test that you can log into NRAO: 
  * In your terminal type: `ssh <username>@login.aoc.nrao.edu` (replace your username). If there's an error message, please email a co-ordinator.

* Download the CHAMP_Bootcamp lessons:
  * Right-click [this link](https://github.com/HERA-Team/CHAMP_Bootcamp/archive/refs/heads/main.zip) and save to your computer. The rest of the instructions will assume you've downloaded to your "Desktop" folder. If you know what you're doing, you can place it elsewhere.
  * Unzip the downloaded archive with whatever software you usually use to do that (extract to your Desktop)
 
* Install Python using Anaconda:
  * Download Miniconda from here: https://docs.conda.io/en/latest/miniconda.html. Choose the 64-bit version for your OS. If you're on Windows, choose the Linux 64-bit installer (because we're going to use it through WSL). On MacOS, choose the "bash" version. Save to your "Downloads" folder.
  * Run the miniconda installer. Answer any questions with the default response, EXCEPT "Do you wish the installer to initialize Miniconda3 by running conda init" -- say YES to this: 
    * Mac: In your terminal, type `cd ~/Downloads; sh Miniconda3-latest-MacOSX-x86_64.sh`.   
    * WSL: In your terminal, type `cd ~/windows-home/Downloads; sh Miniconda3-latest-Linux-x86_64.sh`.
    * Linux: In your terminal, type `cd ~/Downloads; sh Miniconda3-latest-Linux-x86_64.sh`.
  * Type `source ~/.bashrc`. You should see "(base)" at the start of your command prompt now.
  
* Install the C-compiler (if you're on Windows/WSL):
  * In your terminal, type `sudo apt install gcc`
  
* Install the Python packages you'll need. Do all of these steps in your terminal:
  * Create a HERA conda environment: 
    * Linux/Mac: `conda env create -f ~/Desktop/CHAMP_Bootcamp-main/Precamp/hera_env.yml`
    * WSL: `conda env create -f ~/windows-home/Desktop/CHAMP_Bootcamp-main/Precamp/hera_env.yml`
  * Create a 21cmFAST conda environment:
    * Linux/Mac: `conda env create -f ~/Desktop/CHAMP_Bootcamp-main/Precamp/21cmfast_env.yml`
    * WSL: `conda env create -f ~/windows-home/Desktop/CHAMP_Bootcamp-main/Precamp/21cmfast_env.yml`

* Install GitKraken:
  * Go here: https://www.gitkraken.com/download and download for your system (on Windows, download the Windows version).
  * Make sure it opens (don't have to add any profile info yet, just make sure it opens)

* Install VS Code for your OS (Windows version on Windows): https://code.visualstudio.com/Download 
  * Make sure it opens.

* Create a GitHub account (if you don't already have one)
  * Go to https://github.com and click Sign Up.

* Download data needed for the shell lesson: https://swcarpentry.github.io/shell-novice/data/shell-lesson-data.zip
  * Unzip the folder and place it in your desktop.
