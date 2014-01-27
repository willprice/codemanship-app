honcho: sh -c 'honcho start acceptance_tests 2>&1 && honcho start web'
web: sh -c 'cd ./src && gunicorn -w 1 hello:app'
acceptance_tests: java -jar fitnesse-standalone.jar -p 8080
