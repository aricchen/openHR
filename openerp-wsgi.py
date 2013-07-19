
#!/usr/bin/python
# WSGI Handler sample configuration file.
#
# Change the appropriate settings below, in order to provide the parameters
# that would normally be passed in the command-line.
# (at least conf['addons_path'])
#
# For generic wsgi handlers a global application is defined.
# For uwsgi this should work:
#   $ uwsgi_python --http :9090 --pythonpath . --wsgi-file openerp-wsgi.py
#
# For gunicorn additional globals need to be defined in the Gunicorn section.
# Then the following command should run:
#   $ gunicorn openerp:service.wsgi_server.application -c openerp-wsgi.py
import openerp

#----------------------------------------------------------
 # Common
#----------------------------------------------------------
openerp.multi_process = True # Nah!

# Equivalent of --load command-line option
openerp.conf.server_wide_modules = ['web']
conf = openerp.tools.config

# Path to the OpenERP Addons repository (comma-separated for
# multiple locations)

conf['addons_path'] = 'addonpathhere'

# Optional database config if not using local socket
conf['db_host'] = 'localhost'
conf['db_user'] = 'dbuserhere'
conf['db_port'] = 5432
conf['db_password'] = 'dbpasshere'
conf['running_env'] = 'dev'
conf['log_level'] = 'info'
conf['logrotate'] = True

#----------------------------------------------------------
# Generic WSGI handlers application
#----------------------------------------------------------
application = openerp.service.wsgi_server.application

#----------------------------------------------------------
# Gunicorn
#----------------------------------------------------------
# Standard OpenERP XML-RPC port is 8069
bind = '127.0.0.1:8069'
pidfile = '/var/run/openerp.pid'
workers = workershere
timeout = 240
max_requests = 10000
user = dbuserhere

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
