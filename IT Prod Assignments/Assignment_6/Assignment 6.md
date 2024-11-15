# MSD Reading Questions self-assessment bot
## Team members
Kristina Alyabeva - Project manager
Saveliy Chertkov - Developer
Kirill Korikov - Scrum master

[Repository on GitLab](https://gitlab.pg.innopolis.university/k.korikov/iu_rq_self_assessment_bot)
# Review with the customer
- [x] Show the new version of your app to the customer. 

The meeting with the customer took place on 4.11.2024. Previously, we sent him messages from the bot. At the meeting, the functions were demonstrated and their operation was explained.

- [x] Point out any new features that you implemented. Confirm that you understood everything correctly. 

Our team showed the customer the newly developed functions:
- Checking for examples 
- Changing the response structure

- [x] Document all feedback. 

The customer is satisfied with the correctness of the developed functions, but at this stage the whole work seems too primitive for him. Since before that we were developing features that could be implemented using algorithms, we agree that we are not solving the main task of checking for meaningfulness yet.

- [x] Describe what features you are planning to implement next week.

 This week we plan to work on connecting the api to implement the nlp part. We are also working on the correct promt that will be transmitted.

# Formulate hypotheses

- [x] Create a list of your assumptions, ideas, or goals. Your list should contain about 20 items. 

- bot feedback will help
- bot can give peace and tranquility for a student and improve their mental balance
- we assume our survey is relevant
- template will be used
- we got the ratio of lines/refs right
- student can host the bot and has the Docker
- students will leave feedback
- student has basic IT skills and knowledge
- student has Telegram account and a PC
- student knows how to start the bot
- student understands english
- student is taking MSD course
- student has RQ
- RQ is in PDF format
- bot will shorten time for making RQ
- bot will lengthen time for making RQ

- [x] Order the list from the most important at the top to the least important. 

The assumptions above are already sorted by importance.

- [x] Formulate hypotheses from the top 6 or 8 items using the hypothesis template from the lecture. 

The hypotheses for the first 6 assumptions are given below:

We believe that bot feedback for MSD student will result in helping improve RQ when using the bot

We believe that improved RQ for MSD student will result in mental balance improvement when submitting RQ

We believe that our survey is relevant for future MSD students will result in helpful bots's functions when using the bot

We believe that our RQ template will be used for MSD students that will result in efficient feedback when submitting RQ to bot

We believe that we got the ratio of lines/refs right for MSD students and TA will result in improvement of RQ based on bot's feedback when submitting RQ to bot

We believe that having knowledge about working with the Docker will be sufficient for students to will result in launching the bot when starting to use the bot


- [x] Identify the most important hypotheses for your application. It will be the base for your application KPI metric. 

First hypotheses (We believe that bot feedback for MSD student will result in helping improve RQ when using the bot) is most important for us.

Our KPI it is feedback from users. We send a [Google form](https://docs.google.com/forms/d/e/1FAIpQLScenM9ZvUPXMuA2GUZgMWEEa01kFTM2vWlBq2rT6cqlNR4o9A/viewform) to fill out to the user after checking the RQ. The best indicator for the final value will be a score of 7 or higher. The usefulness of the functions will also be tested. We will consider the selected functions useful if the user is satisfied with 60% or more of them.

- [x] Describe how your other hypotheses relate to your main one. 

Improving the RQ will help the student improve his mental state if he is satisfied with the results of the bot after receiving the grade. Also, this result will prove the correctness of the selected functions.

- [x] Study your hypotheses and identify what kind of data you need to collect to prove or disprove your hypothesis. 

To confirm our hypotheses, we will need feedback from students, which will be collected during the beta testing of the bot, using the [Google form](https://docs.google.com/forms/d/e/1FAIpQLScenM9ZvUPXMuA2GUZgMWEEa01kFTM2vWlBq2rT6cqlNR4o9A/viewform)

- [x] Write down how long you think you need to collect the data. You might have several different numbers here. One number could be for data “resolution”. For example, I expect to have 3 users that accomplish some task every week. Here the “resolution” is one week because they might not come to your app every day. The other number could be how long you need to collect the data to prove or disprove your assumption. For example, I expect 7 new active users every week. After 4 weeks of such growth I will conclude that the MVP of my app is popular enough to continue development. 

For data resolution we assume that we will need a period of 3 RQ Assignments, because when RQ1 is executed, users will not yet know the feedback from TA, which they will receive only for the execution of RQ3. It is also possible that when performing RQ1, many people will not want to redo their work to fit the proposed template.

- [x] Describe the data that you need to collect to support your hypotheses

We will need data from the [Google form](https://docs.google.com/forms/d/e/1FAIpQLScenM9ZvUPXMuA2GUZgMWEEa01kFTM2vWlBq2rT6cqlNR4o9A/viewform)

# Add metrics and analytics to your application

- [x] Research methods to collect metrics and analyze the collected data based on what you need to support your hypotheses. 

[Google form](https://docs.google.com/forms/d/e/1FAIpQLScenM9ZvUPXMuA2GUZgMWEEa01kFTM2vWlBq2rT6cqlNR4o9A/viewform)

- [x] Add necessary code to collect analytics to your application. 

The results of the developed code are shown in the figure below
![[Pasted image 20241108185101.png]]

- [x] Create necessary dashboards or charts.

Сharts will be built based on [feedback](https://docs.google.com/forms/d/e/1FAIpQLScenM9ZvUPXMuA2GUZgMWEEa01kFTM2vWlBq2rT6cqlNR4o9A/viewform) data, after filling in by users
# Sprint cycle

- [x] Review changes that you were planning to add to this sprint. Make sure you account for adding analytics to your app. 

This week’s plan had suffered a drastic change:

- We focused on pinpointing the most valuable functionality (ways to tell whether an answer is lacking **justification** and/or **reasoning**) we can provide to implement it first.
- End-user demos weren’t done and instead replaced by researching ways to implement aforementioned functionality using AI models.

This sprint had customer interview delayed because we couldn’t reach them at the initially planned date and time. Because of that delay, sprint review was done much later (on Monday instead of Friday right after the interview). And tasks were planned on this date, which was not reflected in the previous sprint document.

- [x] Review your strategic plan. Are you still on track? Does it need to be modified? Update your plan if needed. 

This week we couldn’t complete our [Iteration 3](https://gitlab.pg.innopolis.university/k.korikov/iu_rq_self_assessment_bot/-/blob/main/IT%20Prod%20Assignments/Assignment_2/Assignment_2.pdf?ref_type=heads) fully (points _b_ and _c_ are missing). Gladly, the initial plan has some room to allow us delays or reschedules. This week was mostly spent on research and adding analytics. The plan might be in need of rework according to the aforementioned change of focus. We’re going to review our strategic plan during this week (8.11 – 15.11).

- [x] Review your sprint process and determine what can be improved. Look at the results of your previous sprint retrospective. Decide how you are going to improve this sprint based on that retrospective. 

Unstable meeting dates harmed the communication between team members. To solve that issue, we have to specify days to meet and communicate.

- [x] Conduct sprint planning. 

Sprint planning was done in our team’s Telegram chat as always.

- [x] Describe the sprint goal. 

Connect AI to our bot so it could be used to implement core functionality (answer **justification** and **reasoning** inspection).

- [x] Determine what tasks need to be done and who is going to do those tasks. 

**Team:** Decide on which specific days and time we will conduct meetings to communicate our current work progress between team members.

**Saveliy:** Connect Gemini API to our bot.

**Kirill:** Update strategic plan. Manage sprint.

**Kristina:** Identify remaining hypotheses and define a KPI metric. Create a questionnaire to gather end user satisfaction with the bot metric.

- [x] Execute the sprint. There should be completed sprint artifacts like tasks, code, merge requests, etc. 

[Link to a Gitlab](https://gitlab.pg.innopolis.university/k.korikov/iu_rq_self_assessment_bot)

- [x] Conduct a sprint retrospective. Describe the results of the retrospective.

**What went well:** we managed to achieve clear tasks for everyone in the end.

**What went wrong**: miscommunication, we weren’t sure of what we have to do until the end of this sprint.

**Possible improvements**: concrete meeting days, mentioned above.