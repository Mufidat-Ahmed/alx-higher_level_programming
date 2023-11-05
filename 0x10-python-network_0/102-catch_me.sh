#!/bin/bash
#causes the server to respond with a message containing You got me!
curl -s --request POST -d "user_id=98" -L 0.0.0.0:5000/catch_me
