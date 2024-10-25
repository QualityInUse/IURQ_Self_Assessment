# MSD Reading Questions self-assessment bot
## Team members
Kristina Alyabeva - Project manager
Saveliy Chertkov - Developer
Kirill Korikov - Scrum master

[Repository on GitLab](https://gitlab.pg.innopolis.university/k.korikov/iu_rq_self_assessment_bot)
# Review with the customer

- [x] Show your v0 version to the customer. 

Our team meeting with the customer on 10/25/2024.
At the meeting, we demonstrated the results of the development of the last sprint:
- Checking for citations in each question
- The ratio of the number of citations in the response to its volume
- Checking the availability of the References section

- [x] Show any changes to the prototype that you made since the last time and confirm that you understood everything correctly. 

At previous meetings, we did not provide a working product to the customer, so no changes were made. Also, the design of the prototype remained the same.
The customer was satisfied with the functions provided.
The recommendations he offered during the show are:
- To clarify the convenience of the interface among stakeholders (students).
- Specify the three-fold ratio of quotations and text size for users to understand.
- Sort the result by the criticality of the answers. 
- In the future, make separate items for each function in the bot's response.

- [x] Review the most important user stories with the customer. 

The customer evaluated the allocated Usr Stories, and we prioritized them (based on the survey we conducted in Assignment 3). Also, the customer and I have classified some User Stories as Extra, since they are more difficult to implement and may not be developed within the framework of MVP.

- [x] Show the use case diagram to the customer 

In the Use Case Diagram, the customer asked us to display only high level functions (the most useful). He also said that it would be convenient for him to share information about changing functions in the form of a Use Case.

- [x] Review your deployment plan with the customer. 

The customer agrees with our [deployment plan](https://gitlab.pg.innopolis.university/k.korikov/iu_rq_self_assessment_bot/-/blob/main/IT%20Prod%20Assignments/Assignment_4/Deployment%20plan/deployment%20plan.png), it is presented in repository, it is also spelled out below.

- [x] Document all feedback. 
- [x] Agree on further steps and the next meeting.

The next meeting will be held on 1.11.2024. For it, we need to develop the following functions:
- check RQ for answers to all the questions
- check RQ for the presence of an example
- Checking for the length of the question (too long, too short)
- Specify the three-fold ratio of quotations and text size for users to understand.
- Sort the result by the criticality of the answers. 
Non-development steps for the next meeting:
- To clarify the convenience of the interface among stakeholders (students)

# Improve the product vision

- [x] Describe all changes to your product vision after the review with the customer. 

The goal of product development has shifted from checking the accuracy of the answer to the  evaluation criteria described by the TA. According to student surveys, these are the most important points for them. It will also take more time to check the correctness of the answer to the question. This goes beyond MVP.

- [x] Review your project description and identify all the assumptions you made. 
- [x] Make a list of your assumptions. 

During the development of the MSD Reading Questions self-assessment bot, we made the following assumptions:
- The response length values we have chosen are the norm. 
- The ratio of references to the length of the response we have chosen is the norm
- We assume that everyone will use our template for RQ
- Prioritized functions

- [x] Create an approximate plan of how you are going to test those assumptions. 

- **The response length values we have chosen.** 
  The assumption is made based on the [criteria for RQ](https://moodle.innopolis.university/pluginfile.php/209803/mod_resource/content/8/RQs_evaluation-criteria_2024.pdf).
  
- **The ratio of references to the length of the response we have chosen.**
  The assumption is made based on personal experience of receiving comments "Surse?" after checking the RQ.
  
- **We assume that everyone will use our template for RQ**
  The bot will offer a [template](https://drive.google.com/drive/u/2/folders/11hyrJl_fWnK9zqjehSj7tw_ImVztiGn-) for RQ. Otherwise, errors may occur when parsing the document. This can lead to incorrect results.

- **Prioritized functions** was tested using a [survey](https://gitlab.pg.innopolis.university/k.korikov/iu_rq_self_assessment_bot/-/blob/main/IT%20Prod%20Assignments/Assignment_3/Questionnaire%20results/Questionnaire_results.png) of students and TA

- [x] Use the GQM model. List all the goals of your project, identify related questions, and plan metrics. 

 [GQM](https://gitlab.pg.innopolis.university/k.korikov/iu_rq_self_assessment_bot/-/blob/main/IT%20Prod%20Assignments/Assignment_4/GQM/GQM.pdf)  of product presented in the repository

- [x] Describe quality attributes that matter for the project. You can use ISO 25010 for inspiration but make sure the customer really cares about those attributes. 

The quality attributes for our project are:
- Usability
  It is important for students to quickly understand how to use our bot. It is important that students quickly check the RQ in the bot and it does not cause them unnecessary inconvenience.
- Functional Suitability
  It is important that all specific tasks are covered. The bot should leave as accurate a result as possible so that it helps to correct the flaws before checking. Otherwise, it will be pointless for students to use it.
- Portability
  It is important to describe exactly how to install the bot, since we are not considering hosting on the server yet. The bot will run locally and it is important to simplify this step as much as possible.

- [x] Describe what steps you need to take to ensure those quality attributes. 

- Usability
  To make life user-friendly, we have a "\help" command that explains how to use the bot. Also, this command will contain all the other amandas that can be used.
  The bot will also have buttons for the main commands that simplify use.
  To display the bot's response, we will conduct a survey among students. This way we will learn how to better display the verification result.
- Functional Suitability
  To compile the necessary functions and their priority, a [survey](https://docs.google.com/forms/d/e/1FAIpQLSeGG94EoyKNWZBXyK3YFLdsgatf5CuFDcln55fxoOM3x3-bpQ/viewform) was compiled among students and TA. Based on this survey, we have divided the functions by development [priorities](https://gitlab.pg.innopolis.university/k.korikov/iu_rq_self_assessment_bot/-/blob/main/IT%20Prod%20Assignments/Assignment_4/Deployment%20plan/deployment%20plan.png).
  The evaluation result of the Bot will be based on our experience of receiving feedback on RQ. The requirements document is also taken into account.
- Portability
  For ease of installation, each step is spelled out in [README.md](https://gitlab.pg.innopolis.university/k.korikov/iu_rq_self_assessment_bot/-/blob/main/README.md) the project

- [x] Create an architectural view of your product.

[Architectural view](https://gitlab.pg.innopolis.university/k.korikov/iu_rq_self_assessment_bot/-/blob/main/IT%20Prod%20Assignments/Assignment_4/Architecture_Diagram/architectureVIsion.png) of product presented in the repository

# Sprint cycle

- [x] Review changes that need to be made based on your improved product vision. 

Improved product vision discussed below.

- [x] Review your strategic plan. Are you still on track? Does it need to be modified? Update your plan if needed. 

Progress towards the [goal](https://gitlab.pg.innopolis.university/k.korikov/iu_rq_self_assessment_bot/-/blob/main/IT%20Prod%20Assignments/Assignment_2/Assignment_2.pdf?ref_type=heads), described in a strategic planning, is assessed with the weekly reviews with a customer who also is a “professor” user in our project.

[Roadmap](https://gitlab.pg.innopolis.university/k.korikov/iu_rq_self_assessment_bot/-/blob/main/IT%20Prod%20Assignments/Assignment_2/Assignment_2.pdf?ref_type=heads) iterations were not followed fully. Customer review proved the “coherence” check of an answer to be too hard given the team resources. References count check from Iteration 2 was implemented instead of the answer length check from Iteration 1.

Other tasks were completed in time, so overall plan is fine.

- [x] Review your sprint process and determine what can be improved to support the quality goals of your project. Look at the results of your previous sprint retrospective. Decide how you are going to improve this sprint based on that retrospective. 

Current sprint process satisfies the team needs, though, concrete days of various steps are still not solidified. This brings some chaos into the developmen processt, but is not deemed critical, given the team size and responsibilities distribution.

By the results of previous retrospection, our team had decided to seek help in conducting customer interviews (in form of personal meeting with a professor), and after following the obtained pieces of advice, have noticed the improvement in this week’s interview results.

Feedback from the review team on the previous assignment shed light on a mistake in our sprint retrospection structure, that feedback was accepted. Review team also noted lack of information about daily meetings that are a part of Sprint process. Our team has no need in daily meetings, because this project is not our only one in this semester, so it’s not possible for us to make daily increments.

- [x] Conduct sprint planning. 

Sprint planning was done in the Telegram call once again, the following plans were written in team chat after that (tasks, related to the assignments are omitted here):
Kirill:
-  By Thursday, conduct 2 interviews with fellow students, asking about bot’s interface clarity and value, that they expect from the bot (this task includes preparing the questions and materials to show beforehand).
- Make 10 user personas by Monday.
Saveliy:
- By Friday, Implement all the features for the [user stories](https://gitlab.pg.innopolis.university/k.korikov/iu_rq_self_assessment_bot/-/blob/main/IT%20Prod%20Assignments/Assignment_3/User%20Stories/photo_2024-10-25_14-57-18.jpg) ([Miro](https://miro.com/app/board/uXjVLUNM4P8=/)), marked with yellow.
Kristina: (both tasks by Friday)
- Fix the use-case diagram, based on the feedback from the customer.
- Update the product vision document.

- [x] Describe the sprint goal. 

Goal of this sprint is the completion of [Iteration 2](https://gitlab.pg.innopolis.university/k.korikov/iu_rq_self_assessment_bot/-/blob/main/IT%20Prod%20Assignments/Assignment_2/Assignment_2.pdf?ref_type=heads) with some changes being made (Length check must be implemented instead of references check).

- [x] Determine what tasks need to be done and who is going to do those tasks. 
- [x] Execute the sprint. There should be completed sprint artifacts like tasks, code, merge requests, etc. 

Sprint described here is planned to be done by the end of next Friday (01.11.24).

- [x] Conduct a sprint retrospective. Describe the results of the retrospective

Due to a newfound discrepancy with the assignments deadlines, current retrospection had to be rescheduled to be conducted right after the review with a customer. Feedback from the reviewing team from the previous assignment was also taken into an account to better structure the sprint retrospection.
What went well: review+interview with a customer; implementation progress.
What went wrong: initial plan was not followed due to discrepancy with the assignments deadlines.
Possible improvements: current development process lacks strict structure and communication between team members.

# Product iteration

- [x] Implement changes that were planned during the sprint

[Repository on GitLab](https://gitlab.pg.innopolis.university/k.korikov/iu_rq_self_assessment_bot)