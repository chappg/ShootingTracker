# ShootingTracker
This is the implementation of the Alexa Shooting Tracker skill: https://www.amazon.com/Backwards-Working-LLC-Shooting-Tracker/dp/B0B529SFZ7/


## Step 1: Log in
To get started, log into the  [Alexa developer console](https://developer.amazon.com/alexa/console/ask)  with your Amazon Developer account. If you do not have an account,  [click here](https://www.amazon.com/ap/register?clientContext=131-0331464-9465436&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&siteState=clientContext%3D142-6935021-1894360%2CsourceUrl%3Dhttps%253A%252F%252Fdeveloper.amazon.com%252Falexa%2Csignature%3Doyixlki7Yxz8bRUtt4vGJ4EugQ8j3D&marketPlaceId=ATVPDKIKX0DER&language=en_US&pageId=amzn_developer_portal&openid.return_to=https%3A%2F%2Fdeveloper.amazon.com%2Falexa&prevRID=HSRBQ1KHA4E5D1PBHPPP&openid.assoc_handle=mas_dev_portal&openid.mode=checkid_setup&prepopulatedLoginId=&failedSignInCount=0&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0)  to create one.


## Step 2: Create your skill

**a.** Click **Create Skill** on the right-hand side of the console. A new page displays.

![](https://d3ogm7ac91k97u.cloudfront.net/content/dam/alexa/alexa-skills-kit/get-deeper/tutorials/cake-time-2/1b.png)


**b.** In the **Skill name** field, enter **Shooting Tracker*.

**c.** Leave the **Default language** set to **English (US)**.

**d.** You are building a custom skill. Under **Choose a model to add to your skill**, select **Custom**.

![](https://d3ogm7ac91k97u.cloudfront.net/content/dam/alexa/alexa-skills-kit/get-deeper/tutorials/cake-time-2/1d.png)

> **Skills have a front end and backend. The front end is where you map utterances (what the user says) into an intent (the desired action). You must decide how to handle the user’s intent in the backend. Host the skill yourself using an    function or HTTPS endpoint, or choose Alexa to host the skill for you. There are limits to the AWS Free Tier, so if your skill goes viral, you may want to move to the self-hosted option. For this course, choose Alexa-Hosted (Python).**

**e.** Under **Choose a method to host your skill’s backend resources**, select **Alexa-Hosted (Python)**.

![](https://d3ogm7ac91k97u.cloudfront.net/content/dam/alexa/alexa-skills-kit/get-deeper/tutorials/cake-time-2/1e.png)

**f.** At the top of the page, click **Create skill**.


![](https://d3ogm7ac91k97u.cloudfront.net/content/dam/alexa/alexa-skills-kit/get-deeper/tutorials/cake-time-2/1f.png)

> **It takes a few moments for AWS to provision resources for your skill. When this process completes, move to the next section.**

>![](https://d3ogm7ac91k97u.cloudfront.net/content/dam/alexa/alexa-skills-kit/get-deeper/tutorials/cake-time/3/building-a-skill-2f-2.png)

> **Note: When you exit and return to the Alexa developer console, find your skill on the Skills tab, in the Alexa Skills list. Click Edit to continue working on your skill.**

> ![](https://d3ogm7ac91k97u.cloudfront.net/content/dam/alexa/alexa-skills-kit/get-deeper/tutorials/cake-time-2/building-a-skill-2f-3.png)

## Step 3: Merge the Shooting Tracker Code


> **Merge the Shooting Tracker files in the interactionModels, lambda, and tst directories.**

## Step 4: Execute the tests and make your own submissions!
