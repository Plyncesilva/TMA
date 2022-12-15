import paramiko

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect("10.0.2.15", password="kali")
ssh_stdin, ssh_stdout, ssh_stderr = ssh.exec_command("wget https://raw.githubusercontent.com/Plyncesilva/TMA/main/ssh.py")
ssh_stdin, ssh_stdout, ssh_stderr = ssh.exec_command("echo gotit")
ssh_stdin, ssh_stdout, ssh_stderr = ssh.exec_command("cat ssh.py")