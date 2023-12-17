# Setting Up an MPI Cluster using Docker Compose

## Starting the Cluster

### On Master Node
1. Build and start the master node container:
    ```bash
    docker-compose up -d --build
    docker-compose exec master bash
    ```

### On Slave Nodes (for each node)
2. Build and start each slave node container:
    ```bash
    docker-compose exec nodeX bash
    ```

## Configuring Slave Nodes

### Inside Each Slave Node
3. Get the IP address of each slave node using:
    ```bash
    service ssh start
    ifconfig
    ```
    Pass for each slave: 123
   
    ```bash
    ssh-copy-id -i ~/.ssh/id_rsa.pub root@<slave_node_ip>
    ```

## Prepare `machinefile` on Master

### On Master Node
4. Create and edit the machinefile to include the IP addresses of all slave nodes:
    Add the IP addresses of all the slave nodes line by line
    Save and exit the file
   
    ```bash
    nano ~/machinefile
    ```

## Run MPI Jobs

### On Master Node
5. Run MPI jobs using the configured machinefile:
    ```bash
    ssh-agent
    mpiexec -n 4 -machinefile ~/machinefile python -m mpi4py ~/ring.py
    mpiexec -n 4 -machinefile ~/machinefile python -m mpi4py ~/graph.py
    ```
