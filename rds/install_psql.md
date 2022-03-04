## Enable EPEL repository
```sudo amazon-linux-extras install epel```

## Install PostgreSQL 13 on Amazon Linux 2
```
sudo tee /etc/yum.repos.d/pgdg.repo<<EOF
[pgdg13]
name=PostgreSQL 13 for RHEL/CentOS 7 - x86_64
baseurl=http://download.postgresql.org/pub/repos/yum/13/redhat/rhel-7-x86_64
enabled=1
gpgcheck=0
EOF
```
                                         
```sudo yum install postgresql13 postgresql13-server```
                                         
## Initialize and start database service
```sudo /usr/pgsql-13/bin/postgresql-13-setup initdb```
                                         
```sudo systemctl enable --now postgresql-13```
                                         
```systemctl status postgresql-13```
                                         
```sudo su - postgres```
