# sql_or_sequal
a simple web scraping script to investigate how redditors pronounce SQL?
This script uses the praw module to create a reddit scrapper that searches submissions and comments for the word SQL proceeded by either 'a' or 'an'.
If people are saying 'a SQL', we can assume they are pronouncing the word 'sequal'.  If on the other hand, they are typing 'an SQL', we assume they 
are saying 'a ESS-QUE-EL'.

## How to use this script
**0)** make sure that you have praw 7.6.0 (or newer) installed 
```
pip install praw` or `pii install --upgrade praw
```
**1)** clone this repo to your computer. 
```
git clone https://github.com/brianSalk/sql_or_sequal
```
**2)** create a reddit account if you do not already have one 
**3)** [create a reddit app](https://www.reddit.com/prefs/apps/) make sure you check the option for script \
**4)** in your cloned repository, create a new folder called `cridentials.py`.
```
touch cridentials.py
```
**5)** Using the information from the reddit.com/prefs/apps, create the following 5 variables and store them in `credentials.py`
```
client_secret="asdfkajsldfkjasj83j823j" # located after word "secret"
client_id="29829383983f9h2389fh2398fh2" # located right under app name
usename="me123" # your reddit user name
password="secret12" # your reddit password
useragent="blahblah" # set equal to any string
```
[This picture](https://imgur.com/a/7PMAFCW) shows you where the client_id and client_secret are.

### Examples
#### view complete list of valid command line arguments along with breif summary of usage:
```
python sql_or_sequal.py -h
```
#### search 300 submissions in r/sql and r/programminghumor, also print a chart of the data
```
python sql_or_sequal.py -s 'sql+programminghumor' -l 300 --chart
```
As of now there is a lot of stderr output.  To suppress the stderr output, prepend `2> /dev/null ` to the above command: 
```
2> /dev/null python sql_or_sequal.py -s 'sql+programminghumor' -l 300 --chart
```
## Help Wanted
**Please help me:** \
remove the error output at the beginning. 



