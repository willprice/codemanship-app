honcho: sh -c 'honcho start web_acceptance_tests 2>&1 && honcho start web'
web: sh -c 'cd ./src && gunicorn -w 1 hello:app'
web_acceptance_tests: java -jar fitnesse-standalone.jar -p $PORT
