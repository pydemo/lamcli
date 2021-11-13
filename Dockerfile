FROM amazonlinux:2.0.20200602.0 as stage2
WORKDIR /app
RUN yum update -y
RUN yum install -y \
python3-pip \
zip \
RUN yum -y clean all
RUN python3 -m pip install --upgrade pip



ENV APP_DIR /var/task

WORKDIR $APP_DIR



COPY requirements.txt .
COPY bin ./bin


RUN mkdir -p $APP_DIR/lib
RUN python3 -m pip  install -r requirements.txt -t /var/task/lib
RUN ls -al /var/task/lib
RUN echo "hello world 123" > output1.txt

FROM scratch 

COPY --from=stage2 /var/task/* .


