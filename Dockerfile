FROM python

# We copy just the requirements.txt first to leverage Docker cache
COPY ./requirements.txt /app/requirements.txt

WORKDIR /app

RUN pip install -r requirements.txt

COPY . /app

ENV FLASK_APP=app/accountPage.py
ENV FLASK_ENV=development

CMD [ "python", "app/accountPage.py" ]