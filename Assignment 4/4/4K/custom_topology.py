#!/usr/bin/python

from mininet.net import Mininet
from mininet.node import Controller, RemoteController, OVSController
from mininet.node import CPULimitedHost, Host, Node
from mininet.node import OVSKernelSwitch, UserSwitch
from mininet.node import IVSSwitch
from mininet.cli import CLI
from mininet.log import setLogLevel, info
from mininet.link import TCLink, Intf
from subprocess import call
import time
import sys
def myNetwork():

    net = Mininet( topo=None,
                   build=False,
                   ipBase='10.0.0.0/8')

    info( '*** Adding controller\n' )
    c0=net.addController(name='c0',
                      controller=Controller,
                      protocol='tcp',
                      port=6633)

    info( '*** Add switches\n')
    s1 = net.addSwitch('s1', cls=OVSKernelSwitch)

    info( '*** Add hosts\n')
    client4 = net.addHost('client4', cls=Host, ip='10.0.0.5', defaultRoute=None)
    client1 = net.addHost('client1', cls=Host, ip='10.0.0.2', defaultRoute=None)
    server = net.addHost('server', cls=Host, ip='10.0.0.1', defaultRoute=None)
    client5 = net.addHost('client5', cls=Host, ip='10.0.0.6', defaultRoute=None)
    client2 = net.addHost('client2', cls=Host, ip='10.0.0.3', defaultRoute=None)
    client3 = net.addHost('client3', cls=Host, ip='10.0.0.4', defaultRoute=None)

    info( '*** Add links\n')
    net.addLink(server, s1)
    net.addLink(s1, client1)
    net.addLink(client2, s1)
    net.addLink(s1, client3)
    net.addLink(client4, s1)
    net.addLink(s1, client5)

    info( '*** Starting network\n')
    
    info( '*** Starting controllers\n')
    for controller in net.controllers:
        controller.start()

    info( '*** Starting switches\n')
    net.get('s1').start([c0])
    net.start()
    net.pingAll()
    info( '*** Post configure switches and hosts\n')
    server.cmd("python3.8 tcp_server_sc_fork.py -p 0 &")
    client1.cmd("python3.8 tcp_client_new.py -p 0 -i \"5\" &")
    client2.cmd("python3.8 tcp_client_new.py -p 0 -i \"5\" &")
    client3.cmd("python3.8 tcp_client_new.py -p 0 -i \"5\" &")
    client4.cmd("python3.8 tcp_client_new.py -p 0 -i \"5\" &")
    client5.cmd("python3.8 tcp_client_new.py -p 0 -i \"5\" &")
    #CLI(net)
    #net.stop()
    time.sleep(5)
    return

 
    
if __name__ == '__main__':
    setLogLevel( 'info' )
    myNetwork()

