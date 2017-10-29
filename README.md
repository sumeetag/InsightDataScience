# Table of Contents
1. [Introduction](README.md#introduction)
2. [Challenge summary](README.md#challenge-summary)


# Introduction
You’re a data engineer working for political consultants and you’ve been asked to help identify possible donors for a variety of upcoming election campaigns. 

The Federal Election Commission regularly publishes campaign contributions and while you don’t want to pull specific donors from those files — because using that information for fundraising or commercial purposes is illegal — you want to identify the areas (zip codes) that may be fertile ground for soliciting future donations for similar candidates. 

Because those donations may come from specific events (e.g., high-dollar fundraising dinners) but aren’t marked as such in the data, you also want to identify which time periods are particularly lucrative so that an analyst might later correlate them to specific fundraising events.

# Challenge summary

For this challenge, we're asking you to take an input file that lists campaign contributions by individual donors and distill it into two output files:

1. `medianvals_by_zip.txt`: contains a calculated running median, total dollar amount and total number of contributions by recipient and zip code

2. `medianvals_by_date.txt`: has the calculated median, total dollar amount and total number of contributions by recipient and date.

As part of the team working on the project, another developer has been placed in charge of building the graphical user interface, which consists of two dashboards. The first would show the zip codes that are particularly generous to a recipient over time while the second would display the days that were lucrative for each recipient. 

Your role on the project is to work on the data pipeline that will hand off the information to the front-end. As the backend data engineer, you do **not** need to display the data or work on the dashboard but you do need to provide the information.

You can assume there is another process that takes what is written to both files and sends it to the front-end. If we were building this pipeline in real life, we’d probably have another mechanism to send the output to the GUI rather than writing to a file. However for the purposes of grading this challenge, we just want you to write the output to files.
