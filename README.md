# on master (terminal)
`docker-compose -d --build`
`docker-compose exec master bash`
# on slaves (terminals)
`docker-compose exec nodeX bash`
# add all slaves ipis into ~/machinefile, ifconfig to get ip in slave terminal
`nano ~/machinefile`
# on each slave run
`service ssh start`
# for each slave in ~/machinefile pass:123 for ssh
`ssh-copy-id -i ~/.ssh/id_rsa.pub root@<container_ip>`
# on master
`ssh-agent`
# run mpi on master
`mpiexec -n 4 -machinefile ~/machinefile python -m mpi4py ~/ring.py`
`mpiexec -n 4 -machinefile ~/machinefile python -m mpi4py ~/graph.py`