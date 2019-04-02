# Nine

## Build the container
```
docker build -t nine .
```

## Running the script
```
docker run --rm --name nine -it nine --help
```


### Create pdf output.pdf from file file.csv
```
docker run --rm -v $PWD:$PWD --name nine -it nine read -f $PWD/file.csv -p $PWD/output.pdf
```
