
FROM node:alpine as builder
WORKDIR '/app'

# Build the UI app ---------------------

COPY package.json .
RUN npm install
COPY . .
RUN npm run build

# For NginX server to serve the UI code -------------------

FROM nginx
EXPOSE 80
COPY ./nginx/default.conf /etc/nginx/conf.d/default.conf
COPY --from=builder /app/build /usr/share/nginx/html


# Enable following for development purposes -------------------
# --- not required since we are building inside a temporary container
# COPY ./build /usr/share/nginx/html