FROM node:10
RUN mkdir app
COPY /classroom-bot-ui/. /app
RUN cd app/  && ls && npm install
WORKDIR /app
CMD ["npm", "test"]