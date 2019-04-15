#!/bin/bash

for dar in *.dar; do
  curl -u admin:2001jcla -X POST -H "content-type:multipart/form-data" http://localhost:4516/deployit/package/upload/$dar -F fileData=@$dar
done
