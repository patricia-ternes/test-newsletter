import yaml
from jinja2 import Environment, FileSystemLoader

# Load the configuration file
with open('config.yaml', 'r') as file:
    config = yaml.safe_load(file)

# Load the Jinja2 template
env = Environment(loader=FileSystemLoader('.'))
template = env.get_template('template.html.j2')

# Render the template with the configuration data
output = template.render(config)

# Write the rendered output to a file
with open('newsletter.html', 'w') as file:
    file.write(output)
