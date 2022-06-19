# action will be run in python3 container
FROM python:3
# heelo_world.py is the file that will contain the codes that we want to run for this action.
COPY hello_world.py /hello_world.py
# we will just run our script.py as our docker entrypoint by python script.py
CMD ["python", "/hello_world.py"]