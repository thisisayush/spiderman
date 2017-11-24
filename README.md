# Scrapy Web Management Portal

### Getting Started (Development)

#### Install Virtualenv
```
sudo apt-get install virtualenv
```
#### Create and Activate Python2 Virtual Environment:

```
virtualenv -p python2 venv 
```
```
source venv/bin/activate
```

P.S. Make virtualenv outside the repo

#### Install Requirements
Navigate to ```<REPO_BASE>/spiderman```

```
pip install -r requirements.txt
```

#### Initialize Database (Automated Method)

```
source initialize.sh
```

#### Initialize Database (Manual Method)

```
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
```

#### Start The Development Server

```
python manage.py runserver
```
