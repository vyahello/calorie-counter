FROM vyahello/calorie-counter-base:0.1.0
LABEL version=0.1.0 \
      metadata="The main image for calorie counter application" \
      maintainer="Volodymyr Yahello <vyahello@gmail.com>"
ARG VERSION
ENV CODE_DIR="/app" \
    SERVER_PORT="5001" \
    IMAGE_VERSION=${VERSION}
WORKDIR ${CODE_DIR}
COPY counter counter
COPY requirements.txt docker/docker-entry.sh ./
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt && \
    rm -v requirements.txt
ENTRYPOINT ["/app/docker-entry.sh"]