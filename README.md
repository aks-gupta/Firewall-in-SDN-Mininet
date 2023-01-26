# Firewall-in-SDN-Mininet

Install mininet using sudo install mn

Install pox from their website

## Installing
There are two scripts namely, mininetScript.py and poxController_firewall.py which will run the mininet based ovsSwitch and POX Controller respectively.

Add the pox_firewall controller to the pox directory and run with the command

```
./pox.py log.level --INFO poxController_firewall
```

Run the mininet script with root privileges

```
python mininetScript.py
```

## Firewall Rules installed in the controller
* Layer-2 Link connection blocked  
  Block all traffic from Host-h2  
  ```
  AddRule(dataPath_id, 00:00:00:00:00:02, NULL, NULL, NULL)
  ```
* Layer-3 Host-to-Host Connectivity blocked  
  Block all traffic from Host-h1 to Host-h4  
  ```
  AddRule(dataPath_id, NULL, 10.0.0.1, 10.0.0.4, NULL)
  ```
* Layer-4 Destination Process blocked  
  Block all traffic destined to Process h3 at port 80  
  ```
  AddRule(dataPath_id, NULL, NULL, 10.0.0.3, 80)
  ```

## Running the Tests
* Layer-2 Link connection blocked  
  ```
  h2 ping h4
  ```
 * Output: The ARP L2-packets will be dropped by the Controller.

* Layer-3 Host-to-Host Connectivity blocked  
  ```
  h1 ping h4
  ```
 * Output: The IP Layer-packets will be dropped by the Controller.

* Layer-4 Destination Process blocked  
 * Run two IPerf servers on Host-h3  
   ```
   h3 iperf -s -p 80 &
   
   h3 iperf -s -p 22 &
   ```
 * Connect to both the servers  
   ```
   h1 iperf –c h3 –p 80 –t 2 –i 1
   
   h1 iperf –c h3 –p 22 –t 2 –i 1
   ```
 * Output: All TCP-traffic to Destination h3 and port 80 are dropped by the Controller.


