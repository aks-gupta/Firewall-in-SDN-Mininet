

"""
Firewall based SDN network
"""
from mininet.topo import Topo
from mininet.net import Mininet
from mininet.util import dumpNodeConnections
from mininet.log import setLogLevel
from mininet.node import RemoteController
from mininet.cli import CLI
#import iperf3

class SingleSwitchTopo(Topo):
    "Single switch connected to n hosts."
    def build(self, n=2):
        switch = self.addSwitch('s1', dpid="00000000000007")
        # Python's range(N) generates 0..N-1
        for h in range(n):
            host = self.addHost('h%s' % (h + 1), ip='10.0.0.%s' % (h+1), mac='00:00:00:00:00:0%s' % (h+1))
            self.addLink(host, switch,bw=200,delay='0ms',loss=0,max_queue_size=1000)

def simpleTest():
    "Create and test a simple network"
    topo = SingleSwitchTopo(n=4)
    net = Mininet(topo, controller=None)
    " Remote POX Controller"
    c = RemoteController('c', '0.0.0.0', 6633)
    h1,h2,h3,h4 = net.get('h1','h2','h3','h4')
    net.addController(c)
    net.start()
    print("Dumping host connections")
    dumpNodeConnections(net.hosts)

    net.ping((h2,h4))   
    net.ping((h1,h4))
    net.iperf([h3,h1], seconds = 2, port = 80)
    net.iperf([h3,h1], seconds = 2, port = 22)
    
    net.pingFull()
   
    CLI(net)
    net.stop()

if __name__ == '__main__':
    # Tell mininet to print useful information
    setLogLevel('info')
    simpleTest()
