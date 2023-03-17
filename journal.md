# Notes / Reminders:

## PG ADMIN
On the second tab, "Connection", add the "Host name/address", "Username", and the "Password".

- "Host name/address" is the name of the service that runs your PostgreSQL database in your docker-compose.yml file, like db
- "Username" is the name of the database user, usually specified by the POSTGRES_USER environment variable, like trivia-game
- "Password" is the password for the database user, usually specified by the POSTGRES_PASSWORD environment variable, like trivia-game
- Enable "Save password?" if you don't want to have to type the password every time you want to connect


## React

Use the following for API calls from the frontend:
  const url = `${process.env.REACT_APP_USERS_API_HOST}/api/users`;
  const response = await fetch(url);
