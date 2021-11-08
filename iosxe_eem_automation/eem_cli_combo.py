import cli

eem = '''
event manager applet upgrade
event none maxrun 400
action 1.0 cli command "enable"
action 2.0 cli command "request platform software package expand file bootflash:cbrsup-universalk9.16.12.01z.SPA.bin to bootflash:/XE-1612-1z/ wipe" '''

cli.configurep(eem)

request = "event manager run upgrade"
cli.executep(request)
