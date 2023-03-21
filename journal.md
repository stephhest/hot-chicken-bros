# Notes / Reminders:

## PG ADMIN
On the second tab, "Connection", add the "Host name/address", "Username", and the "Password".

- "Host name/address" is the name of the service that runs your PostgreSQL database in your docker-compose.yml file, like db
- "Username" is the name of the database user, usually specified by the `POSTGRES_USER` environment variable, like trivia-game
- "Password" is the password for the database user, usually specified by the `POSTGRES_PASSWORD` environment variable, like trivia-game
- Enable "Save password?" if you don't want to have to type the password every time you want to connect


## React
Use the following for API calls from the frontend:
```javascript
  const url = `${process.env.REACT_APP_USERS_API_HOST}/api/users`;
  const response = await fetch(url);
```

## Docker
Use the following command to build containers:
  `DOCKER_DEFAULT_PLATFORM=linux/amd64 docker-compose build`


## Migrations
Take the following steps when modifying the structure of the database:
1. Stop / tear down the containers with `docker-compose down`
2. Delete current db volume with `docker volume rm postgres-hcb-data`
3. Modify the migrations files as needed
4. Recreate the db volume with `docker volume create postgres-hcb-data`
5. Rebuild the containers with `DOCKER_DEFAULT_PLATFORM=linux/amd64 docker-compose build`
6. Restart the containers with `docker-compose up`
IF errors still occur, add the following to the above steps:
  3a. Before recreating volume, delete corresponding images
  3b. Delete the compiled migrations by deleting the __pycache__ folder in each migrations directory
