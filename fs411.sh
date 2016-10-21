#!/usr/bin/env bash

#############################################
#############################################
## 
## Customize this part if you must...or just 
## keep the default settings for a care-free
## install experience.
##
## These are for setting up the database
##
#############################################

db_name='fishingspots'
db_user='django'
db_password='secret'
app_key='y04d8p6(e_1nrwlxx8#^9grr*u%7)!6rilkwga)^rewqb3yq&c'

start_seconds="$(date +%s)"
echo "Welcome to Billy's Big Beautiful Bash Bonanza"

ping_result="$(ping -c 2 8.8.4.4 2>&1)"
if [[ $ping_result != *bytes?from* ]]; then
    echo "Network unavailable. Exiting."
    exit 1
fi

apt_packages=(
    vim
    curl
    git-core
    nodejs

    make
    build-essential
    libssl-dev
    zlib1g-dev
    libbz2-dev
    libreadline-dev
    libsqlite3-dev

    virtualenv
    python-pip
    python3-dev
    
    binutils
    libgeoip1
    gdal-bin
    python-gdal
    
    postgresql-9.5
    postgresql-9.5-postgis-2.2
    pgadmin3
    postgresql-client-common
    postgresql-contrib-9.5
    
    # Needed for python dependencies
    libpq-dev # psycopg2
    libjpeg-dev # python-pillow
)

wget --quiet -O - https://www.postgresql.org/media/keys/ACCC4CF8.asc | sudo apt-key add -
sudo add-apt-repository -y "deb https://apt.postgresql.org/pub/repos/apt/ xenial-pgdg main"

echo "Update and Upgrade..."
sudo apt-get update
sudo apt-get upgrade

echo "Installing packages..."
sudo apt-get install -y ${apt_packages[@]}
sudo apt-get clean

echo "Setup PostgreSQL..."
if sudo -u postgres psql -lqt | cut -d \| -f 1 | grep -qw $db_name; then
    echo "PostgreSQL database exists. Skipping setup."
else
    sudo -u postgres psql -c "CREATE EXTENSION adminpack"
    sudo -u postgres psql -c "CREATE DATABASE $db_name"
    sudo -u postgres psql $db_name -c "CREATE EXTENSION postgis"
    sudo -u postgres psql -c "CREATE USER $db_user WITH PASSWORD '$db_password'"
    sudo -u postgres psql -c "ALTER ROLE $db_user SET client_encoding TO 'utf8'"
    sudo -u postgres psql -c "ALTER ROLE $db_user SET default_transaction_isolation TO 'read committed'"
    sudo -u postgres psql -c "ALTER ROLE $db_user SET timezone TO 'UTC'"
    sudo -u postgres psql -c "ALTER ROLE $db_user SUPERUSER"
    sudo -u postgres psql -c "GRANT ALL PRIVILEGES ON DATABASE $db_name TO $db_user"   
fi

cd /home/$USER
mkdir venvs
virtualenv --python=/usr/bin/python3 venvs/fs411
echo "Activating virtual environment..."
source /home/$USER/venvs/fs411/bin/activate

echo "Cloning project from github..."
git clone https://github.com/SELUDreamTeam/FishingSpots.git
cd FishingSpots

echo "Creating .env file..."
echo "SECRET_KEY = '$app_key'" >> .env
echo "DB_NAME = '$db_name'" >> .env
echo "DB_USER = '$db_user'" >> .env
echo "DB_PASSWD = '$db_password'" >> .env
echo "DEBUG = True" >> .env

echo "Installing requirements from pip..."
pip install -r requirements.txt

echo "Django migrations..."
python manage.py makemigrations
python manage.py migrate

echo "Creating Django superuser..."
echo "...you will need a user name and password that is"
echo "...with a minimum of 8 characters..."
python manage.py createsuperuser

end_seconds="$(date +%s)"

echo "------------------------------"
echo "Setup completed in "$(expr $end_seconds - $start_seconds)" seconds."

echo "You can start the application now by running: "
echo "python manage.py runserver"

