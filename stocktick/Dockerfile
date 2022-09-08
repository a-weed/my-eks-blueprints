FROM python:3

ADD requirements.txt /

RUN pip install -r requirements.txt

ADD stockWatcher.py /

CMD ["pthon", "./stockWatcher.py"]