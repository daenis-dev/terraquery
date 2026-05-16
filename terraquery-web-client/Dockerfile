FROM node:20-alpine

WORKDIR /app

RUN npm install -g http-server

COPY . .

EXPOSE 4200

CMD ["http-server", ".", "-p", "4200", "--cors"]