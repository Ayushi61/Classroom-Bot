FROM python:3.7.9-stretch

RUN mkdir /bot_proxy_server
COPY bot_proxy_server/ bot_proxy_server/
COPY execute-proxy.sh /bot_proxy_server/execute-proxy.sh
WORKDIR /bot_proxy_server
RUN mkdir ./static/
RUN chmod +x execute-proxy.sh
RUN pip3 install -r requirements.txt
CMD ["./execute-proxy.sh"]
