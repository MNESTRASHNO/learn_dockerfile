FROM nginx:alpine

WORKDIR /usr/share/nginx/html 

EXPOSE 8080

COPY default.conf /etc/nginx/conf.d/default.conf

COPY . /usr/share/nginx/html

CMD ["nginx", "-g", "daemon off;"]
