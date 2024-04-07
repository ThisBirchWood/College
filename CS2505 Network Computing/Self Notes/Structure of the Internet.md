# Network Edge

## What does it contain?
- End Systems (hosts)
	- applications, web, email
- Client/Server Models
	- Web browsers/server; email client/server
- Peer-to-peer model
	- Skype, Teams, BitTorrent

## Data Rate
 - Amount of data that can be transmitted per time unit over a link

- The term **bandwidth** refers to the amount of frequency spectrum available on a communication link, which is related to data rate
## Access networks
- Access networks are part of a telecommunications network that connects the end-users to the **core network** or the ISP's infrastructure.
- These access network systems connect the end users to the greater internet

- Examples:
### Dial-up Modem
- Runs on the telephone lines, which technically only support sound
- Translates your bits to sound, which causes that funny noise
- Max speed of 56Kb/s
### Digital subscriber line (DSL)
- Uses the telephone line as well
- Uses a different radio frequency, so data rates are higher
### Cable Modem
- Internet access can be delivered over coaxial cables originally built for cable television
### Fiber to the Home (FTTH)
![[Pasted image 20240326164723.png]]
 - Optical links from *central office* to homes
 - Very high data rates, can also carry television and phone services
### Wireless Local Area Networks
- Typically what we know as "WiFi"
- Range of around 30m
### Wide-Area Cellular Networks
- Mobile data, 4G/5G
- Provided by mobile network operators
- Range of 1-100km
	- Depending on obstacles and population density

## Physical Media
### Twisted Pair
- two insulated copper wires
- this is an ethernet cable
### Coaxial cable
- bidirectional
- multiple frequency channels on cable
- 100's Mbps per channel
### Fiber Optic Cable
- Glass fiber carrying light pulses
- very fast
	- 10s to 100s Gbps
- low error rate
	- repeaters spaced far apart

### Wireless radio
- signal carried in electromagnetic spectrum
- Types:
	- terrestrial microwave
	- WiFi
	- wide-area cellular
	- satellite (270ms end-end delay (bad!))


# Network Core
- Mesh of interconnected routers
- How is data transferred through the network?
	- **Circuit Switching**: dedicated circuit per call
	- **Packet Switching**: data is sent through the network in packets
		- Each packet is transmitted at full speed

## Circuit Switching
