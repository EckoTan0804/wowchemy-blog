---
# ===== Title, summary, and position in the left sidebar =====
linktitle:  # Title shown in the left sidebar menu
summary:  # Summary of this post
weight: 410
# ============================================================

# ========== Basic metadata ==========
title: CI/CD
date: 2022-05-11
draft: false
type: book # page type
authors:
  - admin
tags:
  - Software Engineering
  - Best Practice
  - CI/CD
categories:
  - Software Engineering
toc: true # Show table of contents
# ====================================

# ========== Advanced metadata =========
profile: false  # Show author profile?
reading_time: true # Show estimated reading time?
share: true  # Show social sharing links?
featured: true
comments: true  # Show comments?
disable_comment: false
commentable: true  # Allow visitors to comment? Supported by the Page, Post, and Book content types.
editable: false  # Allow visitors to edit the page? Supported by the Page, Post, and Book content types.

# Optional header image (relative to `assets/media/` folder).
header:
  caption: 
  image:  
---

{{< figure src="https://raw.githubusercontent.com/EckoTan0804/upic-repo/master/uPic/cicd.svg.imgo.svg" caption="CI/CD (Source: [Synopsys](https://www.synopsys.com/glossary/what-is-cicd.html))" numbered="true" >}}





## What is CI/CD?

- A method to frequently deliver [apps](https://www.redhat.com/en/topics/cloud-native-apps) to customers by introducing [automation](https://www.redhat.com/en/topics/automation) into the stages of [app development](https://www.redhat.com/en/topics/cloud-native-apps/why-choose-red-hat-cloud-native).
  - **CI** = **C**ontinuous **I**ntegration
  - **CD** = **C**ontinuous **D**elivery and **D**eployment
- Introduces ongoing automation and continuous monitoring throughout the [lifecycle of apps](https://www.redhat.com/en/topics/devops/what-is-application-lifecycle-management-alm), from integration and testing phases to delivery and [deployment](https://www.redhat.com/en/topics/automation/what-is-deployment-automation). 

### Continuous Integration (CI)

- An automation process for **developers**
  - New code changes to an app are regularly built, tested, and merged to a shared repository.
- This process is automated to ensure that teams can build, test, and package their applications in a reliable and repeatable way.
- Helps streamline code changes, thereby increasing time for developers to make changes and contribute to improved software.
- A solution to the problem of having too many branches of an app in development at once that might conflict with each other.

### Cotinuous Delivery and/or Deployment (CD)

- **[Continuous delivery](https://www.synopsys.com/glossary/what-is-continuous-delivery.html)**
  - The automated delivery of completed code to environments like testing and development. 
    - *I.e.*, a developer’s changes to an application are automatically bug tested and uploaded to a repository
  - Provides an automated and consistent way for code to be delivered to these environments.
- [**Continuous deployment**](https://www.synopsys.com/glossary/what-is-continuous-development.html) 
  - Next step of continuous delivery
  - Every change that passes the automated tests is automatically placed in production, resulting in many production deployments.
  - Addresses the problem of overloading operations teams with manual processes that slow down app delivery

{{% callout note %}}
They are related concepts that sometimes get used interchangeably. Both are about automating further stages of the pipeline, but they’re sometimes used separately to illustrate just how much automation is happening.
{{% /callout %}}

### Difference between CI and CD

CI is a set of practices performed *as developers are writing* code, and CD is a set of practices performed *after* the code is completed.

## How CI/CD pipeline works?

The CI/CD pipeline works like an infinity loop:

{{< figure src="https://raw.githubusercontent.com/EckoTan0804/upic-repo/master/uPic/cicd.svg.imgo.svg" caption="CI/CD (Source: [Synopsys](https://www.synopsys.com/glossary/what-is-cicd.html))" numbered="true" width="80%">}}

1. Developers write the **code**
2. **Build** or compile the code
3. **Test** the code for bugs
4. **Release** the code if all tests are passed
5. **Deploy** the change in production
6. End users or customers **operate** the new change
7. Project owner or project manager monitors and gets feedback
8. **Plan** the next step based on the feedback
9. Back to step 1: Write code based on the plan

## Why is CI/CD Important?

- Allows organizations to ship software quickly and efficiently. 
- Facilitates an effective process for getting products to market faster than ever before, continuously delivering code into production, and ensuring an ongoing flow of new features and bug fixes via the most efficient delivery method. 

## Benefit of CI/CD

- Automated testing enables continuous delivery, which ensures software **quality** and **security** and increases the **profitability** of code in production.
- CI/CD pipelines enable a much **shorter time to market** for new product features, creating happier customers and lowering strain on development.
- The **great increase in overall speed of delivery** enabled by CI/CD pipelines improves an organization’s competitive edge.
- Automation **frees team members** to focus on what they do best, yielding the best end products.
- Organizations with a successful CI/CD pipeline can attract great talent. By moving away from traditional [waterfall methods](https://en.wikipedia.org/wiki/Waterfall_model), engineers and developers are no longer bogged down with repetitive activities that are often highly dependent on the completion of other tasks. 

##Reference

- [What is CI/CD?](https://www.redhat.com/en/topics/devops/what-is-ci-cd)

- [CICD](https://www.synopsys.com/glossary/what-is-cicd.html)

- Video tutorials

  - DevOps CI/CD Explained in 100 Seconds

    {{< youtube scEDHsr3APg>}}

  - CI/CD Explained | How DevOps Use Pipelines for Automation

    {{< youtube M4CXOocovZ4>}}

​		