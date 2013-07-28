#!/usr/bin/python
# -*- coding: utf-8 -*-
#Title: Counting Sundays

import datetime

startDay = [0,0,0,0,0,0,0]
for year in range(1901,2001):
	for month in range(1,13):
		startDay[datetime.date(year, month, 1).weekday()] += 1

print startDay[6]
