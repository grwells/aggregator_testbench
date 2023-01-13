# Data Gator Test Bench
This directory contains the code used to monitor and log data collected from the aggregator, including battery statistics, power draw, and MQTT data transmission.

All data will be collected by a Raspberry Pi and stored in log files while also printing the data to the terminal. Data logs will be divided into three:

1. MQTT Topics and Messages: `mqtt_log.csv`
    * time stamps will be provided for each data entry
    * header: ` date , time , topic , message`

2. Fuel Gauge: `fuel_guage.csv`
    * time stamps for each entry
    * header: ` date , time , battery voltage , battery percentage , (dis)charge rate `

3. INA219 Current Monitor: `power_draw.csv`
    * time stamps for each entry
    * header: ` date , time , voltage(V), current(A), power(W) `
