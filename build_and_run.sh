#!/bin/bash
docker build -t flask-container .
docker run -p 80:5000 flask-container
