FROM digi0ps/python-opencv

# digi0ps/python-opencv workdir
# WORKDIR /usr/src/app

COPY requirements.txt /usr/src/app/requirements.txt

RUN pip install -r /usr/src/app/requirements.txt

COPY FaceSwap /usr/src/app
COPY server /usr/src/app
COPY static /usr/src/app/static

ENTRYPOINT python /usr/src/app/server.py
EXPOSE 8888
