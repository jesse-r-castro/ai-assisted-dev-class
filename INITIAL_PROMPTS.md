# Prompts Used in the Making of this Software

## The Initial Idea Prompt

This was the initial prompt used to generate the initial structure of REQUIREMENTS.md:

```
You are Senior Product Manager & Technical Architect collaborating with a small team of AI-assisted junior developers in a 90-minute rapid-build workshop.

PROJECT TITLE
“CSV Storyteller Dashboard” – A local-first, Python/Streamlit web app that lets users drop in a CSV, get quick stats & charts, and receive an LLM-generated natural-language summary of the data.

OBJECTIVE
Produce a concise but complete Software Requirements Document (SRD) that developers can follow with minimal back-and-forth during the session.
Keep it short enough to scan in 5 minutes but explicit enough that code can be immediately scaffolded.

OUTPUT FORMAT
Return a single Markdown document with the following numbered sections:

Executive Summary (≤150 words)
Target Users & Primary Use-Cases (bulleted)
Functional Requirements 3.1 File Upload & Validation 3.2 Descriptive Statistics 3.3 Visualization 3.4 Natural-Language Summary 3.5 UI / UX Flow
Non-Functional Requirements (Performance, Security, Portability, Offline fallback)
Technology Stack & Dependencies
API / Module Sketch (function names, key parameters, return types)
Stretch Goals (nice-to-haves if time remains)
Out-of-Scope Items
Acceptance Criteria & Quick Test Plan
Deliverables & Folder Structure
STYLE GUIDELINES
• Use clear, imperative sentences.
• Prefer bullet lists > long paragraphs.
• Include code/folder examples in fenced Markdown blocks.
• Reference concrete packages (e.g., pandas, plotly, openai, Docker).
• Timebox the MVP so it is realistically shippable in 90 minutes by two devs using ChatGPT or similar.
• Ask clarifying questions ONLY if absolutely necessary; otherwise proceed with best-effort assumptions.

CONSTRAINTS TO KEEP IN MIND
• Must run locally with venv but also have a one-shot Dockerfile.
• No external database.
• If offline or rate-limited, the summarizer should fall back to a template-based summary.
• Keep the requirements vendor-neutral (OpenAI, Anthropic, etc. may be swapped).

WHEN READY
Reply with the complete Markdown SRD.

We will write our results to REQUIREMENTS.md
```


## Requirements refinement

Once the initial document was created, it was take through a series of refinements from the point of view of "experts" in their field to make sure the requirements were comprehensive.


### Prompt 1

```
I'd like you to look at this document from the point of view of a very sceptical senior security engineer.  Obviously the BSA that wrote this didn't take security into considertion!  Why would they?!  Your job is to review REQUIREMENTS.md to ensure that the requirements adequately cover security so that our application cannot be used to compromize our security.  Please review the document thoroughly and make any suggested changes per your expertise.  This document has already been reviewed by other experts in their respective fields, so please limit yourself to security topics.
```

### Prompt 2

```
I'd like you to look at this document from the point of view of a very sceptical senior network engineer.  Obviously the BSA that wrote this didn't take our networking structure into considertion!  Why would they?!  Your job is to review REQUIREMENTS.md to ensure that the requirements adequately cover network infrastructure so that our application can be deployed safely and easily across our network.  Please review the document thoroughly and make any suggested changes per your expertise.  This document has already been reviewed by other experts in their respective fields, so please limit yourself to networking topics.  It's entirely possible that previous experts have corrected any issues, so if you don't need to make any changes, please respond with "no changes are needed for networking".
```

### Prompt 3

```
I'd like you to look at this document from the point of view of a very sceptical senior UX engineer.  Obviously the BSA that wrote this didn't take User Experience into considertion!  Why would they?!  Your job is to review REQUIREMENTS.md to ensure that the requirements adequately address UI/UX concerns so that our application can be used by anyone across our global company.  Please review the document thoroughly and make any suggested changes per your expertise.  This document has already been reviewed by other experts in their respective fields, so please limit yourself to UI/UX topics.  It's entirely possible that previous experts have corrected any issues, so if you don't need to make any changes, please respond with "no changes are needed for networking".
```

### Prompt 4

```
I'd like you to look at this document from the point of view of a very sceptical senior devops engineer.  Obviously the BSA that wrote this didn't take Developer Experience and Operations into considertion!  Why would they?!  Your job is to review REQUIREMENTS.md to ensure that the requirements adequately address devops concerns so that our application can be used be easily and safely deployed across the company and that developers are not able to check in unsecure, garbage code and ruin the build.  Please review the document thoroughly and make any suggested changes per your expertise.  This document has already been reviewed by other experts in their respective fields, so please limit yourself to devops topics.  It's entirely possible that previous experts have corrected any issues, so if you don't need to make any changes, please respond with "no changes are needed for devops".
```

### Prompt 5

```
I'd like you to look at this document from the point of view of a very sceptical senior developer.  Obviously the BSA that wrote this didn't take how software needs to be made and developed into considertion!  Why would they?!  Your job is to review REQUIREMENTS.md to ensure that the requirements adequately address technical requirements so that you and your team can actually WRITE this application.  Please review the document thoroughly and make any suggested changes per your expertise.  This document has already been reviewed by other experts in their respective fields, so please limit yourself to general python development topics.  It's entirely possible that previous experts have corrected any issues, so if you don't need to make any changes, please respond with "no changes are needed for developmet".
```

### Prompt 6

```
I'd like you to look at this document from the point of view of a very sceptical senior business manager.  Obviously the BSA that wrote this didn't take usefullness for business operations into considertion!  Why would they?!  Your job is to review REQUIREMENTS.md to ensure that the requirements adequately address any business concerns so that our application can smoothly sail through any approval processes because it will be THAT useful and maximize business value and efficiency THAT much.  Please review the document thoroughly and make any suggested changes per your expertise.  This document has already been reviewed by other experts in their respective fields, so please limit yourself to purely business-oriented topics.  It's entirely possible that previous experts have corrected any issues, so if you don't need to make any changes, please respond with "no changes are needed for business".
```

### Prompt 7

```
I'd like you to look at this document from the point of view of a very sceptical senior AI Engineer.  Obviously the BSA that wrote this didn't take modern AI and LLM technology into considertion!  Why would they?!  Your job is to review REQUIREMENTS.md to ensure that the requirements are in line with modern safe, ethical, effective usage for LLMs.  Please note that while our company Twilio mainly leverages OpenAI and that will be the primary model used, the requirements should allow for configurability with ANY model endpoint as able.  Please review the document thoroughly and make any suggested changes per your expertise.  This document has already been reviewed by other experts in their respective fields, so please limit yourself to purely AI/LLM development topics.  It's entirely possible that previous experts have corrected any issues, so if you don't need to make any changes, please respond with "no changes are needed for AI/LLM technologies".
```

### Prompt 8

```
I'd like you to look at this document from the point of view of a very sceptical senior Architect.  Obviously the BSA that wrote this doesn't understand how detailed a document like this needs to be from the point of view of architecture design!  Why would they?!  Your job is to review REQUIREMENTS.md to ensure that the requirements are in line with modern safe, ethical, effective software architecture principals with a focus on safety and security.  Please review the document thoroughly and make any suggested changes per your expertise.  In particular, please be sure to supplement the document with any needed architecture diagrams using Mermaid syntax.  This document has already been reviewed by other experts in their respective fields, so please limit yourself to purely architectural topics.  It's entirely possible that previous experts have corrected any issues, so if you don't need to make any changes, please respond with "no changes are needed for architecture".
```

### Prompt 9

```
I've had the following experts review the REQUIREMENTS.md document for thoroughness:

1. Security Engineer
2. Network Engineer
3. UX Engineer
4. DevOps Engineer
5. Senior Developer
6. Business Manager
7. AI Engineer
8. Architect

It is entirely possible this constitutes a thorough review of the requirements.  If that is the case, please respond with "I believe the requirements have been reviewed enough".  If you feel they would benefit from further review, please list out who else you feel should review this software.

```

Note: The AI said this was enough review.


## Stakeholder Review

The following prompt is meant to constitute "stakeholder review" of the requirements.  Note: I did this for the first time later in the process than I should have, it should have been done both here AND either right before or right after the first blush of REQUIREMENTS.md was generated (or even both).  Helping the LLM understand your intent will always lead to better results.

```
The initial REQUIREMENTS.md is done!  Now is your opportunity to do a round of feedback with the stakeholder.  Assume the stakeholder understand all the requirements or has people with them that can help them understand and is capable of answering any questions you ask.  Please review the REQUIREMENTS.md document carefully.  Then generate a list of five questions which, if you had their answers, would allow you to improve the REQUIREMENTS.md document to it's maximum effectiveness.  You only get FIVE questions, so please make sure you prioritize and ask only the most important questions.  Please wait for the answers on the questions, and then update the REQUIREMENTS.md document as needed based on the user's answers.  If no updates are needed, please respond with "No updates are needed".
```

The LLM responded with the following:
```


```

Responses:

```


```

### Actual Stakeholder Review

At this point, I thoroughly reviewed the requirements document myself to make sure I'd captured everything I wanted this application to do.  My final response:

```


```


## Cleanup and Generating/Prioritizing User Stories

Now that the requirements have been solidified, we'll restructure the document the document and generate usable user stories.



### Prompt 1

```
I'd like you to look at this document from the point of view of a very sceptical senior BSA.  You took an initial stab at writing REQUIREMENTS.md based on the stakeholders requirements from an intial prompt.  This document was pretty good!  Now, though, the following list of experts has gone through and made a bunch of changes to your beautifully written document:

1. Security Engineer
2. Network Engineer
3. UX Engineer
4. DevOps Engineer
5. Senior Developer
6. Business Manager
7. Open Source Advocate
8. AI Engineer
9. Architect
10. The stakeholder!!!

The requirements are pretty thorough now, but the document may be a mess.  Your job is to review REQUIREMENTS.md to ensure that the document is internally consistent and at LEAST matches all the functionality in the "The Intial Idea Prompt" section of INTITIAL_PROMPTS.md.  It's okay if there is MORE functionality than what is described there but not LESS.  Please review the document thoroughly and make any suggested changes per your expertise.  Please ensure that the document has been streamlined to be well-written, easily-readable, easily-understandable, easily-executable, and will generally lead to the success of the application if followed carefully.

```

### Prompt 2

```
Now that we have solidified our requirements, it's time to leverage your skills as a BSA!  Please thoroughly review the REQUIREMENTS.md document and then convert it into a series of user stories.  The user stories first line should be the commit message we will use for the user story (e.g. feat: Add in the widget library) and should then proceed to describe the functionality required from the requirement in detail as a typical user story (e.g. As a developer, I should be able to use the widget library in the project).  The user stories will be used in an iterative development process as outline in the LLM_INSTRUCTIONS.md document.  Please write the user stories to maximize working with an LLM so that stories are easily achievable using the process outlined in LLM_INSTRUCTIONS.md.  Write the user stories to a file called TODO.md when you're finished.
```

### Prompt 3

Note I wrote this without even reviewing the output just assuming they would be too broad because they are ALWAYS too broad the first time.

```
Great job!  It's my opinion that at least *some* of these stories are too broad a task for an LLM to accomplish using the iterative process we've discussed.  Please review LLM_INSTRUCTIONS.md and TODO.md and further break down the tasks into as atomic a level as possible to maximize LLM success at each step.  Fill in further detail as you see fit as well.  It doesn't matter if there are a LOT of tasks, only that each one is achievable with a round of iteration as outlined in LLM_INSTRUCTIONS.md.  If you are confident this is already done, say "I believe no changes are needed".
```

### Prompt 4

```
This looks really good!  Now, I'd like you to make one final pass over the REQUIREMENTS.md and LLM_INSTRUCTIONS.md documents.  Our goal here is to prioritize the requirements in an order of execution that makes the most sense for our achieving our goals.  Remember that the LLM_INSTRUCTIONS.md calls for things like test-first approach, so take that into account when prioritizing.  It is entirely possible that the current list is properly prioritized from previous steps and no changes are needed.  When the list has been prioritized, please number the list according to it's final priority and then write all the results back to TODO.md.
```

### Prompt 5

```
I think we're done with the requirements phase.  Let's do one final comprehensive review of both REQUIREMENTS.md and TODO.md to make sure that we've "crossed all of our t's and dotted all of our i's" so to speak.  Make sure everything is internally consistent and that TODO.md represents a really good todo list and REQUIREMENTS.md is a really good business requirements document for what we're trying to accomplish as outlined in the "The Intial Idea Prompt" section of INTITIAL_PROMPTS.md.
I expect there will be no further adjustments required, but if you need to make any last minute tweaks, please do so now before I do an initial commit.
```
