---------------------------------------Swift Conversions: High School Track & Field Performance Calculator-------------------------------

Summary:

-Swift Conversions is an event to event performance equivalence calculator for High School Track and Field. 
In short, Swift Conversions uses percentile to establish common ground between performances in the sport. For example: if a score of 
's1' in event 'e1' would rank its proper athlete in the 75th percentile across all participants of 'e1', and a score of 's2' in event 
'e2' would place its proper athlete in the 75th percentile across participants of 'e2', then 's1' is assumed to be equivalent to 's2'. 
Swift Conversions provides a fast and user friendly means of comparing all track and field performances based on this simple and 
objective criteria. Performances can be filtered according to an athlete's grade, gender, or the year in which it was achieved to 
provide a more complete picture of the athletes aptitude in relation to other participants in the sport. Swift Conversions is equipped 
with a database of over 1.5 million athletes from the years 2014-2018, essentially every official participant in the sport is included 
in the calculations. Data has been obtained via web scraping.

-Swift Conversions is a useful tool for coaches to determine which events an athlete may have the highest potential in. It can be 
used to predict future potential based on current ability. It can be used to compare the aptitudes of two or more athletes who 
participate in different events.

----------------------------------------------------------------How to use:--------------------------------------------------------

Note: This tool will not function without the database to support its calculations. This essential component will not be included on 
github due to issues with the size of the database files. Users of Swift Conversions will be limited to personal associates until the 
project is made public elsewhere. 

1. Select input event and insert score (default event is arbitrarily set to '800m'), minutes/seconds slot default to 0 when 
nothing is inserted. Feel free to enter a decimal for the seconds place. 

2. Select gender for input event. (You can convert male scores to female scores and vice-versa)

3. Select year range. Swift Conversions allows flexibility in the data used for its conversions. For example,
the user can select years 2014-2015 for the input event and 2016-2018 for the output event, the percentile will be calculated based 
on this refined sample size. 

4. Select grade range: You can convert 9th grade scores to 12th grade scores or any other desired combination.

5. Repeat this process for the output event, and click the 'get result' button. The output score, as well as the associated percentile 
will be included in the result. 

-----------------------------------------------------------Disclaimers------------------------------------------------------------------


-Percentile only serves as a rough indicator of performance 'aptitude'. Events are assumed to be equal when in reality they are not.
It is expected, however, that the various events in high school track and field are similarly accessible and no particular event 
attracts a more motivated or naturally gifted crowd of participants. Take the results of this calculator with a grain of salt. 

-It should be worth noting that performances in the extremely far ends of the spectrum are more volatile and the results obtained 
by comparing times in this area should be considered less indicative of the quality of the performance. The calculator cannot output a 
score that is faster than or slower than what has been achieved by a high schooler in the years 2014-2018. 
For example, if you were to insert '3:43.13' for the men's 1600m (input and output), the result would be '3:59.80' which is the fastest 
recorded 1600m by a high schooler in this time frame.


Please direct any questions or comments to 'nick.buoncristiani@berkeley.edu'. 


