#docker build -t go_test -f ./Dockerfile .
#docker run -d -p 9000:9000 go_test:latest
FROM golang:alpine as build

WORKDIR /opt/app

EXPOSE 9000

COPY . .

RUN CGO_ENABLED=0 GOOS=linux go build -o hello main.go

#second step 
FROM scratch
WORKDIR /opt/app

COPY --from=build /opt/app /opt/app/

CMD [ "./hello" ]
