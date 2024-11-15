# MSD Reading Questions self-assessment bot
## Team members
Kristina Alyabeva - Project manager
Saveliy Chertkov - Developer
Kirill Korikov - Scrum master

[Repository on GitLab](https://gitlab.pg.innopolis.university/k.korikov/iu_rq_self_assessment_bot)
# Review with the customer

- [x] Show the new version of your app to the customer. 

The meeting with the customer took place on 11/15/2024. At the meeting, we showed 
- gemini integration into the bot 
- developed promt for gemini
- the result of the bot's work (the answer that the bot outputs to RQ)

- [x] Point out any new features that you implemented. Confirm that you understood everything correctly. 

The added functions are listed above. We demonstrated the functions to the customer at the meeting.

- [x] Document all feedback. 

In general, the customer is satisfied with the work done. For further development, he recommended splitting the bot's response into categories: the correctness of the response, checking the relevance of quotations and the coherence of the text.

- [x] Describe what features you are planning to implement next week.

We are planning for the next meeting:
- Finalize the promt
- Refine a more convenient output of the bot's response
- Integrate verification for GPT generation
# Analytics data

- [x] Start collecting analytics data to evaluate hypotheses that you formulated in the previous assignment. 
- [x] Provide screenshots of analytics dashboards. 
- [x] Provide your interpretation of the data on those dashboards. 
- [x] Provide conclusions that you can make based on the data.
For analytics, we decided on gathering it from the Google Forms questionnaire that our bot will send after student finishes their RQ assessment in it.
We discarded the idea to implement usage analytics in code due to its high cost. Our current product  has no server capabilities, we'd have to buy a server and develop a new backend  just to gather analytics data.
We believe, our small and very specific user base will allow us to manually gather data via the questionnaire. It's already hosted on Google servers and has already implemented dashboards and filters to visualise data.
# Setup usability testing 

- [x] Create a pre-test survey. Remember the goal here is to get important user attributes for your application. For example if you are making a camera application, you’ll want to know if the user is a professional photographer or not. This will later help you understand the usage patterns. Think of multiple user attributes that might be relevant to your application. Refer to the user personas for inspiration. 

**Key user attributes** we managed to extract from the end-user surveys:
- Usually can’t understand TA’s comments
- See no gaps in their reasoning
- Don’t spend much time on formatting
[Link](https://gitlab.pg.innopolis.university/k.korikov/iu_rq_self_assessment_bot/-/tree/main/IT%20Prod%20Assignments/Assignment_7) to the survey/interview results.

- [x] Write down how you will introduce the task that the user needs to do in your app.

For ease of use, the bot contains hints with which users can immediately understand what to do. The interface is standard for a telegram bot and intuitive. Also user can send "/help"  message that will once again show how to use the bot. 
![[photo_2024-11-15_18-16-54.jpg]]

- [x] Think how you will observe what the user is doing. Create a separate dashboard if you can use analytics. If you can’t use analytics, write down a process of how you will observe the experiment and take notes. Maybe you can do both. 

To monitor the usability, we asked our classmates to check the use of the bot. They did a good job without causing any errors. It was also not difficult for them to insert their answers into the template.
![[Pasted image 20241115185854.jpg]]

- [x] Create a post-test survey. Include SEQ, ASQ, SUS, and open-ended questions. 

We have created a [post-test survey](https://forms.gle/tP6tCpGYLze1E9tQ7) that includes all types of questions for feedback from users

- [x] Do a couple of practice runs. Ask your friend to go through the entire usability testing process. Make sure all surveys work, you can observe what the user is doing, you can collect analytics, and the data comes in a format that you expect. 

Analytical data on the survey can be seen in the [repository](https://gitlab.pg.innopolis.university/k.korikov/iu_rq_self_assessment_bot/-/blob/main/IT%20Prod%20Assignments/Assignment_7/Post-test_survey_.csv.zip). 

- [x] Make sure you can split your observations into categories Exploratory Actions (Gibson Affordances) and Correct Usability (Norman Affordances).

| Exploratory Actions / Gibson Affordances                              | Correct Usability / Norman Affordances                                |
| --------------------------------------------------------------------- | --------------------------------------------------------------------- |
| The user launches the application                                     | The user sees the start message with the command "/help"              |
| The user clicks the "/help" command to learn how to work with the bot | The user clicks the "/help" command to learn how to work with the bot |
| The user clicks the "/upload" command                                 | The bot asks you to enter the RQ number                               |
| The user enters the RQ number                                         | The bot requests to download a RQ file                                |
| The user uploads the file                                             | The bot displays the result of the check                              |

The observation process was conducted without any errors by the users

# Sprint cycle 

- [x] Review changes that you were planning to add to this sprint. Make sure you account for adding analytics to your app. 

Improve our model to:
- return more readable text (split bot’s answer in paragraphs by answer grading criteria)
- inspect referenced sources directly (implement Retrieval Augmented Generation)
- justify its statements (if bot says something is relatable, this statement should be proven so).

- [x] Review your strategic plan. Are you still on track? Does it need to be modified? Update your plan if needed. 

Initial strategic plan was mostly complete, excluding few features: title page, page limit, reference page inspections.
During the development these features were marked as not important currently. Instead, we focused on the improving feature that gives our project its core value – answer’s coherence/relevance inspection by AI.
This feature was implemented during this sprint and we plan to refine it in all the next ones, comparing it to the students and TAs/Professor’s assessments of our bot comments.
Basically, all next iterations will look like that:
**Thursday:** team meeting to discuss current progress and tasks.
**Friday:** review with the customer, distribution of tasks between team members.
**Saturday – Wednesday:** model improvement + feedback collection.

- [x] Review your sprint process and determine what can be improved. Look at the results of your previous sprint retrospective. Decide how you are going to improve this sprint based on that retrospective. 

Previous retrospection mentioned communication issues. They were solved by team members reaching out to the remaining one to discuss this and decide on specific date to meet.
For now, we don’t see any issues in our sprint process.

- [x] Conduct sprint planning. 

Sprint planning this time was split into two meetings: one personal on Thursday, and one via Telegram call on Friday, after the customer review.

- [x] Describe the sprint goal. 

Make bot’s feedback more relatable to the TA/professor one by completing aforementioned tasks. This is measured solely by students and TA/professor feedback.

- [x] Determine what tasks need to be done and who is going to do those tasks.

**Saveliy:** Refine model.
**Kirill:** Sprint management. Product demos to end-users.
**Kristina:** Team management. Assignments management.

- [x] Execute the sprint. There should be completed sprint artifacts like tasks, code, merge requests, etc. 

[Link to a Gitlab](https://gitlab.pg.innopolis.university/k.korikov/iu_rq_self_assessment_bot)

- [x] Conduct a sprint retrospective. Describe the results of the retrospective.

**What went well:** communication issues solved.
**What went wrong**: we didn’t see any issues with our sprint process this week.
**Possible improvements**: we can’t find any now. Current sprint process is in somewhat stable phase now as it seems, so most of the improvements were already done and pace of improvements has dropped significantly for us to improve each week given our management resources.