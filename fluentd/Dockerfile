FROM ubuntu:20.04

# https://github.com/shimizukawa/docker-td-agent


RUN apt-get update && apt-get -y install curl libcurl4-openssl-dev ruby ruby-dev make
RUN apt-get install -y sudo gnupg
RUN curl -L https://toolbelt.treasuredata.com/sh/install-ubuntu-focal-td-agent4.sh | sh
RUN apt-get clean && rm -rf /var/cache/apt/archives/* /var/lib/apt/lists/*

# https://github.com/treasure-data/omnibus-td-agent/blob/master/plugin_gems.rb
RUN /opt/td-agent/bin/fluent-gem install --no-document \
    fluent-plugin-elasticsearch \
    fluent-plugin-record-modifier \
    fluent-plugin-exclude-filter \
    ruby-kafka \
    fluent-plugin-kafka

ADD ./config /etc/fluentd

CMD /opt/td-agent/bin/fluentd -vv -c /etc/fluentd/fluent.conf
