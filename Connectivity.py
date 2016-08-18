import jenkins
import socket

server = jenkins.Jenkins('http://localhost:8080', username='thirumalraj.s', password='password')
user = server.get_whoami()
##version = server.get_version()
versionss = server.get_version
print('Hello %s from Jenkins %s' % (user['fullName'], versionss))
devices = socket.gethostname()
listt = server.get_all_jobs()

print listt
print devices