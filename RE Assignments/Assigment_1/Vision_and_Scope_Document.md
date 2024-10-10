# 1 Business Requirements
## 1.1 Background

The MSD Reading Questions self-assessment bot is driven by the need to create a self-assessment tool for the Managing Software Development (MSD) discipline. During the preparation of their homework, students may encounter little feedback, which makes it difficult not only to correct their answers, but also to deepen their understanding of the material before submitting the work to the instructors for review.

The lack of immediate, structured feedback often results in students overlooking key aspects of an assignment that require revision. This highlights the importance of creating a system that can provide students with analyses of responses.

The MSD RQ Assessment Bot will provide students with the resources they need to improve themselves and deepen their skills.The bot will not only improve final grades, but also promote a deeper understanding of the material.

## 1.2 Business Opportunity

To date, no direct competitors have been identified that solve a similar problem. However, the market analysis has identified several indirect competitors that solve related problems. The table provides a competitive analysis.


|               | Answer is too short/long | Irrelevant to the question | Unclear question | Incoherent | Missing example | GPT generated | Spell check |
| ------------- | :----------------------: | :------------------------: | :--------------: | :--------: | :-------------: | :-----------: | :---------: |
| Grammarlly    |            -             |             -              |        -         |     ±      |        -        |       +       |      +      |
| ProWritingBot |            -             |             -              |        -         |     ±      |        -        |       -       |      +      |
| Quillbot      |            -             |             -              |        -         |     ±      |        -        |       +       |      +      |
| GPT-4         |            +             |             ±              |        +         |     +      |        ±        |       ±       |      +      |
| Gemini        |            +             |             ±              |        +         |     +      |        ±        |       ±       |      +      |

### 1.2.1 Grammarly
[Grammarly](https://www.grammarly.com) is a tool that helps students check their work from a grammatical point of view. The main features include checking spelling and punctuation, analysing text for incoherence and stylistic errors, and identifies AI-generated text. While Grammarly offers useful features to improve clarity and literacy, it does not have tools that evaluate the content of an answer, making it not a complete solution to the task of self-assessing reading quesstions.

### 1.2.2 ProWritingAid
[ProWritingAid](https://www.prowritingaid.com/) is a tool similar to Grammarly that helps students check their answers in terms of grammar. It lacks the function of identifying AI-generated text, but it has more literacy-enhancing features. 

### 1.2.3 Quillbot
[Quillbot](https://quillbot.com/)  is an information system, just like the previous one designed to improve the grammatical aspects of students' texts. This system includes paraphrasing and grammar checking tools to help improve the clarity of answers. There is also a tool to check for the presence of AI generated text, but there are no tools to check the meaningfulness of the answers.

### 1.2.4 GPT-4
[GPT-4](https://chatgpt.com/) is an intelligent system that can help students with assessment not only in terms of grammar but also in terms of logic, content and clarity. This system is able to improve the structure of the answer, can point out flaws in the reasoning, and can suggest options for improvement. But this system can often make mistakes and can end up confusing the student.

### 1.2.5 Gemini
[Gemini](https://gemini.google.com/) is an intelligent system that works in a similar way to ChatGPT. It can analyse the answer not only from a grammatical point of view, but also evaluate the agrumentation of the answer and help clarify unclear points. But at the same time, this system can make mistakes and confuse the student even more.

## 1.3 Business Objectives
The main business objectives of this project are related to reducing the time spent on the assessment of student work, as well as improving the performance of the Managing Software Development discipline. MSD Reading Question self-assessment Bot will provide value to students and instructors through the following objectives:
- **Problem with user perception:** Student acceptance of the new self-assessment system may be slow if the performance does not meet expectations or is not useful.
- **Improving Student Achievement:** Providing students with instant feedback will improve the quality of their answers before they are sent to the instructor for evaluation.
- **Expected product release date:** We plan to deliver an MVP by 6 December 2024.
## 1.4 Success Metrics
The success of the project will be measured using the following key indicators:
- **Assistants' survey:** Our team will conduct a survey among TAs to assess their opinion on the quality of the work assessment provided by the system. The survey will include questions on how well the bot's conclusions correspond to the TA's assessments.
- **Utility Metrics:** Our team will conduct a survey among students who will describe their experience of using this system, how useful the feedback the bot provided on the assignment, and how much the bot helped improve the quality of students' work.
## 1.5 Vision Statement
The goal of our MSD Reading Question Bot project is to create a tool that can improve the quality of mastering Managing Software Development material. 
With the help of our product, students will be able to assess their work in advance, identify weaknesses and receive recommendations for improvement, which will lead to a better understanding of the course material, as well as to a higher quality of work done.
Our product will support students to continuously improve their skills in Managing Software Development.
## 1.6 Business Risks
During the system development process, the following key business risks were identified that could affect the success of the project:
- **Problem with user perception:** Student acceptance of the new self-assessment system may be slow if the performance does not meet expectations or is not useful.
  **Risk severity:** High
  **Market Reduction Measures:** Conduct testing with small groups of students to get feedback on product improvements prior to final release. 
- **Market competition:** Although there are no direct competitors, there are indirect competitors such as Grammarly, ChatGPT and other assessment systems that may offer similar features. This can reduce interest in a product if it does not offer unique features or good quality.
  **Risk severity:** Medium.
  **Market Reduction Measures:** Continuous improvement of bot functionality, better analysis of response content.
- **Difficulties in releasing on schedule:** Failure to release the product as planned may lead to a decrease in user confidence.
  **Risk severity:** Medium.
  **Market Reduction Measures:** Clear planning of development phases, continuous monitoring of the development process and readiness to troubleshoot any problems encountered.
## 1.7 Business Assumptions and Dependencies
### 1.7.1 Business Assumption
- **Availability of source data:** It is expected that we will have a sufficient number of graded student papers to train the system.
- **Positive perceptions from students:** Students are expected to use the bot as a self-checking tool, and they are expected to trust the system's recommendations to improve their papers.
### 1.7.2 Business Dependencies
- **Dependence on external technologies:** The successful operation of the system will require the use of third-party technologies, which means that any errors or changes to them may affect the system's performance.
- **Dependence on user feedback and support:** In the absence of feedback or with little or no feedback, system improvement and adaptation may slow down or not occur at all.
# 2 Scope and Limitations
## 2.1 Major Features
1. Student can submit their RQ assignment.
2. Automatic inspection of the RQ assignments, submitted by students, for compliance with grading criteria, using AI-model.
3. Return of the inspection results to the user.
4. AI-generated content check.
## 2.2 Scope of Initial Release
-  Self-hosted bot with working AI-model.
- Student can submit their RQ assignments to the Self-Assessment bot by choosing them locally during the interaction with a bot.
- Bot is able to accept only PDF files.
- Parsing of the PDF files to "question-answer" pairs.
- Inspection of the following answer criteria: length, references, coherence, relevance to the question.
- Inspection of the page limit, title formatting, references page.
- Return of the comments for each question-answer pair with results of the inspection. 
## 2.3 Scope of Subsequent Releases
- Telegram bot hosted on a server.
- Return of the inspection results in form of the PDF file with comments, highlighting problematic parts of the text.
- Additional answer criteria checks: all necessary definitions are given, all assumptions are clearly stated before they appear, example is given.
- Potential accuracy improvement of "coherency" and "relevance" criteria inspections.
- Inspection of the question formatting.
## 2.4 Limitations and Exclusions
- Inspection of the "specific enough" criteria for the answer.
- Return of the comments on how to improve the answers.
- Inspection by this product won't replace the real inspection by the TA/Professor.
# 3 Business Context
## 3.1 Stakeholder Profiles

| Stakeholder | Major Value                                                    | Attitudes                                                                                                                                                                                        | Major Interests                                                     | Constraints                                                                |
| ----------- | -------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------- | -------------------------------------------------------------------------- |
| Students    | 1. Increasing the accuracy of answers   2. Improved formatting | • Peace of mind while waiting for the final assessment.<br>•No waiting for an assessment, and saving time on searching for the right criteria in the  document.<br>• Minimizing format problems. | Improving grades                                                    | Distrust of NLP and unwillingness to fix the errors pointed out by the bot |
| Tutors      | Automating part of the work                                    | The speed of verification, you can double-check only the answers to which the bot did not give negative comments or questions with which it does not agree on the bot's feedback.                | Reducing the verification time                                      | Distrust of the results of the bot, checking everything yourself           |
| Professor   | Automating<br>part of the<br>work                              | Objectivity in evaluating or rechecking the work. they can refer to two sources of evaluation.                                                                                                   | Reduction of dissatisfaction based on the results of the assessment |                                                                            |
## 3.2 Project Priorities


| Dimension  |      Driver (state objective)       |                    Constrain (state limits)                     |      Degree of Freedom (state allowable range)      |
| :--------: | :---------------------------------: | :-------------------------------------------------------------: | :-------------------------------------------------: |
| *Schedule* | MVP to be available by December 6th |                                                                 |                                                     |
| *Features* |                                     |                                                                 |      80%-90%  features must be included in MVP      |
| *Quality*  |                                     |                                                                 | 90%-95% of user acceptance things must pass for MVP |
|  *Staff*   |                                     |            Maximum team size is 1PM and 2 developers            |                                                     |
|   *Cost*   |                                     | The project does not provide for external financial investments |                                                     |
## 3.3 Deployment Considerations

MVP will be deployed locally on users' PCs via Docker Compose. To do this, the user will need to have a telegram account, as well as the latest version of Telegram and the startup file. Detailed deployment documentation will be written later, during product development.