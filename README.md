# Installation on Amazon Elastic Beanstalk

Need to use something larger than a t2.micro. I used a t2.micro and it ran out of memory.

ssh into the instance. Start by installing the basics with yum:

`
sudo yum install update
sudo yum install git
sudo yum groupinstall "Development Tools"
sudo yum install python-devel libpng-devel freetype-devel 
`

the last two are necessary for pip to run without failing with error 'Command "python setup.py egg_info" failed with error code 1'

next we set up the virtual environment:

`
git clone https://github.com/ktarrant/stockfinder
cd stockfinder
virtualenv venv
source venv/bin/activate
pip install -r requirements.txt
`