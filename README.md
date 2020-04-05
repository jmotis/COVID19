# COVID19

This repository includes state-by-state US official infection counts data pulled from the Covid Tracking Project (https://covidtracking.com) with Wikipedia & news reports to fill in the gaps

The code extrapolates from the official infection count to determine the current infection rates taking into rough account the incubation period, time it takes to become symptomatic to report to authorities, and testing timelines (14-16 days).
It also provides a guess as to total infections assuming a 25% asymptomatic rate - this latter number is still speculative.
It then divides by the state's 2019 population (gathered from Wikipedia, with a few holes patched by Google searches) and multiplies by 100 to give the percent of the population infected.

All numbers should be taken with a grain of salt.  We know there's rampant underreporting in the US and we *really* haven't got a good handle on asymptomatic rates.