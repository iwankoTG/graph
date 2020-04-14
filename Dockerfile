FROM nvcr.io/nvidia/tensorflow:19.12-tf1-py3  

ARG DEBIAN_FRONTEND=noninteractive
             
RUN apt-get update && \
    apt-get install -y python3-tk && \
    pip install --upgrade pip && \
    pip install networkx && \
    pip install nxviz && \
    pip install pytest && \
    pip install nose


