FROM public.ecr.aws/lambda/python:3.8
# Adding application.
COPY app.py ${LAMBDA_TASK_ROOT}
# Add application requirements.
COPY requirements.txt ${LAMBDA_TASK_ROOT}
# Install application dependencies.
RUN python3 -m pip install -r requirements.txt
CMD [ "app.handler" ]
