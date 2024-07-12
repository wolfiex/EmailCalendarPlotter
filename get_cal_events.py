
from accept import * 
from icalendar import Calendar
from datetime import datetime
from colour import * 

all_colours = list(colors.values())[::20]+list(colors.values())[10::20]+list(colors.values())[4::20]+list(colors.values())[14::20]

names = []

def fixdate(date):
    return datetime.combine(date, datetime.min.time()).strftime('%Y-%m-%dT%H:%M:%S')

# Fetch events
events = []
for calendar in calendars:
    for event in calendar.events():
        event_data = event.data
        calendar_event = Calendar.from_ical(event_data)
        for component in calendar_event.walk():
            if component.name == "VEVENT":
                event_details = {
                    'summary': component.get('SUMMARY'),
                    'dtstart': component.decoded('DTSTART'),
                    'dtend': component.decoded('DTEND'),
                    'location': component.get('LOCATION'),
                    'description': component.get('ORGANIZER'),
                }
                
                email = str(component.get('ORGANIZER')).replace('MAILTO:','').replace('mailto:','')
                # print(email)
                if email not in names:
                    names.append(email)
                    
                
                events.append({
                    'title': f"{user[email]} - {event_details['summary']}",
                    'start': fixdate(event_details['dtstart']),
                    'end': fixdate(event_details['dtend']),
                    'color': all_colours[names.index(email)]
                })

# Sort events by start date
events.sort(key=lambda x: x['start'])

newnames = [f"{user[name]} - {name}" for name in names]

keys = dict(zip(newnames,all_colours))


# some filter here?


