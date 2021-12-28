# base that include lamdba runtime api
FROM public.ecr.aws/lambda/python:3.8

LABEL Maintainer="Korey Hayes"

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

CMD [ "search.search" ]