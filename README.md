# Slack name ppm
it changes your slack name to ppm of CO2.

# Sample
![](./sample.png)

# DEVELOPMENT
prepare `dev.bash`.

```dev.bash
#!/bin/bash
export NETATOMO_CLIENT_ID=""
export NETATOMO_CLIENT_SECRET=""
export NETATOMO_USER_NAME=""
export NETATOMO_PASS=""
export NETATOMO_MODULE_NAME=""
export SLACK_TOKEN=""
export SLACK_USER_ID=""
export SLACK_USER_NAME_PREFIX=""

"$@"
```
