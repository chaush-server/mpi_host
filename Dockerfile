FROM husseinabdallah2/mpi4py-cluster:master

# Copy the startup script into the container's root directory
COPY ring.py /root/ring.py
COPY graph.py /root/graph.py
# Grant execution permissions to the script
RUN chmod +x /root/ring.py
RUN chmod +x /root/graph.py
