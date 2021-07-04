.PHONY: publish test build-test run-test-image

publish:
	@serverless deploy -v

remove:
	@serverless remove -v

test: build-test run-test-image

build-test:
	@docker build -t myonlinebookstore_lambda_book:latest .

run-test-image:
	@docker run -p 9000:8080 myonlinebookstore_lambda_book:latest

run-test-query-local:
	@curl -XPOST "http://localhost:9000/2015-03-31/functions/function/invocations" -d '{}'

run-test-query-aws:
	@serverless invoke -f generate-book
