FROM nginx:1.15.9

RUN rm /etc/nginx/nginx.conf
COPY nginx/nginx.conf /etc/nginx/

RUN rm /etc/nginx/conf.d/default.conf
COPY nginx/thea.conf /etc/nginx/conf.d/

COPY nginx/static ./static
