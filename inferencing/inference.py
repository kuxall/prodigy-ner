import spacy

from time import perf_counter

nlp = spacy.load(r"/home/kushal/Dropbox/sherpa codes/services/data annotations/dolphin/test/model/2023-02-06_model/2023-02-06_test_model/model-best/")

def extract_entities(text):
    doc = nlp(text)
    entities = [(ent.text, ent.label_) for ent in doc.ents]
    return entities

if "__main__" == __name__:
	start = perf_counter()
	text = """Professional Summary: 7 years of experience in IT industry comprising of Linux System Administration, DevOps Engineering, and in automating, building, releasing of code from one environment to other environment and deploying to servers. Extensive experience includes SCM, AWS, DevOps, Build/Release Management, Cloud Management and Containerization. Strong experience on AWS platform and its dimensions of scalability including EC2, S3, EBS, VPC, ELB, AMI, SNS, RDS, IAM, Route 53, Auto scaling, Cloud Front, Cloud Watch, Cloud Trail, Cloud Formation, Terraform, OPS Work, Security Groups. Experienced in working on DevOps/Agile operations and tools area (Build & Release Automation, Environment Service). Well versed with Open stack-based cloud infrastructure. Developed and maintained tasks using shell scripts to integrate Open Stack components with Open Contrail (Networking Component) consequently optimizing the essential services. Competent extent of skills on DevOps essential tools like Chef, Puppet, Ansible, Docker, Subversion (SVN), GIT, Hudson, Jenkins, Ant, Maven. Ensured data integrity and data security on AWS technology by implementing AWS best practices. Ability to identify and gather requirements to define a solution to be built and operated on AWS. Provisioning of AWS instances with Jenkins plans and Ansible, using zookeeper. Used Python fabric for AWS instance provisioning. Extensively experienced in Bash, Perl, Python, Ruby scripting on Linux. Used Python libraries like Beautiful Soap and SQL Alchemy and Wrote Python scripts to parse JSON documents and load the data in database. Experienced in Branching, Merging, Tagging and maintaining the version across the environments using SCM tools like GIT and Subversion (SVN) on Linux platforms. Integration, deployment and automation of application servers Tomcat, WebLogic across Linux platforms. Set up Continuous Integration pipelines for major releases in Jenkins. Implemented Puppet modules to automate the installation and configuration for a broad range of services. Well versed with many different concepts of Chef like Roles, Environments, DataBags, Knife, and Chef Server Admin/Organizations. Implemented Chef Recipes for Deployment on build on internal Data Centre Servers. Also re-used and modified same Chef Recipes to create a Deployment directly into Amazon EC2 instances. Mainly used Chef for server provisioning and automating infrastructure. Development and version control of Chef Cookbooks, testing of Cookbooks using Food critic and Test Kitchen and running recipes on nodes managed by on premise Chef Server. Explicit knowledge on Ansible Playbooks, modules and roles. Experienced with build automation tools like Ant and Maven. Practical Knowledge in using Bug Tracking tools like JIRA and HP Quality center. Experienced with Docker container service and dockerized various applications by creating Docker images from Dockerfile. Used kubernetes to deploy scale, load balance, scale and manage docker containers with multiple name spaced versions Experienced in administrating, deploying and managing UBUNTU and CentOS servers. Strong influenced skills in Agile Testing Methodologies & Software Test Life Cycle (STLC). Extensive experience in UNIX performance tuning and Capacity Planning. Experience in deploying system stacks for different environments like Dev, UAT, and Prod in both on premise and cloud infrastructure. Good analytical, problem solving, communication skills and have an ability to work either independently with little or no supervision or as a member of a team. Excellent written and verbal communication skills, strong organizational skills, and a hard-working team player Operating Systems Linux (Centos/ Redhat), WINDOWS Server, Mac Version Control Tools SVN, Git, Git Hub, Git Lab Programming Languages Bash, Perl, Python, Ruby Databases MySQL, Oracle, Cassandra, NoSQL DB. Application/Web Servers WebLogic, JBoss, Tomcat, Jetty, Nginx Build Scripting Tools Ant, Maven, Gradle CI/ Other Tools Jenkins, Team City, Bamboo, TFS, Gerrit, Zabbix, Yum Infrastructure Tools VMware, KVM, Chef, Puppet Enterprise, Foreman, Apache Lib cloud, Google Cloud, AWS Programming Languages C, C++, Perl scripting, Shell scripting, Groovy, Python, SQL, Java/J2EE, .Net, Ruby, Bash,. Technical Skill Wells Fargo, Des Moines, IA							Sep 2016 – Till date DevOps/AWS Engineer Responsibilities: Involved in designing and deploying multitude applications utilizing almost all AWS stack (Including EC2, Route53, S3, RDS, Dynamo DB, SNS, SQS, IAM, ELK) focusing on high-availability, fault tolerance, and auto scaling in AWS Cloud Formation. Configured AWS IAM and Security Group in Public and Private Subnets in VPC. Created AWS Route53 to route traffic between different regions. Configure and administrate source code repositories for enterprise projects (BitbucketGit). Strong experience utilizing Jenkins for enterprise scale infrastructure configuration and application deployments - checking out code from SVN/Bitbucket and use ant/maven to build war/jar artifacts. Assisted customer in implementing DevOps strategies using Jenkins for automated deployment of builds to different environments and Build Forge as the automated engine. Built Jenkins jobs to create AWS infrastructure from GitHub repos containing Terraform code Worked on Project-Generator which creates Jenkinsfile and seed jobs in Jenkins and Rundeck jobs with job definitions. In this webhooks also configured when the commits done in Bitbucket and jobs are triggered in Jenkins. Installed and configured GIT and communicating with the repositories in BitBucket repository Built Continuous Integration and Continuous delivery environment in Jenkins. Prototype CI/CD system with Bitbucket on GKE utilizing kubernetes helm and Docker for the runtime environment for the CI/CD systems to build and test and deploy. Configured RDS instances using Cloud formations and Terraform and used Terraform to map more complex dependencies and identify network issue. Installed and managed kubernetes applications using helm. Utilized Configuration Management Tools like Terraform, Ansible& Chef. Written Chef recipes in Cookbooks for various DB configurations to modularize and optimize product configuration, converting production support scripts to Chef Recipes and AWS server provisioning using Chef Recipes. Given support for AWS/DevOps. For maintaining the High Availability and maintaining the high durability. Developing and maintaining playbooks for software package installations and configuration management using Ansible. Manage AWS EC2 instances utilizing Auto Scaling, Elastic Load Balancing and Glacier for our QA and UAT environments as well as infrastructure servers for Bitbucket and Chef. Used AWS Beanstalk for deploying and scaling web applications and services developed with Java, PHP, Node.js, Python, Ruby, and Docker on familiar servers such as Apache, and IIS. Configured plugins for the integration tools to the version control tools. Used ANT and MAVEN as a build tools on java projects for the development of build artifacts on the source code. Experience in creating Docker containers leveraging existing Linux Containers and AMI's in addition to creating Docker containers from scratch. Worked on creation of custom Docker container images, pushing the images and Docker consoles for managing the application life cycle. Skilled in monitoring servers using Nagios, Data dog, Cloud watch and using ELK Stack Elastic Search Logstash. Writing new plugins in Nagios to monitor resources. Working in implementation team to build and engineer servers on Ubuntu and RHEL Linux. Provisioning virtual servers on VMware and ESX servers using Cloud. Environment: Amazon AWS Services, Docker, Kubernetes, Oracle Virtual Box, Subversion (SVN), GIT, GIT Hub, SOA, Oracle Fusion middle ware, OSB, ANT, Maven, Jenkins, Shell Scripts, Ruby, XML, python (BOTO API), Linux administration Apache, MySQL, JIRA, SOA, MS build and NANT. Kankai Technology Network and Research Center Pvt. Ltd. Sifal, Kathmandu, Nepal						       Jan 2015 To June 2016 DevOps Engineer Responsibilities: Used SVN as source code repository. Created and maintained the Shell/Perl deployment scripts for Web logic and UNIX servers. Analyzed the ANT Build projects for conversion. Converting the ANT Build projects to Maven Build projects. Developing the Maven build scripts (pom.xml's). Managed Maven project dependencies by creating parent-child relationships between projects. Configuring and Administering the Jenkins Continuous Integration servers. Created end to end build automation and CI setup for button click push deployment. Creating new build jobs, Integration testing jobs and deploy jobs in Jenkins to automate the process. Implemented &maintained the branching and build/release strategies utilizing Subversion in Linux environments. Performed all necessary day-to-day Subversion support for different projects like Check-in, Checkouts, import, export, branching, tagging, and conflict resolution. Maintained History of all the repositories using Subversion. Extensive usage of TortiseSVN in Windows environment for version control activities. Involved in the bare metal provisioning of the new servers using DHCP/TFTP/PXE-server boot and DNS configuration of the new servers. Installed and Configured the Apache Tomcat application servers for Dev and Integration Test Environments. Installed and configured Nexus Repository Manager to share the artifacts between the teams within the company. Automated the process of deployment to Apache Tomcat Application Servers by developing Python Scripts. Worked in Agile Project management Process. Built and Deployed Java/J2EE to Tomcat Application servers in an agile continuous integration process and automated the entire process. Involved in periodic archiving and storage of the source code for disaster recovery. Developed, maintained, and distributed release notes for each scheduled release. Worked with JIRA for Issue Tracking and monitoring. Worked with the Architects on SDLC process being the owner of post development environments. Coordinated the resources by working closely with Project Managers for the release and carried deployments and builds on various environments using continuous integration tool. Environment: Subversion, .Net, Java, GIT, Jenkins, Python, PHP, Linux, Apache, Maven, MySQL, JSP, XML, Clear Quest, DB2 and Web logic. Nona IT Pub, UnPark, Lalitpur, Nepal						Sep 2011 To Oct 2014 System Admin Responsibilities: Managed and installed packages using yum and rpm tools. Created user accounts, managed user privileges, managing disk space and setting up disk quotas for specific accounts. Created RHEL virtual servers in VmWare center. Configured and setup networks for newly created virtual servers. Installed, configured and supported apache on virtual machines. Set up cron jobs and enabled or disabled jobs as required. Created filesystems using logical volumes and updated fstab. Installed redhat servers using puppet. Cloned virtual machines in VMware ESXi host and migrated between hosts. Created and managed user accounts, user profiles, and privileges. Granted sudo (elevated) privileges as required. Configured local repositories for development servers that were not connected to the satellite server. Configuring and setting up NFS filesystem. Virtual box setup on windows machines using centos vdi images. General troubleshooting."""
	entities = extract_entities(text)
	print(entities)
	print("Time taken:", perf_counter() - start)
