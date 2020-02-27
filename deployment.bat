SET LAMBDA_NAME=tfl_status
SET ZIP_FILE_NAME=code.zip

pip install -r requirements.txt -t ./
7z a -tzip %ZIP_FILE_NAME% @listfile.txt
aws lambda update-function-code --profile personal --function-name %LAMBDA_NAME% --zip-file fileb://%ZIP_FILE_NAME%
DEL %ZIP_FILE_NAME%