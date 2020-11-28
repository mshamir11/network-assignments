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
    s4 = net.addSwitch('s4', cls=OVSKernelSwitch)
    s1 = net.addSwitch('s1', cls=OVSKernelSwitch)
    s5 = net.addSwitch('s5', cls=OVSKernelSwitch)
    s6 = net.addSwitch('s6', cls=OVSKernelSwitch)
    s3 = net.addSwitch('s3', cls=OVSKernelSwitch)
    s2 = net.addSwitch('s2', cls=OVSKernelSwitch)
    s7 = net.addSwitch('s7', cls=OVSKernelSwitch)

    info( '*** Add hosts\n')
    L = net.addHost('L', cls=Host, ip='10.0.0.6', defaultRoute=None)
    K = net.addHost('K', cls=Host, ip='10.0.0.5', defaultRoute=None)
    server = net.addHost('server', cls=Host, ip='10.0.0.1', defaultRoute=None)
    O = net.addHost('O', cls=Host, ip='10.0.0.9', defaultRoute=None)
    N = net.addHost('N', cls=Host, ip='10.0.0.8', defaultRoute=None)
    J = net.addHost('J', cls=Host, ip='10.0.0.4', defaultRoute=None)
    H = net.addHost('H', cls=Host, ip='10.0.0.2', defaultRoute=None)
    I = net.addHost('I', cls=Host, ip='10.0.0.3', defaultRoute=None)
    M = net.addHost('M', cls=Host, ip='10.0.0.7', defaultRoute=None)

    info( '*** Add links\n')
    s1s2 = {'bw':40}
    net.addLink(s1, s2, cls=TCLink , **s1s2)
    s2s4 = {'bw':20}
    net.addLink(s2, s4, cls=TCLink , **s2s4)
    s2s5 = {'bw':20}
    net.addLink(s2, s5, cls=TCLink , **s2s5)
    s4H = {'bw':10}
    net.addLink(s4, H, cls=TCLink , **s4H)
    s4I = {'bw':10}
    net.addLink(s4, I, cls=TCLink , **s4I)
    s5J = {'bw':10}
    net.addLink(s5, J, cls=TCLink , **s5J)
    s5K = {'bw':10}
    net.addLink(s5, K, cls=TCLink , **s5K)
    s6L = {'bw':10}
    net.addLink(s6, L, cls=TCLink , **s6L)
    s6M = {'bw':10}
    net.addLink(s6, M, cls=TCLink , **s6M)
    s7N = {'bw':10}
    net.addLink(s7, N, cls=TCLink , **s7N)
    s7O = {'bw':10}
    net.addLink(s7, O, cls=TCLink , **s7O)
    s1server = {'bw':40}
    net.addLink(s1, server, cls=TCLink , **s1server)
    s1s3 = {'bw':40}
    net.addLink(s1, s3, cls=TCLink , **s1s3)
    s3s6 = {'bw':20}
    net.addLink(s3, s6, cls=TCLink , **s3s6)
    s3s7 = {'bw':20}
    net.addLink(s3, s7, cls=TCLink , **s3s7)

    info( '*** Starting network\n')
    net.build()
    info( '*** Starting controllers\n')
    for controller in net.controllers:
        controller.start()

    info( '*** Starting switches\n')
    net.get('s4').start([c0])
    net.get('s1').start([c0])
    net.get('s5').start([c0])
    net.get('s6').start([c0])
    net.get('s3').start([c0])
    net.get('s2').start([c0])
    net.get('s7').start([c0])

    info( '*** Post configure switches and hosts\n')

    CLI(net)
    net.stop()

if __name__ == '__main__':
    setLogLevel( 'info' )
    myNetwork()

