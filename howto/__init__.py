from __future__ import unicode_literals

from contrail_api_cli.commands import Command, Arg


class Hello(Command):
    description = 'Hello world command'
    who = Arg(nargs='?', default='cli', help='Person to greet')

    def __call__(self, who):
        return 'Hello world %s !' % who
