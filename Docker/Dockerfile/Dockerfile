#FROM twint as interpreter
#COPY requirements.txt /requirements.txt
#RUN pip install -r /requirements.txt \
#    && rm -rf /root/.cache/pip/*
#RUN mkdir -p /opt/tsunamitwint
#LABEL name=interpreter stage=dev
#ENTRYPOINT ['python3']

#FROM tsunamitwint-interpreter as wheels
#WORKDIR /wheels
#COPY --from=dev /requirements.txt /wheels/requirements.txt
#RUN pip wheel --wheel-dir=/wheels -r /wheels/requirements.txt \
#    && pip wheel --wheel-dir=/wheels Docker-packages
#LABEL name=tsunamitwint stage=wheels


FROM interpreter as run
#COPY --from=wheels /wheels /wheels
#RUN pip install --no-index \
#                -r /wheels/requirements.txt \
#                --find-links=/wheels \
#    && rm -rf /wheels \
#    && rm -rf /root/.cache/pip/*

COPY run.py /run.py
RUN chmod +x /run.py

LABEL name=run stage=prod

ENTRYPOINT ['/run.py']
WORKDIR /opt/tsunamitwint