# test-newsletter

Repository to test actions for creating a newsletter based in a html template. Once it is working, this will be replicated into ARCleeds orgs

## How it works

Every time a change is made in a branch (besides the main branch) the action will run the python code.

Python script uses jinja2 to read the config file and the template file to generate a html as output.

Note: Important to give write access for actions.
