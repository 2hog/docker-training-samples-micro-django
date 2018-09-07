FROM node:10.9 as builder

ARG APP_DIR=training/web/static/web
WORKDIR /usr/src/app

# Install packages
COPY package.json yarn.lock ./
COPY ${APP_DIR}/package.json ${APP_DIR}/yarn.lock ./${APP_DIR}/
RUN yarn

# Build things
COPY ${APP_DIR} ./${APP_DIR}/
RUN yarn heroku-postbuild

FROM python:3.6

RUN pip install pipenv

WORKDIR /usr/src/app

COPY Pipfile Pipfile.lock ./
RUN pipenv install --system --deploy

COPY . .
COPY --from=builder /usr/src/app/training/web/static/web/dist/ /usr/src/app/training/web/static/web/dist/

CMD ["./bin/migrate-and-serve"]