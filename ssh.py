import paramiko
from scp import SCPClient

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())


ssh.connect("10.0.2.15", password="kali")

scp = SCPClient(ssh.get_transport())
scp.put("ssh.py")


ssh_stdin, ssh_stdout, ssh_stderr = ssh.exec_command("cat ssh.py")