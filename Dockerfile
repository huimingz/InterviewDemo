FROM python:3.8

MAINTAINER huimingz <huimingz12@outlook.com>

# 更换至清华源
#RUN cp /etc/apt/sources.list /etc/apt/sources.list.d/sources.list.bak \
#    && echo "deb https://mirrors.tuna.tsinghua.edu.cn/debian/ buster main contrib non-free" > /etc/apt/sources.list \
#    && echo "deb https://mirrors.tuna.tsinghua.edu.cn/debian/ buster-updates main contrib non-free" >> /etc/apt/sources.list \
#    && echo "deb https://mirrors.tuna.tsinghua.edu.cn/debian/ buster-backports main contrib non-free" >> /etc/apt/sources.list \
#    && echo "deb https://mirrors.tuna.tsinghua.edu.cn/debian-security buster/updates main contrib non-free" >> /etc/apt/sources.list \

RUN mkdir -p /var/www/django/demo

WORKDIR /var/www/django/demo/

COPY ./requirements.txt /var/www/django/demo/requirements.txt

RUN pip install -i https://pypi.tuna.tsinghua.edu.cn/simple -r requirements.txt \
    && pip install -i https://pypi.tuna.tsinghua.edu.cn/simple uwsgi


COPY manage.py  ./
COPY . ./

RUN python manage.py makemigrations \
    && python manage.py migrate


EXPOSE 8080

#ENTRYPOINT ["uwsgi", "-b", "32768", "--http", "0.0.0.0:8080", "--module", "InterviewDemo.wsgi"]

ENTRYPOINT ["python", "manage.py", "runserver", "0.0.0.0:8080"]
