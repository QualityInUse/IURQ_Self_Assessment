# MSD Reading Questions self-assessment bot
## Team members
Kristina Alyabeva - Project manager
Saveliy Chertkov - Developer
Kirill Korikov - Scrum master

[Repository on GitLab](https://gitlab.pg.innopolis.university/k.korikov/iu_rq_self_assessment_bot)
# Review with the customer

- [x] Show you v1 version to the customer

Unfortunately, this week we rescheduled a meeting with the customer and it will take place only on 11.14.2024
We sent him the changes containing: 
- Checking for examples 
- Changing the response structure

- [x] Show this version of the product to your customer. Point out any new features that you implemented. Confirm that you understood everything correctly. 
- [x] Document all feedback. 
- [x] Describe what features you are planning to implement next week.
This week we plan to work as agreed with the customer:
- Implement a check for all issues
- Connect keys to gemini to implement other functions
- Get feedback from students on UX
# Add unit tests

- [x] Add appropriate unit test framework for your project. For example, if you are using Python, I recommend pytest. If you are using Go, pick an appropriate test framework for Go. 

We use pytest module for the application testing. 

- [x] Add test coverage. 
- [x] Add unit tests. You should aim for at least 50% coverage. The test coverage should not be less than 30% for this assignment. 

Our Unit-tests cover 54% of the code.

![[photo_2024-11-01_19-47-49.jpg]]
- [x] Add documentation on how to run your tests and check the test coverage.

Test documentation you can finde in [repository](https://gitlab.pg.innopolis.university/k.korikov/iu_rq_self_assessment_bot/-/blob/main/IT%20Prod%20Assignments/Assignment_5/Test_Documentation.md)
# Extra credit opportunity

- [ ] Set up production and staging application instances. 
- [x] Set up continuous integration and continuous deployment pipelines.

We have only done the CI part.
There is no CD part in our project, because our project is not deployed on the server.

The CI part contains the build and test stages. 

You can check it out in the [repository](https://gitlab.pg.innopolis.university/k.korikov/iu_rq_self_assessment_bot/-/blob/main/.gitlab-ci.yml).
# Sprint cycle

- [x] Review changes that you were planning to add to this sprint. Make sure you account for adding unit tests this sprint. 

[Initial plan](https://gitlab.pg.innopolis.university/k.korikov/iu_rq_self_assessment_bot/-/blob/main/IT%20Prod%20Assignments/Assignment_4/Assignment%204.md?ref_type=heads) had a mistake: requirement specified making 5 personas, not 10.
Our team couldn't contact customer for a review this week, so instead we sent them screenshots of the current project state.

- [x] Review your strategic plan. Are you still on track? Does it need to be modified? Update your plan if needed. 

[Iteration 2](https://gitlab.pg.innopolis.university/k.korikov/iu_rq_self_assessment_bot/-/blob/main/IT%20Prod%20Assignments/Assignment_2/Assignment_2.pdf?ref_type=heads) is almost fully done. Only thing left is to check the relevance of an answer which is harder than anticipated and will be moved to the next iteration.

- [x] Review your sprint process and determine what can be improved. Look at the results of your previous sprint retrospective. Decide how you are going to improve this sprint based on that retrospective. 

Current sprint processes fully satisfy the team, so we don't see any need in changing anything.

- [x] Conduct sprint planning. 

- Implement feature of checking presence of all answers, researching methods to use AI to inspect answer's relevance.
- Conduct 2 demonstrations of the bot to end-users to gather their feedback

- [x] Describe the sprint goal. 

Completion of [Iteration 3](https://gitlab.pg.innopolis.university/k.korikov/iu_rq_self_assessment_bot/-/blob/main/IT%20Prod%20Assignments/Assignment_2/Assignment_2.pdf?ref_type=heads) features.

- [x] Determine what tasks need to be done and who is going to do those tasks. 

Apart from this assignment, there were no management tasks needed during this sprint, next week is uncertain until the next assignment appears.
For now, **Saveliy** implements new features in the bot.
**Kristina** manages overall work, curating tasks priority.
**Kirill** conducts interviews with the end-users

- [x] Execute the sprint. There should be completed sprint artifacts like tasks, code, merge requests, etc. 

●      [Link to a Gitlab](https://gitlab.pg.innopolis.university/k.korikov/iu_rq_self_assessment_bot) 

- [x] Conduct a sprint retrospective. Describe the results of the retrospective.

**What went well:** During that sprint we've learned that feedback from the end-users is highly valuable and had to be collected at the very start.
**What went wrong**: this week's workload didn't allow for an effective communication, so sprint was done mostly blindly.
**Possible improvements**: we still lack communication