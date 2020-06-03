# [Integrating Ansible with Jenkins in a CI/CD process](https://www.redhat.com/en/blog/integrating-ansible-jenkins-cicd-process)
The aim of this post is to demonstrate how to use Ansible for environment provisioning and application deployment in a Continuous Integration/Continuous Delivery (CI/CD) process using a Jenkins Pipeline.

The purpose of using Ansible in the pipeline flow is to reuse roles and Playbooks for provisioning, leaving Jenkins only as a process orchestrator instead of a shell script executor.

The tools used to create the examples for this post are:
-   Vagrant and libvirt to create the infrastructure for this lab
-   SonarSource to bring up quality analysis to the CI/CD process
-   Maven to set and deploy the Java project
-   GIT for source code management and control
-   Nexus is the repository for artifact binaries
-   Jenkins to orchestrate the CI/CD pipeline flow
-   And finally, Ansible to create all infrastructure for this lab and the to provision the application

Architectural elements:
-   Github is where our project is hosted and where Jenkins will poll for changes to start the pipeline flow.
-   SonarSource is our source code analysis server. If anything goes wrong during the analysis (e.g. not enough unit tests), the flow is interrupted. This step is important to guarantee the source code quality index.
-   Nexus is the artifact repository. After a successful compilation, unit tests and quality analyses, the binaries are uploaded into it. Later those binaries will be downloaded by Ansible during the application deployment.
-   The Ansible Playbook, which is a YAML file integrated in the application source code, deploys the Spring Boot App on to a CentOS machine.
-   Jenkins is our CI/CD process orchestrator. It is responsible to put all the pieces together, resulting in the application successfully deployed in the target machine.

https://plugins.jenkins.io/ansible/