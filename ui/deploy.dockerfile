FROM httpd:2.4.46
COPY classroom-bot-ui/build/. /usr/local/apache2/htdocs/
COPY .htaccess /usr/local/apache2/htdocs/
COPY httpd.conf /usr/local/apache2/conf/
CMD ["httpd-foreground"]
EXPOSE 80
