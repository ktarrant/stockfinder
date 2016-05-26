# Installation on Amazon Elastic Beanstalk

Need to use something larger than a t2.micro. I used a t2.micro and it ran out of memory.
I recommend the t2.small.

Set it up to use Python. The default Python 3.4, Amazon Linux instance is acceptable.

Set up the RDS database. Set up the environment variables to pass in the information. See this page
for more information: http://docs.aws.amazon.com/elasticbeanstalk/latest/dg/AWSHowTo.RDS.html
How nice!

ssh into the instance. Start by installing the basics with yum:

```
sudo yum install update
sudo yum install git
sudo yum groupinstall "Development Tools"
sudo yum install python-devel libpng-devel freetype-devel 
```

the last two are necessary for pip to run without failing with error 'Command "python setup.py egg_info" failed with error code 1'

next we set up the virtual environment:

```
git clone https://github.com/ktarrant/stockfinder
cd stockfinder
virtualenv venv
source venv/bin/activate
pip install -r requirements.txt
```

When setting it up on Amazon, you need to use the production branch:
git checkout production

Whichever branch you are using, you need to make settings for it. This will contain the secret key
and the database settings. master is set up for a local dev environment. production is set up for
ana Amazon Elastic Beanstalk environment. Both need a fresh secret key provided.