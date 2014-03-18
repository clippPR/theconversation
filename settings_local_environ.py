import os

# connection string for your mongodb instance.
os.environ['MONGODB_URL'] = "mongodb://heroku:5_Ccqy27rFkd1wESPlE_AqfYIimcobdoieztdZkd6srOEZTOXbVfgdnYcjmeZjoOmQcHslAhoX3AuOZ30QBxDw@oceanic.mongohq.com:10065"
os.environ['DB_NAME'] = "app23110495"

# Environment -- use "dev" for local development; "test" for staging, "prod" for production
os.environ['ENVIRONMENT'] = "dev"

os.environ['BASE_URL'] = "localhost:8001"
os.environ['COOKIE_SECRET'] = "9HjKRKMHiEjHfQq8Z6hFkHYf"

os.environ['DISQUS_PUBLIC_KEY'] = "1ed7caJuh7VFZmGMjzOueYCDRfBCPsD9nWjBS1U7dC62hFfW5IT02yssKbbhHBUS"
os.environ['DISQUS_SECRET_KEY'] = "a7LjzUAo3PR4y020Yc786Rjs85rXkyQXfW3c4twpY5JADAIZrzslKmhMiQLb4F2F"
os.environ['DISQUS_SHORT_CODE'] = "primeloopcmty"

os.environ['TWITTER_CONSUMER_KEY'] = "CV7SfZsLQSgGdjgtMOPobQ"
os.environ['TWITTER_CONSUMER_SECRET'] = "sh0Dq9T51UeBfBVndeIW0suzNvkq4MlPYkBZ1gwU"

os.environ['SENDGRID_USER'] = "cmty"
os.environ['SENDGRID_SECRET'] = "3CzFHb7kCsK7coKC"
