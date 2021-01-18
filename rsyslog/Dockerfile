FROM ubuntu:20.04

RUN apt-get update \
&& apt-get install -y --no-install-recommends \
    rsyslog \
    rsyslog-kafka \
&& apt-get -y clean \
&& rm -rf /var/lib/apt/lists/*

VOLUME [ "/config", "/work", "logs" ]
CMD [ "-f", "/config/rsyslog.conf", "-nd" ]
ENTRYPOINT [ "rsyslogd" ]
