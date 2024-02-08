---
default_file: 01-basics.pdf
---
- ISPs are connected through "Internet Exchange Points"
	- That's how different ISPs(VodaFone, Three, Eir) can all  connect to each other
```slide-note
page: 67
```
- If the buffer is full, and a packet arrives, the packet gets lost
- Only dealing with packet-switching now
```slide-note
page: 68
```
- Processing delays are inconceivably low (under a millisecond) 
- Queueing delay can be estimated using queue theory
```slide-note
file: 01-basics.pdf
page: 69
```
- Fibre cables have a propagation speed of 2x10^8 m/s(speed of light)
- Transmission delay is the amount of time it takes to gather the bits and put them onto the link
	- Meanwhile the propagation delay is the amount of time it takes to travel the link
	- Very often confused
- https://computerscience.unicam.it/marcantoni/reti/applet/TransmissionVsPropagationDelay/traProp.html
- If distances are short, propagation delays are negligible
- If packet size is small, transmission delay doesn't matter much
- If you have large packets, getting a high transmission *rate* is important
```slide-note
page: 70
```
```slide-note
page: 71
```
```slide-note
page: 72
```
- Queueing theory is used to work out the length given to the packet queue when congestion is high
