# EmailCalendarPlotter

This process creates a dynamic calendar system that fetches email invites, processes them into calendar events, and displays them in a color-coded, interactive web interface. The system uses environment variables for secure credential management and leverages various Python libraries for email processing, calendar operations, and HTML generation.


```mermaid
graph TD
    A[User] -->|Enters URL| B[Apache Web Server]
    A -->|Enters credentials| C[Apache Authentication]
    C -->|Authenticates| D[CGI Script cgi.py]
    D -->|Executes| E[Python Environment]
    
    subgraph "Python Scripts"
        E -->|Imports| F[accept.py]
        F -->|Connects to| G[IMAP Server]
        F -->|Connects to| H[CalDAV Server]
        G -->|Fetches emails| F
        F -->|Processes invites| H
        
        E -->|Imports| I[get_cal_events.py]
        I -->|Imports data from| F
        I -->|Fetches events| H
        I -->|Processes event details| J[Event Data]
        
        E -->|Imports| K[make_html.py]
        K -->|Imports data from| I
        K -->|Loads| L[Jinja2 Template]
        K -->|Renders template| M[Generated HTML]
    end
    
    M -->|Sends| N[CGI Output]
    N -->|Displays in| O[User's Browser]
    
    subgraph "Data Flow"
        P[Environment Variables] -.->|Provides credentials| F
        Q[email_credentials.json] -.->|Alternative credentials| F
        R[User Dictionary] -.->|Stores user info| I
        S[Event List] -.->|Stores event data| K
        T[Color Assignment] -.->|Assigns colors to events| I
    end
    
    subgraph "File Structure"
        U[accept.py]
        V[cgi.py]
        W[get_cal_events.py]
        X[make_html.py]
        Y[calendar.conf]
        Z[template.jinja]
    end
    ```

## Detailed explanation of each step:

### User Interaction:

User enters the URL (calendar.wcrp-cmip.org) in their browser
Apache prompts for authentication
User enters username and password


### Apache Web Server:

Handles the incoming request
Authenticates the user using the .htpasswd file
If authenticated, passes control to the CGI script


### CGI Script (cgi.py):

Sets up the Python environment
Prints the Content-Type header
Imports and runs make_html.py


### Python Environment:

Executes the Python scripts in the following order:


### accept.py:

Connects to the IMAP server using credentials from environment variables
Fetches emails from the inbox
Connects to the CalDAV server
Processes calendar invites from emails and adds them to the calendar


### get_cal_events.py:

Imports functions and data from accept.py
Fetches events from all calendars
Processes event details (summary, start/end times, organizer)
Assigns colors to events based on the organizer's email
Prepares event data for display


### make_html.py:

Imports event data from get_cal_events.py
Loads the Jinja2 template (template.jinja)
Renders the template with the event data and color keys
Prints the generated HTML


### Generated HTML:

The fully rendered HTML calendar is sent back through the CGI script


### User's Browser:

Receives the HTML content
Renders and displays the calendar to the user


