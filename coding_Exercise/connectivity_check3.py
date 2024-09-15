# Example
# -------
#
#   connectivity_check.py

from pyats import aetest
import re
import logging

class CommonSetup(aetest.CommonSetup):

    @aetest.subsection
    def check_topology(self,
                       testbed,
                       ios1_name = 'WWT-ATP-CIN'):
        ios1 = testbed.devices[ios1_name]


        # add them to testscript parameters
        self.parent.parameters.update(ios1 = ios1)

        # get corresponding links


    @aetest.subsection
    def establish_connections(self, steps, ios1):
        with steps.start('Connecting to %s' % ios1.name):
            ios1.connect()

class TESTCASE_1_PING_FROM_CIN_CBR8(aetest.Testcase):

    @aetest.test
    def T1_PING_FROM_CIN_TO_CBR8(self, ios1):
        try:
            result = ios1.execute('ping 10.233.1.8')
        except Exception as e:
            self.failed('Something go wrong'.format(str(e)), goto = ['exit'])
        else:
            match = re.search('timeout', result) or re.search('host unreachable', result)
            print('################')
            print('Result is =>', result)
            print('Math is =>', match)
            print('################')
            if match:
                print('Math is => FIND', match)
                print('################')
                self.failed()
            else:
                print('Slot 0, Port 0 is unreachable')
                print('################')


class CommonCleanup(aetest.CommonCleanup):

    @aetest.subsection
    def disconnect(self, steps, ios1):
        with steps.start('Disconnecting from %s' % ios1.name):
            ios1.disconnect()


if __name__ == '__main__':
    import argparse
    from pyats.topology import loader

    parser = argparse.ArgumentParser()
    parser.add_argument('--testbed', dest = 'testbed',
                        type = loader.load)

    args, unknown = parser.parse_known_args()

    aetest.main(**vars(args))
