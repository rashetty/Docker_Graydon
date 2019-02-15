FROM       python:3
LABEL      maintainer="Rahul Shetty"

ARG model_file=DT_2017md10_mss5_msl5_mf25_balanced.sav
ARG company_file=companies_with_features.csv

COPY $model_file model.sav
COPY $company_file company.csv
COPY       get_company_probability.py /

RUN        pip install numpy
RUN        pip install pandas
RUN        pip install sklearn
RUN        chmod a+x get_company_probability.py

ENTRYPOINT ["./get_company_probability.py"]

