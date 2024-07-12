

from jinja2 import Environment, FileSystemLoader

from get_cal_events import events,keys
# print()
# print(events)

'''
# Define data to be inserted into the template
events = [
      {
        "title": 'Meeting 4',
        "start": '2024-06-12T14:30:00',
        "end": '2024-06-12T14:50:00',
        "color":'green'
      },
      {
        "title": 'Birthday Party',
        "start": '2024-06-13T07:00:00'
      },
      {
        "title": 'Click for Google',
        "url": 'https://google.com/',
        "start": '2024-06-28'
      }
    ]
'''


# Initialize Jinja2 environment to load templates from the current directory
env = Environment(loader=FileSystemLoader('.'))

# Load the template
template = env.get_template('template.jinja')

# R"end"er the template with data
output = template.render(events=events,keys=keys)

print(output)

# Write the r"end"ered output to a file
#with open('output.html', 'w') as f:
#    f.write(output)




