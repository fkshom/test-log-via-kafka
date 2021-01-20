FROM logstash:7.10.1

RUN apt-get update \
&& apt-get install -y --no-install-recommends \
    bash \
    vim \
&& apt-get -y clean \
&& rm -rf /var/lib/apt/lists/*
  
CMD ["ls", "-la"]
ENTRYPOINT [ "ls", "-la" ]