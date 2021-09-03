# Heroku model deployment

### Clone the repo

- `git clone https://github.com/makkader/heroku-model-deploy.git`

### Create app

- `heroku create <appname>`

### Create remote for heroku

- `heroku git:remote -a <appname>`

### Push to heroku

- `git push heroku master`

## Test

curl --request POST 'https://airline-delay-123-test.herokuapp.com/predict' \
--header 'Content-Type: application/json' \
--user 'datarobot:apikey_for_datarobot' \
--data-raw '[{"DAY":11,"DAY_OF_WEEK":7,"ORIGIN_AIRPORT":"ABQ","DESTINATION_AIRPORT":"DFW","DEPARTURE_DELAY":2,"TAXI_OUT":11,"DISTANCE":570}]'

## Debug heroku

`heroku logs --tail`
