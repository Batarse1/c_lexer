FROM python

WORKDIR /app

RUN pip install ply
RUN pip install prettytable

COPY . /app

CMD [ "python", "main.py" ]