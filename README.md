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