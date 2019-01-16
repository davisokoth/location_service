# location_service

## Development

### Basic set up

Build the image:

```bash
docker-compose build
```

Run the web server:

```bash
docker-compose up
```

Open your browser with URL `http://localhost:8080`. For the admin panel
`http://localhost:8080/admin` (user: `admin`, password: `admin`).

The documentation can be consulted in `http://localhost:8080/docs`.

### Development utils

Run the tests only once:

```bash
docker-compose run --rm --entrypoint 'bash scripts/run-tests.sh' location_service
```

Run the tests and leave bash open inside the container, so it's possible to
re-run the tests faster again using `bash scripts/run-tests.sh [--keepdb]`:

```bash
docker-compose run --rm --entrypoint 'bash scripts/run-tests.sh --bash-on-finish' location_service
```

To run bash:

```bash
docker-compose run --rm --entrypoint 'bash' location_service
```

If you would like to clean the database and start the application, do:

```bash
docker-compose up --renew-anon-volumes --force-recreate --build
```
