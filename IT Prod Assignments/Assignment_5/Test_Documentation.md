To start with, you need to clone the repository. In [README.md](https://gitlab.pg.innopolis.university/k.korikov/iu_rq_self_assessment_bot/-/blob/main/README.md?ref_type=heads) you can read how to do that.
Before you start testing, you need to install the py test module using the commands described below:
`pip install pytest`
or
`pip install --no-cache-dir -r requirements.txt`

Next step is to run the command:

`pytest --cov=MainTask`

After that, you will have a table with the code coverage by tests.