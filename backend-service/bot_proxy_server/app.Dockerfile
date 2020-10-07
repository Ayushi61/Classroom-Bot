FROM python:3.7.9-stretch

RUN mkdir /bot_proxy_server
COPY ./ bot_proxy_server/
WORKDIR /bot_proxy_server
RUN mkdir ./static/
RUN chmod +x execute.sh
RUN pip3 install -r requirements.txt
CMD ["./execute.sh"]
