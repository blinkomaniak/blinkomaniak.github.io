---
# the default layout is 'page'
icon: fas fa-info-circle
order: 1
---

<!-- > Add Markdown syntax content to file `_tabs/about.md`{: .filepath } and it will show up on this page. -->
<!-- {: .prompt-tip } -->

## Virtual network implementation for research idea.

![alt text](/assets/images/network_implementation.png)

**Description**

Three hosts with Linux-based OS. Each host has an IPv4 address in the range 114.71.51.0/24:
- Server 1 is 114.71.51.39/24
- Server 2 is 114.71.51.41/24
- Server 3 is 114.71.51.43/24

Each Server will host different sub-networks composed by virtual machines, virtual switches, and virtual routers. To communicate these sub-networks between each other and to provide internet access to these sub-networks, each of the virtual routers' WAN interface should be in 'Bridge' mode. For the 'Bridge' mode to work properly, it will be necessary to assign an IPv4 address from the same network range as the IPv4 addresses of each host, in the range 114.71.51.0/24.

Another solution can be to set the router's WAN interface in 'NAT' mode. However, more complex configuration is needed. 'Bridge' mode is the simplest guaranteed strategy to provide external-network access to the sub-networks.