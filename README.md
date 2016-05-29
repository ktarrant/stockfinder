# Installation on Amazon Elastic Beanstalk

Need to use something larger than a t2.micro. I used a t2.micro and it ran out of memory.
I recommend the t2.small. Make sure to say "yes" when it asks you if you want to set up an RDS 
storage. We will use this for the Django database.

Once it finishes setting stuff up, add the environment variables for the database credentials:

```
RDS_TABLE_NAME
RDS_USERNAME
RDS_PASSWORD
RDS_HOSTNAME
RDS_PORT
```

You also need to set up the plotly credentials:

```
PLOTLY_USERNAME
PLOTLY_API_KEY
```

Select the superuser accounts:

```
SUPERUSER_USERNAME
SUPERUSER_EMAIL
SUPERUSER_PASSWORD
```

The Django settings. I don't know what the "correct" way to generate a secret key is. I create a
temporary project using `django-admin startproject` and then take the secret key from the generated
settings.py project. I think you could probably just generate a key of the correct length from a 
hex generator.

```
DJANGO_SECRET_KEY
DJANGO_SETTINGS_MODULE
```

Clone the repo to your local machine. Install the AWS EB CLI tool if you don't have it already:

```
git clone https://github.com/ktarrant/stockfinder.git
cd stockfinder
pip install awsebcli
eb init
# Set up with AWS Elastic Beanstalk using the prompt
eb deploy
```