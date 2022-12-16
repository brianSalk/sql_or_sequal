# sql_or_sequal
a simple web scraping script to investigate how redditors pronounce SQL?
This script uses the praw module to create a reddit scrapper that searches submissions and comments for the word SQL proceeded by either 'a' or 'an'.
If people are saying 'a SQL', we can assume they are pronouncing the word 'sequal'.  If on the other hand, they are typing 'an SQL', we assume they 
are saying 'a ESS-QUE-EL'.

## How to use this script
**0)** make sure that you have praw 7.6.0 (or newer) installed \
**1)** clone this repo to your computer. \
**2)** create a folder in the repo called *credentials.py* \
**3)** create a reddit account (if you don't already have one) and log into your account \
**4)** create a reddit script at <https://www.reddit.com/prefs/apps/> \
**5)** once you have created your app, create the following variables in your *credentials.py* file: \
	*client_id, client_secrete, user_agent, username, password* \
and set each to its appropriate value 
### Examples
#### search 300 submissions in r/sql and r/programminghumor, also print a chart of the data
`python sql_or_sequal -s 'sql+programminghumor' -l 300 --chart`
## Help
Please help me: \
remove the error output at the beginning. \
Do more meaningful analysis (Can we apply some hypothesis testing or basian statistics?) \
make the code run faster. \


