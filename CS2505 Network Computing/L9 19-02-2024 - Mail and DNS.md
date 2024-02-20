---
default_file: Lecturers Notes/02-app-layer.pdf
---
```slide-note
page: 57
```
- User agent would be the interface to interact with, read and write emails
	- The main gmail page would be a user agent
```slide-note
page: 58-65
```
- POP downloads your messages, you don't have an inbox stored on a server
	- Designed for if you disconnect from the internet
```slide-note
page: 67
```
- IMAP and POP3 is an access protocol, meaning it's what gets your emails.
	- SMTP only sends

```slide-note
page: 69
```
- DNS maps names to ip addresses
	- Makes it much easier to remember the names of sites
	- 204.325.64.21 could become "www.google.ie"
- Back in the day, it would just be one file in each computer with the two columns, "name" and "address"
	- Very hard to update
	- Bad
```slide-note
page: 70
```
- DNS allows for load balancing by allowing multiple ip addresses to one name
	- For example, google has multiple machines, but still only one hostname
```slide-note
page: 71
```
- Hosts manage their own DNS servers (known as local name server)
- Normally, clients don't go to the root DNS server, they go their own local name server
	- It's cached
```slide-note
page: 72-75
```
- Caching is performed in all servers
	- Not just the local DNS server
- This diagram is the worst case
	- Likely a lot better due to caching
```slide-note
page: 76
```
- This is worse because of the stateful nature of the requests
	- Each DNS server must keep state of the connection
	- Puts a lot of load onto the DNS servers

```slide-note
page: 77
```
- Consistency is an issue with caching
