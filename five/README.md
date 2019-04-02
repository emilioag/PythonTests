# five

Get tweets

## Build the container

```bash
docker build -t five .
```

## Setting up the environment

```bash
docker run --rm --name rethink -p 28015:28015 -p 29015:29015 -p 8080:8080 -d rethinkdb:2
```

## Running the script

```bash
docker run -v <volume-out>:<volume-in> --link rethink:rethink -it five get -u twitter_user -p <volume-in>/outputfile.pdf
```

### Environment variables

| VARIABLE         | DEFAULT                     |
|------------------|-----------------------------|
| RETHINK_HOST     | rethink                     |
| RETHINK_PORT     | 28015                       |
| TWITTER_BEARER   | 8798787898                  |
| TWITTER_BASE_URL | https://api.twitter.com/1.1 |
