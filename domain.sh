#!/bin/bash

cat $1 | tr " " "\n" | grep .$2
