# preview demo video

![img.png](docs/img.png)
![img_1.png](docs/img_1.png)
# Step 1 Cloud resources
## 1.1 create ecs with security group 8501 open
![img_2.png](docs/img_2.png)
![img_3.png](docs/img_3.png)

### need to create/ select if you have vpc setup
![img_4.png](docs/img_4.png)
### create security group
![img_5.png](docs/img_5.png)
![img_6.png](docs/img_6.png)
![img_7.png](docs/img_7.png)
![img_8.png](docs/img_8.png)
![img_9.png](docs/img_9.png)
![img_10.png](docs/img_10.png)
## 1.2 create adbpg with fastann enabled
![img_11.png](docs/img_11.png)
![img_12.png](docs/img_12.png)=
### this will take a around 10-15 mins, 
### get the public access endpoint:
![img_14.png](docs/img_14.png)
![img_15.png](docs/img_15.png)
### create admin account
![img_16.png](docs/img_16.png)
eg: 
username: aigcpostgres ,password: alibabacloud666
![img_17.png](docs/img_17.png)
### create a database with name: aigcpostgres
![img_18.png](docs/img_18.png)
![img_19.png](docs/img_19.png)

### add whitelist ip to 0.0.0.0/0
![img_20.png](docs/img_20.png)
![img_21.png](docs/img_21.png)

Step 2 env init
![img_22.png](docs/img_22.png)

```apt update && apt install git -y && apt install unzip -y && apt install docker-compose -y && apt install postgresql -y```
![img_23.png](docs/img_23.png)

Step 3 install packages
```git clone https://github.com/daviddhc20120601/chat-with-pdf.git && cd chat-with-pdf/```
![img_24.png](docs/img_24.png)

Step 4 run the docker
```cp .devops/Dockerfile . && docker build . -t haidonggpt/front:1.0   && docker run -d -p 8501:8501 haidonggpt/front:1.0```
![img_25.png](docs/img_25.png)

Step 5 insert you token and start using
![img_26.png](docs/img_26.png)
5.1 chatgpt token:
5.2 adbpg host name:gp-gs5inp2dl746742muo-master.gpdbmaster.singapore.rds.aliyuncs.com
![img_27.png](docs/img_27.png)
5.3 port: 5432
![img_28.png](docs/img_28.png)
5.4 database name: aigcpostgres
![img_29.png](docs/img_29.png)
5.5 adb pg username: aigcpostgres

5.6 adb pg password: alibabacloud666
step 6 my token and credentials are invalidated, do not try to use it , it is a waste of time