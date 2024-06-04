# Event Newsletter Generator

This repository builds an `HTML` newsletter that can be shared via outlook.

The newsletter is built using a [`Jinja2`](https://palletsprojects.com/p/jinja/) template (`template.html.j2`), a configuration file (`config.yaml`) and a python script (`generate_newsletter.py`).

## How it works

- Every time a change is made in a branch (besides the main branch) the GH action will run the python code.
- Python script uses `jinja2` to read the config file and the template file to generate a html as output.

*Note: Important to give GH Actions write access.*

### Workflow

```bash
Create a new branch in this repo
            |
            |
            v
Update the configuration file
            |
            |
            v
Github action detects a change in 
the new branch and starts the action
            |  
            |
            v
Github action runs a python script 
that reads the configuration file and
uses variables to fill a jinja template
            |
            |
            v
Github action commits a new 
newsletter.html file as output.
```

## The Configuration File

The base configuration file (`config.yaml`) should look like:

```yaml
  title: "Title"
  heading: "Short heading"
  body: "This is the body of the advertising. Here you can put any information you want."

  events:
    - title: "Event 1"
      dates:
        - 2024-02-20
      tags:
        - "tag1"
        - "tag2"
      summary: "This is a summary of the event 1."
      url: "https://example.com/event1"
      
    - title: "Event 2"
      dates:
        - 2024-03-05
        - 2024-03-12
      tags:
        - "tag3"
        - "tag4"
        - "tag5"
      summary: "This is a summary of the event 2."
      url: "https://example.com/event2"
```

You can have as many events you want, and for each event you can also have as
many dates and tags as necessary. This is possible as the placeholder for this
information is under a for loop in the template html file.

## Backlog

Some things that can be further improved

- **Event grid**. In the moment the width of the grid is somehow set to auto. So depending on the Event description size, the blue box for calendar and date change the size. It would better find a better layout definition
- **Jinja2 GH Action?** I created a very standard python script for using jinja2. It should exist some equivalent GitHub Action to do this without the python script.
- **GH Action Warning:** Note.js is dreprecated, so it is necessary update the GH Action.
a
