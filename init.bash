#!/bin/bash\n

rm -rf /etc/environmentadb \n
cat >> /etc/environmentadb << \"EOF\" \n
PG_HOST=${DBConnectString} \n
PG_PORT=5432 \n
PG_DATABASE=${DBMasterUserName} \n
PG_USER=${DBMasterUserName} \n
PG_PASSWORD=\"${DBMasterPassword}\"\n
\n

apt update && apt install git -y && apt install unzip -y && apt install docker-compose -y && apt install postgresql -y  \n

git clone https://github.com/daviddhc20120601/chat-with-pdf.git && cd chat-with-pdf/ \n

cp .devops/Dockerfile . && docker build . -t haidonggpt/front:1.0   && docker run -d -e /etc/environmentadb -p 8501:8501 haidonggpt/front:1.0  \n



