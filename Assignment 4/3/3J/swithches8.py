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
    s2 = net.addSwitch('s2', cls=OVSKernelSwitch)
    s4 = net.addSwitch('s4', cls=OVSKernelSwitch)
    s3 = net.addSwitch('s3', cls=OVSKernelSwitch)
    s10 = net.addSwitch('s10', cls=OVSKernelSwitch)
    s7 = net.addSwitch('s7', cls=OVSKernelSwitch)
    s9 = net.addSwitch('s9', cls=OVSKernelSwitch)
    s8 = net.addSwitch('s8', cls=OVSKernelSwitch)

    info( '*** Add hosts\n')
    server = net.addHost('server', cls=Host, ip='10.0.0.1', defaultRoute=None)
    client = net.addHost('client', cls=Host, ip='10.0.0.2', defaultRoute=None)

    info( '*** Add links\n')
    servers1 = {'bw':1000}
    net.addLink(server, s1, cls=TCLink , **servers1)
    s1s2 = {'bw':1000}
    net.addLink(s1, s2, cls=TCLink , **s1s2)
    s2s3 = {'bw':1000}
    net.addLink(s2, s3, cls=TCLink , **s2s3)
    s3s4 = {'bw':1000}
    net.addLink(s3, s4, cls=TCLink , **s3s4)
    s7s8 = {'bw':1000}
    net.addLink(s7, s8, cls=TCLink , **s7s8)
    s8s9 = {'bw':1000}
    net.addLink(s8, s9, cls=TCLink , **s8s9)
    s9s10 = {'bw':1000}
    net.addLink(s9, s10, cls=TCLink , **s9s10)
    s10client = {'bw':1000}
    net.addLink(s10, client, cls=TCLink , **s10client)
    s4s7 = {'bw':1000}
    net.addLink(s4, s7, cls=TCLink , **s4s7)

    info( '*** Starting network\n')
    net.build()
    info( '*** Starting controllers\n')
    for controller in net.controllers:
        controller.start()

    info( '*** Starting switches\n')
    net.get('s1').start([c0])
    net.get('s2').start([c0])
    net.get('s4').start([c0])
    net.get('s3').start([c0])
    net.get('s10').start([c0])
    net.get('s7').start([c0])
    net.get('s9').start([c0])
    net.get('s8').start([c0])

    info( '*** Post configure switches and hosts\n')

    CLI(net)
    net.stop()

if __name__ == '__main__':
    setLogLevel( 'info' )
    myNetwork()

