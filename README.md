# podcrawler

What is the point of having 500 episodes of a podcast if only the 100 most recent are in the feed?

## Running the program

- Clone the repo
- Download the requirements listed in `requirements.txt`
- Add the environment variable for the root podcast URL. eg:

```sh
# .env
POD_URL=http://podcastwebsite.com
```
- Run the file from the command line. The program expects 3 arguments: starting index, ending index (not inclusive), and the output filename. eg:
```sh
python3 main.py 1 15 output-file.json
```

## Structure and Modularity

The main file takes the root URL `POD_URL` from the system environment, and tries to find all pages for a given range in the form `POD_URL/###` (where the ### are the numbers within the given range).

The get_data module provides the logic for extracting data from a given webpage. For different websites, it would be trivial to swap this module out with a different implementation, as long as the entrypoint takes HTML text and returns a JSON-serializable Dictionary.
