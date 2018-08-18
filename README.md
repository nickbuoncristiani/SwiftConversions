# Swift Conversions: High School Track & Field Performance Calculator

## Summary:

Swift Conversions is an event to event performance equivalence calculator for High School Track and Field. 
Swift Conversions uses percentile to establish common ground between performances in the sport. For example: a performance of 11.0 seconds in a 100m dash would rank its proper athlete in the top ~1.85% of all 100m participants nationwide, therefore this performance is considered 'equivalent' to a 1:57.8 which is also a top 1.85% performance amongst 800m athletes. Swift Conversions provides a fast and user friendly means of comparing all track and field performances based on this simple and objective criteria. Performances can be filtered according to an athlete's grade, gender, or the year in which it was achieved to provide a more complete understanding of the athletes aptitude in relation to other participants in the sport. Swift Conversions is equipped with a database of over 1.5 million athletes from the years 2014-2018: essentially every participant in the sport. Data has been obtained by scraping the web.

The primary motivation for using Swift Conversions is individual curiosity. Say, you're a 1600m athlete and your best friend prefers to run the 400m. With Swift Conversions you will have the ability to see which of the two of you is stronger in his/her respective event.
Swift Conversions is also a useful tool for coaches to determine in which events an athlete may have the highest potential. The results can also be easily extrapolated to predict future potential: simply narrow the grade filter (see instructions below).

## How to use:

0. Download the full project here: https://drive.google.com/open?id=1IinMifyE-am5kWL1_tVorxzES-m35-Xi 

1. Select input event and insert score (default event is arbitrarily set to '800m'), minutes/seconds slot default to 0 when 
nothing else is provided. Feel free to enter a decimal for the seconds place.

2. Select gender for input event. (You can convert male scores to female scores and vice-versa)

3. Select year-range. Swift Conversions allows flexibility in the data used for its conversions. For example,
the user can select years 2014-2015 for the input event and 2016-2018 for the output event, the percentile will be calculated based 
on this refined sample size. 

4. Select grade-range: You can convert 9th grade scores to 12th grade scores or any other desired combination. This can be a useful tool for predicting future performance of younger athletes.

5. Repeat this process for the output event, and click the 'get result' button. The output score, as well as the associated percentile 
will be included in the result. 

## Disclaimers

-Percentile only serves as a rough indicator of performance 'aptitude'. It is expected that the various running events in high school track and field are similarly accessible and no particular event attracts a more motivated or naturally gifted crowd of participants. Taking this into consideration, raw percentile seems to be the most pragmatic means of comparison. 

-It should be worth noting that performances in the EXTREMELY far ends of the spectrum are more volatile and the results obtained 
by comparing times in this area should be considered slightly less indicative of the quality of the performance. Also, The calculator cannot output a score that is faster than or slower than what has been achieved by a high schooler in the years 2014-2018. 
For example, if you were to insert '3:43.13' for the men's 1600m (world record) and compare it to the same event, the result would be '3:59.80' which is the fastest recorded 1600m by a high schooler in this time frame. 


Please direct any questions or comments to 'nick.buoncristiani@berkeley.edu'. 


