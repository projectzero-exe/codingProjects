# Example
# -------
#
#   an example testbed file - ios_testbed.yaml

testbed:
    name: IOS_Testbed
    tacacs:
        username: admin
    passwords:
        tacacs: cisco
        enable: cisco

devices:
    ios-1: # <----- much match to your device hostname in the prompt
        os: ios
        type: ios
        connections:
            a:
                protocol: telnet
                ip: 1.1.1.1
                port: 11023
    ios-2:
        os: ios
        type: ios
        connections:
            a:
                protocol: telnet
                ip: 1.1.1.2
                port: 11024
            vty:
                protocol: ssh
                ip: 5.5.5.5
topology:
    ios-1:
        interfaces:
            GigabitEthernet0/0:
                ipv4: 10.10.10.1/24
                ipv6: '10:10:10::1/64'
                link: link-1
                type: ethernet
            Loopback0:
                ipv4: 192.168.0.1/32
                ipv6: '192::1/128'
                link: ios1_Loopback0
                type: loopback
    ios-2:
        interfaces:
            GigabitEthernet0/0:
                ipv4: 10.10.10.2/24
                ipv6: '10:10:10::2/64'
                link: link-1
                type: ethernet
            Loopback0:
                ipv4: 192.168.0.2/32
                ipv6: '192::2/128'
                link: ios2_Loopback0
                type: loopback
