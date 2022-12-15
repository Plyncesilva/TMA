import paramiko

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect("10.0.2.15", password="kali")
ssh_stdin, ssh_stdout, ssh_stderr = ssh.exec_command("wget ")
ssh_stdin, ssh_stdout, ssh_stderr = ssh.exec_command("echo hello")
ssh_stdin, ssh_stdout, ssh_stderr = ssh.exec_command("echo hello")