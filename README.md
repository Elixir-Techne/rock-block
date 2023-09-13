# Rockblock Integration

# Running Locally


## Copy environment file and fill all requirements

    $ cp .env.template .env


## Run Server
- **Create Virtual environment**

  `$ python3 -m venv /path/to/new/virtual/environment`

  `$ source /path/to/new/virtual/environment/bin/activate`


- **Install dependencies**
    
    `$ pip install -r requirements.txt`


- **Run Migrations**

    `$ alembic upgrade head`


- **Run Server**

    `$ uvicorn rockblock_integration.main:app --reload --port 8000`


- **Test Application**

    - `Open swagger URL http://127.0.0.1:8000`


# Update Server AWS
- **Connect to AWS Server**

  `$ ssh -i "rockblock-integration.pem" ubuntu@ec2-16-171-76-6.eu-north-1.compute.amazonaws.com`


- **Update Code files**
 
  `$ sudo -f`

   `$ cd /home/ubuntu/rockblock_integration`


- **Rebuild Docker**
 
  `$ docker-compose down`
 
  `$ docker-compose build`


- **Start Docker**
 
  `$ docker-compose up -d`
