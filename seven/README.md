# Seven

## Build the container

```bash
docker build -t seven .
```

## Running the script
```bash
docker run --rm --name seven -it seven --help
```

### Upload file

```bash
docker run \
    --rm \ 
    --name seven \
    -v <path_of_credentials_out>:<path_of_credentials_in> \
    -v <path_of_file_out>:<path_of_file_in> \
    -it seven upload -f <path_of_file_in>/file_to_upload -c <path_of_credentials_in>/credentials.json
```