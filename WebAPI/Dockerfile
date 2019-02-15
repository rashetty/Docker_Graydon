FROM       ubuntu:16.04
LABEL      maintainer="Rahul Shetty"

ARG model_file=DT_2017md10_mss5_msl5_mf25_balanced.sav

RUN apt-get update -y \ 
    && apt-get install -y python3-pip python3-dev \
    && cd /usr/local/bin \
    && ln -s /usr/bin/python3 python \
    && pip3 install --upgrade pip 

COPY $model_file model.sav 
COPY api_features_to_probs.py /

RUN        pip install numpy
RUN        pip install pandas
RUN        pip install flask
RUN        pip install sklearn
RUN        chmod a+x api_features_to_probs.py 

ENTRYPOINT ["python"]
CMD ["api_features_to_probs.py"]

