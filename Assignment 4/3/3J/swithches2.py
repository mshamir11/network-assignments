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
    s10 = net.addSwitch('s10', cls=OVSKernelSwitch)

    info( '*** Add hosts\n')
    server = net.addHost('server', cls=Host, ip='10.0.0.1', defaultRoute=None)
    client = net.addHost('client', cls=Host, ip='10.0.0.2', defaultRoute=None)

    info( '*** Add links\n')
    servers1 = {'bw':1000}
    net.addLink(server, s1, cls=TCLink , **servers1)
    s10client = {'bw':1000}
    net.addLink(s10, client, cls=TCLink , **s10client)
    s1s10 = {'bw':1000}
    net.addLink(s1, s10, cls=TCLink , **s1s10)

    info( '*** Starting network\n')
    net.build()
    info( '*** Starting controllers\n')
    for controller in net.controllers:
        controller.start()

    info( '*** Starting switches\n')
    net.get('s1').start([c0])
    net.get('s10').start([c0])

    info( '*** Post configure switches and hosts\n')

    CLI(net)
    net.stop()

if __name__ == '__main__':
    setLogLevel( 'info' )
    myNetwork()

