# Heroku model deployment

### clone the repo

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
--data-raw '{"input_data":[{"fields":["DAY","DAY_OF_WEEK","ORIGIN_AIRPORT","DESTINATION_AIRPORT","DEPARTURE_DELAY","TAXI_OUT","DISTANCE"],"values":[[11,7,"ABQ","DFW",2,11,570]]}]}'

## Debug heroku

`heroku logs --tail`
