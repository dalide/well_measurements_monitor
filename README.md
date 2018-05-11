# Well_measurements_monitor
This app is a simple dashboard to monitor measurements. It can be used for data from well drill centers and pipelines.
The goal is to build an interactive dashboard, which integrates monitoring, predicting and alerting.  

Main tools used for the app:
* plotly dash --- a web based framework for building interactive dashboard
* css file and some layouts are adopted from the [oil-and-gas demo](https://github.com/plotly/dash-oil-and-gas-demo)

Right now it is a simple template showing some pressure and temperature data. 
The data is in csv format, but the file is too large so it is not uploaded. And the sample data is a simple modification of real data. 

To do list:
* make the layout more beautiful
* utilize streaming tools like [Spark Streaming](https://spark.apache.org/streaming/) or [Streamz](https://github.com/mrocklin/streamz)
* ...

The app is deployed on heroku, here is the [link](https://well-measurements-monitor-app.herokuapp.com/). It seems a little stuck right now. 
