## Title

BibboDB

## Platform

olicyber

## Url

https://training.olicyber.it/challenges#challenge-303

## Category

Web

## Difficult

easy (if you know the nosql injection not like me)

## Step

1. The first thing I did was to download and look at the source code.
2. The second thing I did was to start the docker to have more freedom to test and to be able to print out what I was sending.
3. After that I found two possible vulnerabilities, the first was to bypass the if control, realising after a few attempts that this was not possible.
4. Next, I looked to see if the Mongo query was vulnerable.
5. In fact, by using a test input I found online ([source](https://www.firecompass.com/blog/detecting-nosql-injection/)) I saw that injections were possible

## Solution

Once the vulnerability was found, all that was needed was to learn more about how it worked until you got as query to send: ` filter['$eq'] = secret ` where eq is one of mongo's query conditions (eq = equal)
