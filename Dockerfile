FROM python:3.12.1-slim

RUN mkdir -p backend && \
	apt-get update && \
	apt-get install bash && \
	apt-get install -y python3-pip

COPY backend/requirements.txt ./backend/
RUN pip install -r backend/requirements.txt

COPY backend ./backend
WORKDIR /backend

COPY init.sh /init.sh
RUN chmod +x /init.sh

ENTRYPOINT ["/init.sh"]