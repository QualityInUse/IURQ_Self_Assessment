## Launching the RQ self-assessment bot
To start with, you need to clone the repository:

`git clone https://gitlab.pg.innopolis.university/k.korikov/iu_rq_self_assessment_bot.git`

After that, you need to go to the working directory: 

`cd MainTask`

Create a file `.env`, create a constant `TELEGRAM_BOT_TOKEN` in it (you can get this token from @BotFather or ask @CHSaveliy) and create a constant `GOOGLE_API_KEY`

Then execute the following commands:

`docker build -t rqbot .`

and

`docker run rqbot`

(If you have a problem try run it with VPN)