FROM debian 

ENV PYTHONUNBUFFERED=1

RUN apt-get update && apt-get upgrade -y && \
apt-get install python3-pip curl nano -y && \
pip3 install pandas numpy scikit-learn && \
pip3 install -i https://test.pypi.org/simple lambdata-johanaluna && \
python3 -c "import lambdata_johanaluna; print('sucess!!!')"
