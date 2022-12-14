# sql_or_sequal
a simple web scraping script to investigate the most important question known to mankind: How do redditors pronounce SQL?
This script is simple!  It uses praw to create a reddit scrapper that searches submissions and comments for the word SQL followed by either 'a' or 'an'.
If people are saying 'a SQL', we can assume they are pronouncing the word 'sequal'.  If on the other hand, they are typing 'an SQL', we assume they 
are saying 'a ESS-QUE-EL'.

## How to use this script
**0)** make sure that you have praw 7.6.0 (or newer) installed \
**1)** clone this repo to your computer. \
**2)** create a folder in the repo called *credentials.py* \
**3)** create a reddit account (if you don't already have one) and log into your account \
**4)** create a reddit app at <https://www.reddit.com/prefs/apps/> \
**5)** once you have created your app, create the following variables in your *credentials.py* file: \
	*client_id, client_secrete, user_agent, username, password* \
and set each to its appropriate value \
### Examples
python sql\_or\_sequal -s 'sql+programminghumor' -l 300 --chart

