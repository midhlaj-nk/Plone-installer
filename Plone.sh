#!/bin/bash

zenity --info \
--title="Plone Installer" \
--width=640 --height=500 \
--ok-label="Next" \
--text='<span font="20">Welcome to Plone Installer!</span>\n<span foreground="red" font="12">By Cybrosys Technologies</span>'\

# Prompt the user for the installation option
option=$(zenity --list \
    --title="Plone Installer" \
    --column="Option" --column="Select an installation method" \
    "1" "Install Plone 6.0.1 Classic (Standalone)" \
    "2" "Install latest Volto Frontend (Standalone)" \
    "3" "Install Plone 6.0.1 with the latest Volto Frontend" \
    --width=640 --height=500)


# Prompt the user for the password
password=$(zenity --password \
    --title="Adminstrative Authentication")

# Validate the password
echo $password | sudo -S echo "Password is correct"
if [ $? -eq 0 ]; then
    case $option in

        1)
          sudo apt-get install build-essential python-dev-is-python3 libjpeg-dev libxslt-dev python3.8-dev -y    
          echo "packages"
          sudo apt-get install python3.9-venv -y
          echo "packages"
          sudo apt install python3.9 -y
          echo "python 3.9"
        # Prompt the user for the directory name
        dir_name=$(zenity --entry \
            --title="Plone Installer" \
            --width=640 --height=500 \
            --text="Enter the name for you Plone Directory:" \
            --entry-text="")

        # Create the directory
        mkdir "$dir_name"

        # Go to the directory and create a Python venv
        cd "$dir_name"

        #Set the administration password for plone
        admin_password=$(zenity --entry \
            --title="Plone Installer" \
            --width=640 --height=500 \
            --text="Enter the an administrative password for plone:" \
            --entry-text="")
       
        # Create a buildout.cfg file with "Hello world"
        echo "[buildout]
extends = https://dist.plone.org/release/6.0.1/versions.cfg
parts = instance
[instance]
recipe = plone.recipe.zope2instance
eggs =
   Plone
   plone.volto
user = admin:"$admin_password"" > buildout.cfg

    echo "buildout.cfg created!"
    python3.9 -m venv .
    echo "python venv created!"
    bin/pip install -r https://dist.plone.org/release/6.0.1/requirements.txt
    echo "python requirements installed!"

    ./bin/buildout
    echo "First Buildout Done!"
    ./bin/buildout


            zenity --info \
    --title="Plone Installer" \
    --width=640 --height=500 \
    --text='<span font="20">The Installation is completed succesfully! </span>
            \n<span  font="14">To run the instance go to the directory of plone and open a terminal</span>
            \n<span  font="13">And run the commands below as per your needs</span>
            \n<span foreground="blue" font="12">./bin/instance start (To start the instance)</span>
            \n<span foreground="blue" font="12">./bin/instance stop (To stop the instance)</span>
            \n<span foreground="blue" font="12">./bin/instance debug (used to debug the instance)</span>)
             \n<span foreground="blue" font="12">./bin/instance fg (Used for development purposes, as it serves the complete live log of the running instance, the user may experience slow performance)
</span> '\
;;

    2)
    sudo apt install cmdtest
         # Get the name for the new Volto directory
         #install nvm
         touch ~/.bash_profile
         curl -o- https://raw.githubusercontent.com/creationix/nvm/v0.39.3/install.sh | bash
         source ~/.bash_profile
         nvm --version
    volto_dir_name=$(zenity --entry \
        --title="Plone Installer" \
        --width=640 --height=500 \
        --text="Enter the name for your Volto Directory:" \
        --entry-text="")
     
    # Create the directory
    mkdir "$volto_dir_name"

    # Go to the directory and create a Python venv
    cd "$volto_dir_name"
    curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.1/install.sh | bash
    sudo apt-get install build-essential libssl-dev curl git-core
    export NVM_DIR="$([ -z "${XDG_CONFIG_HOME-}" ] && printf %s "${HOME}/.nvm" || printf %s "${XDG_CONFIG_HOME}/nvm")"
    [ -s "$NVM_DIR/nvm.sh" ] && \. "$NVM_DIR/nvm.sh"
    nvm install 16
    nvm use 16
    sudo npm install -g yo
    curl -sSf https://dl.yarnpkg.com/debian/pubkey.gpg | sudo apt-key add -
    echo "deb https://dl.yarnpkg.com/debian/ stable main" | sudo tee /etc/apt/sources.list.d/yarn.list
    sudo apt-get update -y
    sudo apt-get install yarn
    npm install -g yo @plone/generator-volto
    zenity --info --title="Plone Installer" --width=640 --height=500  --text="Please configure you're Volto project in the terminal."
    yo @plone/volto | tee -a volto-install.log


    ;;

    3)
    echo "Initiating Full Installation..."
      sudo apt-get install build-essential python-dev-is-python3 libjpeg-dev libxslt-dev python3.8-dev -y    
          echo "packages"
          sudo apt-get install python3.9-venv -y
          echo "packages"
          sudo apt install python3.9 -y
          echo "python 3.9"
        # Prompt the user for the directory name
        dir_name=$(zenity --entry \
            --title="Plone Installer" \
            --width=640 --height=500 \
            --text="Enter the name for you Plone Directory:" \
            --entry-text="")

        # Create the directory
        mkdir "$dir_name"

        # Go to the directory and create a Python venv
        cd "$dir_name"

        #Set the administration password for plone
        admin_password=$(zenity --entry \
            --title="Plone Installer" \
            --width=640 --height=500 \
            --text="Enter the an administrative password for plone:" \
            --entry-text="")
       
        # Create a buildout.cfg file with "Hello world"
        echo "[buildout]
extends = https://dist.plone.org/release/6.0.1/versions.cfg
parts = instance
[instance]
recipe = plone.recipe.zope2instance
eggs =
   Plone
   plone.volto
user = admin:"$admin_password"" > buildout.cfg

    echo "buildout.cfg created!"
    python3.9 -m venv .
    echo "python venv created!"
    bin/pip install -r https://dist.plone.org/release/6.0.1/requirements.txt
    echo "python requirements installed!"

    ./bin/buildout
    echo "First Buildout Done!"
    ./bin/buildout

    #Volto Installation

     sudo apt install cmdtest
         # Get the name for the new Volto directory
    volto_dir_name=$(zenity --entry \
        --title="Plone Installer" \
        --width=640 --height=500 \
        --text="Enter the name for your Volto Directory:" \
        --entry-text="")

    # Create the directory
    mkdir "$volto_dir_name"

    # Go to the directory and create a Python venv
    cd "$volto_dir_name"
    curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.1/install.sh | bash
    sudo apt-get install build-essential libssl-dev curl git-core
    export NVM_DIR="$([ -z "${XDG_CONFIG_HOME-}" ] && printf %s "${HOME}/.nvm" || printf %s "${XDG_CONFIG_HOME}/nvm")"
    [ -s "$NVM_DIR/nvm.sh" ] && \. "$NVM_DIR/nvm.sh"
    nvm install 16
    nvm use 16
    sudo npm install -g yo
    curl -sSf https://dl.yarnpkg.com/debian/pubkey.gpg | sudo apt-key add -
    echo "deb https://dl.yarnpkg.com/debian/ stable main" | sudo tee /etc/apt/sources.list.d/yarn.list
    sudo apt-get update -y
    sudo apt-get install yarn
    npm install -g yo @plone/generator-volto
    zenity --info --title="Plone Installer" --width=640 --height=500  --text="Please configure you're Volto project in the terminal."
    yo @plone/volto | tee -a volto-install.log

                zenity --info \
    --title="Plone Installer" \
    --width=640 --height=500 \
    --text='<span font="20">The Installation is completed succesfully! </span>'\

    esac
else
    zenity --error \
        --title="Plone Installer" \
        --text="Incorrect password entered. Please try again." \
        --width=400 --height=200
    exit 1
fi
