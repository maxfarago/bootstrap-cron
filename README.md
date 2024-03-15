# bootstrap-cron

This repo contains the code for all scheduled tasks running within the `bootstrap` ecosystem.  These tasks share code with `bootstrap-api`, and leverage infrastructure created in the `bootstrap` repo.

While these tasks are being initially created and defined, they will live in this separate repo for the sake of clarity and instruction.  But relatively quickly these tasks should be incorporated into the `bootstrap` monorepo, [given the amount of shared logic](https://wiki.c2.com/?DontRepeatYourself).

## Task List

Individual tasks belong to an organizing concept within the `bootstrap` ecosystem.  For example, ***mailers*** is an organizing concept, and is a parent of the *Attendance Form Mailer* task that sends attendance forms to teachers of active events.

#### Attendance Form Mailer (`attendance`)
- Concept: `mailers`
- Schedule: Every day at 9am ET
- Description: Generates a new Google Form for taking attendance and emails it to the teacher leading the event

## Local Development

To run the `attendance` function locally:
```
npm run attendance
```