FROM python:3.8
RUN pip install scipy praw matplotlib

ADD sql_or_sequal.py praw_lib.py credentials.py pyplot_lib.py

CMD ["python", "./sql_or_sequal.py"]

