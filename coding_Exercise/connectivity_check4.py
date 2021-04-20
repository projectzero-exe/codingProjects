# Example
# -------
#
#   connectivity_check.py

from pyats import aetest
import re
import logging

# get your logger for your script
logger = logging.getLogger(__name__)

class CommonSetup(aetest.CommonSetup):

    @aetest.subsection
    def check_topology(self,
                       testbed,
                       ios1_name = 'WWT-ATP-CIN'):
        ios1 = testbed.devices[ios1_name]

        # add them to testscript parameters
        self.parent.parameters.update(ios1 = ios1)




    @aetest.subsection
    def establish_connections(self, steps, ios1):
        with steps.start('Connecting to %s' % ios1.name):
            ios1.connect()


@aetest.loop(device = ('ios1'))

class PingTestcase(aetest.Testcase):

    @aetest.test.loop(destination = ('10.233.1.8'))
    def ping(self, device, destination):
        try:
            result = self.parameters[device].ping(destination)

        except Exception as e:
            self.failed('Ping {} from device {} failed with error: {}'.format(
                                destination,
                                device,
                                str(e),
                            ),
                        goto = ['exit'])
        else:
            match = re.search(r'Success rate is (?P<rate>\d+) percent', result)
            success_rate = match.group('rate')

            logger.info('Ping {} with success rate of {}%'.format(
                                        destination,
                                        success_rate,
                                    )
                               )

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
