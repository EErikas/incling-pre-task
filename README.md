# Pre-Interview Task

## Project Set Up
The project is implemented using Django and uses the PostgreSQL database.
The required environment variables are provided in the `project.env` file and if used in production, their values should be changed

## Launching the Project
To launch the project, enter the following command:
```bash
docker compose up
```

## Routes
The routes are as follows:
* `/api/tasks/`: API endpoint for adding Tasks
* `/api/tiles/`: API endpoint for adding Tiles
* `/admin`: Admin site, the credentials for admin user are provided in the environment variables called `DJANGO_SUPERUSER_USERNAME`, `DJANGO_SUPERUSER_EMAIL`, `DJANGO_SUPERUSER_PASSWORD` which are provided in `project.env` file