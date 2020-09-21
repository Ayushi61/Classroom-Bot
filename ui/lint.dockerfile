FROM node:10
RUN mkdir app
COPY /classroom-bot-ui/. app/
RUN cd app/  && \
    npm install && \
    npm install -g eslint
CMD ["eslint", "app/src/"]