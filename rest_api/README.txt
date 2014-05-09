REST API
========

Assumptions:

  * You have python installed. This was developed on 2.7 but may work with other versions although is untested.
	* You have virtualenv installed
	* You have pip installed

Instructions:

  1) Setup virtualenv+flask
    a) virtualenv env
    b) source env/bin/activate
    c) pip install -r requirements.txt

  2) Run the api server:
    a) ./rest_server.py

  3) Test per the specs in README.md

Language justification:

  I'm a huge fan of python for tasks like this. It's easy to use and has great
resources available for it. I'm generally a django user, which I really like but
django is just absolute overkill for a simple REST API like this. I had heard of
flask before so decided to give it a try. I'm really very impressed with it and
like it a lot.
