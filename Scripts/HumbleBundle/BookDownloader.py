'''
var allLinks = {};
$('a').each(function(x){ 
	var obj = $(this)[0]; 
	if(['PDF', 'MOBI', 'EPUB','XPS', 'DOC'].includes(obj['innerText'])){
		try{
			var previousTitle = obj.parentElement.parentElement.parentElement.parentElement.parentElement.children[1].children[0].children[0];
			var md5sum = obj.parentElement.parentElement.children[1].children[0].children[1].getAttribute("href");
			var fileName = previousTitle.innerHTML.replace(/[^\x00-\x7F]/g, "").trim().replace(/\s+/g,'-') + "." + obj['innerText'].toLowerCase();
			allLinks[fileName] = [obj['href'], md5sum];
		}
		catch(err){}
	}
});

console.log(JSON.stringify(allLinks));
'''




import urllib
import urllib2
import multiprocessing
from multiprocessing.dummy import Pool as ThreadPool 

allLinks = {"Introducing Windows Azure for IT Professionals.pdf":"http://ligman.me/1IW1oab","Introducing Windows Azure for IT Professionals.mobi":"http://ligman.me/1Uixtlq","Introducing Windows Azure for IT Professionals.epub":"http://ligman.me/1R9Ubgt","Microsoft Azure Essentials Azure Automation.pdf":"http://ligman.me/1H4VXHT","Microsoft Azure Essentials Azure Automation.mobi":"http://ligman.me/1f8XUKy","Microsoft Azure Essentials Azure Automation.epub":"http://ligman.me/1HBEUPi","Microsoft Azure Essentials Azure Machine Learning.pdf":"http://ligman.me/1NDTZR4","Microsoft Azure Essentials Azure Machine Learning.mobi":"http://ligman.me/1Uiy2f9","Microsoft Azure Essentials Azure Machine Learning.epub":"http://ligman.me/1epZ0QU","Microsoft Azure Essentials Fundamentals of Azure.pdf":"http://ligman.me/1JIhgjA","Microsoft Azure Essentials Fundamentals of Azure.mobi":"http://ligman.me/1CQX5uG","Microsoft Azure Essentials Fundamentals of Azure.epub":"http://ligman.me/1JD5Q3i","Microsoft Azure Essentials Fundamentals of Azure, Second Edition.pdf":"http://ligman.me/2sUanwC","Microsoft Azure Essentials Fundamentals of Azure, Second Edition Mobile.pdf":"http://ligman.me/2twPBSD","Microsoft Azure Essentials Migrating SQL Server Databases to Azure  Mobile.pdf":"http://ligman.me/2tE7q0i","Microsoft Azure Essentials Migrating SQL Server Databases to Azure 8.5X11.pdf":"http://ligman.me/2t2y29a","Microsoft Azure ExpressRoute Guide.pdf":"http://ligman.me/2tJ1pj4","Rapid Deployment Guide For Azure Rights Management.pdf":"http://ligman.me/2u2KdXT","Rethinking Enterprise Storage: A Hybrid Cloud Model.pdf":"http://ligman.me/1IW1s9S","Rethinking Enterprise Storage: A Hybrid Cloud Model.mobi":"http://ligman.me/1UixANR","Rethinking Enterprise Storage: A Hybrid Cloud Model.epub":"http://ligman.me/1f8Xvri","BizTalk Server 2016 Licensing Datasheet.pdf":"http://ligman.me/2tEn8Zy","BizTalk Server 2016 Management Pack Guide.doc":"http://ligman.me/2tEbPAp","Enterprise Cloud Strategy.pdf":"http://ligman.me/2u0WD2F","Enterprise Cloud Strategy.mobi":"http://ligman.me/2t2FyB9","Enterprise Cloud Strategy.epub":"http://ligman.me/2uGi1Ig","Enterprise Cloud Strategy  Mobile.pdf":"http://ligman.me/2t2Ghm1",".NET Microservices: Architecture for Containerized .NET Applications.pdf":"http://ligman.me/2sLiBTE",".NET Technology Guidance for Business Applications.pdf":"http://ligman.me/1gfeQ27","Building Cloud Apps with Microsoft Azure: Best practices for DevOps, data storage, high availability, and more.pdf":"http://ligman.me/1KBM8DL","Building Cloud Apps with Microsoft Azure: Best practices for DevOps, data storage, high availability, and more.mobi":"http://ligman.me/1GVxKR6","Building Cloud Apps with Microsoft Azure: Best practices for DevOps, data storage, high availability, and more.epub":"http://ligman.me/1KBM1YL","Containerized Docker Application Lifecycle with Microsoft Platform and Tools.pdf":"http://ligman.me/2v7M0bp","Creating Mobile Apps with Xamarin.Forms, Preview Edition 2.pdf":"http://ligman.me/1dDcwQC","Creating Mobile Apps with Xamarin.Forms, Preview Edition 2.mobi":"http://ligman.me/1LIQw4D","Creating Mobile Apps with Xamarin.Forms, Preview Edition 2.epub":"http://ligman.me/1HCWJ2c","Creating Mobile Apps with Xamarin.Forms: Cross-platform C# programming for iOS, Android, and Windows.pdf":"http://ligman.me/2u1190V","Creating Mobile Apps with Xamarin.Forms: Cross-platform C# programming for iOS, Android, and Windows.mobi":"http://ligman.me/2sE8dNG","Creating Mobile Apps with Xamarin.Forms: Cross-platform C# programming for iOS, Android, and Windows.epub":"http://ligman.me/2twPKVT","Managing Agile Open-Source Software Projects with Microsoft Visual Studio Online.pdf":"http://ligman.me/1NErkvl","Managing Agile Open-Source Software Projects with Microsoft Visual Studio Online.mobi":"http://ligman.me/1KyWplK","Managing Agile Open-Source Software Projects with Microsoft Visual Studio Online.epub":"http://ligman.me/1RabduO","Microsoft Azure Essentials Azure Web Apps for Developers.pdf":"http://ligman.me/1epZeHO","Microsoft Azure Essentials Azure Web Apps for Developers.mobi":"http://ligman.me/2tE9hCx","Microsoft Azure Essentials Azure Web Apps for Developers.epub":"http://ligman.me/2uFU3wF","Microsoft Platform and Tools for Mobile App Development.pdf":"http://ligman.me/2t2WqaR","Microsoft Platform and Tools for Mobile App Development  Mobile.pdf":"http://ligman.me/2sUA9kk","Moving to Microsoft Visual Studio 2010.xps":"http://ligman.me/1CQXMEp","Moving to Microsoft Visual Studio 2010.pdf":"http://ligman.me/1JITgwM","Moving to Microsoft Visual Studio 2010.mobi":"http://ligman.me/1RaaZny","Moving to Microsoft Visual Studio 2010.epub":"http://ligman.me/2uZg49h","Programming Windows 8 Apps with HTML, CSS, and JavaScript.pdf":"http://ligman.me/1LN5APL","Programming Windows 8 Apps with HTML, CSS, and JavaScript.mobi":"http://ligman.me/1GVx0eW","Programming Windows 8 Apps with HTML, CSS, and JavaScript.epub":"http://ligman.me/1dD5sDy","Programming Windows Store Apps with HTML, CSS, and JavaScript, Second Edition.pdf":"http://ligman.me/1RWzfoe","Programming Windows Store Apps with HTML, CSS, and JavaScript, Second Edition.mobi":"http://ligman.me/1JDj7Jl","Programming Windows Store Apps with HTML, CSS, and JavaScript, Second Edition.epub":"http://ligman.me/1f9bOfu","Programming Windows Phone 7 (Special Excerpt 2).xps":"http://ligman.me/1LNdusd","Programming Windows Phone 7 (Special Excerpt 2).pdf":"http://ligman.me/1KyWLZv","Team Foundation Server to Visual Studio Team Services Migration Guide.pdf":"http://ligman.me/2tEKIoU","5 cool things you can do with CRM for tablets.pdf":"http://ligman.me/2uGZkV1","Create Custom Analytics in Dynamics 365 with Power BI.pdf":"http://ligman.me/2tJAEuU","Create of Customize System Dashboards.pdf":"http://ligman.me/1odT1MW","Create Your First CRM Marketing Campaign.pdf":"http://ligman.me/1NJ0vpb","CRM Basics for Outlook basics.pdf":"http://ligman.me/1dHBtdA","CRM Basics for Sales Pros and Service Reps.pdf":"http://ligman.me/1NIYrxw","Give Great Customer Service with CRM.pdf":"http://ligman.me/1qNYIYi","Go Mobile with CRM for Phones  Express.pdf":"http://ligman.me/1rH9Ar3","Go Mobile with CRM for Tablets.pdf":"http://ligman.me/1kvWKEm","Import Contacts into CRM.pdf":"http://ligman.me/1m8yCMD","Introducing Microsoft Social Engagement.pdf":"http://ligman.me/1kvXrxj","Introduction to Business Processes.pdf":"http://ligman.me/1pUnYfG","Meet Your Service Goals with SLAs and Entitlements.pdf":"http://ligman.me/1CWgeLI","Microsoft Dynamics CRM 2016 Interactive Service Hub User Guide.pdf":"http://ligman.me/2v0ShWr","Microsoft Dynamics CRM 2016 On-Premises Volume Licensing and Pricing Guide.pdf":"http://ligman.me/2sF6M19","Microsoft Dynamics CRM for Outlook Installing Guide for use with Microsoft Dynamics CRM Online.pdf":"http://ligman.me/2sVh6qf","Microsoft Dynamics CRM Resource Guide 2015.pdf":"http://ligman.me/2tYdqU8","Microsoft Social Engagement for CRM.pdf":"http://ligman.me/1oB9ptL","Product Overview and Capability Guide Microsoft Dynamics NAV 2016.pdf":"http://ligman.me/2sFbbl0","RAP as a Service for Dynamics CRM.pdf":"http://ligman.me/2v1ok8u","Set Up A Social Engagement Search For Your Product.pdf":"http://ligman.me/1HIcIKB","Social is for Closers.pdf":"http://ligman.me/1Cl328D","Start Working in CRM.pdf":"http://ligman.me/VSpodw","Your Brand Sux.pdf":"http://ligman.me/1S36CGa","10 essential tips and tools for mobile working.pdf":"http://ligman.me/2tEPKBF","An employees guide to healthy computing.pdf":"http://ligman.me/2sVSiyp","Guide for People who have Language or Communication Disabilities.doc":"http://ligman.me/2tEHPV9","Guide for People who have Learning Disabilities.doc":"http://ligman.me/2t3xIav","Introduction to Per Core Licensing and Basic Definitions.pdf":"http://ligman.me/1H1MFKr","Licensing Windows and Microsoft Office for use on the Macintosh.pdf":"http://ligman.me/2u2bSbh","VLSC Software Assurance Guide.pdf":"http://ligman.me/2u7XYoT","Windows Server 2016 and System Center 2016 Pricing and Licensing FAQs.pdf":"http://ligman.me/2txAWqi","Access 2013 Keyboard Shortcuts .pdf":"http://ligman.me/1sgBtn4","Azure AD/Office 365 seamless sign-in.pdf":"http://ligman.me/2tEnvmU","Content Encryption in Microsoft Office 365.pdf":"http://ligman.me/2txxLic","Controlling Access to Office 365 and Protecting Content on Devices.pdf":"http://ligman.me/2u89sJ3","Customize Word 2013 Keyboard Shortcuts .pdf":"http://ligman.me/1qzON6Q","Data Resiliency in Microsoft Office 365.pdf":"http://ligman.me/2tXYR34","Excel 2013 Keyboard Shortcuts .pdf":"http://ligman.me/1onTg9n","Excel 2016 keyboard shortcuts and function keys.doc":"http://ligman.me/2uH1nrZ","Excel Online Keyboard Shortcuts .pdf":"http://ligman.me/VP2t2L","File Protection Solutions in Office 365.pdf":"http://ligman.me/2v0u0jd","First Look: Microsoft Office 2010.xps":"http://ligman.me/1dD6v6s","First Look: Microsoft Office 2010.pdf":"http://ligman.me/1Ra595J","Get Started With Microsoft OneDrive .pdf":"http://ligman.me/2v0H3ku","Get Started With Microsoft Project Online.pdf":"http://ligman.me/2tEtms3","Getting started with MyAnalytics.doc":"http://ligman.me/2u88i06","How To Recover That Un-Saved Office Document .pdf":"http://ligman.me/1jWMJA2","InfoPath 2013 Keyboard Shortcuts.pdf":"http://ligman.me/1qZlnOJ","Keyboard shortcuts for Microsoft Outlook 2013 and 2016.doc":"http://ligman.me/2u2RnLQ","Keyboard shortcuts for Microsoft Word 2016 for Windows.doc":"http://ligman.me/2v0AQFy","Licensing Microsoft Office 365 ProPlus Subscription Service in Volume Licensing.pdf":"http://ligman.me/1xqtaWN","Licensing Microsoft Office software in Volume Licensing.pdf":"http://ligman.me/2v0v72p","Microsoft Access 2013 Quick Start Guide.pdf":"http://ligman.me/1HCDxl9","Microsoft Classroom Deployment.pdf":"http://ligman.me/2u7Lw8N","Microsoft Excel 2013 Quick Start Guide.pdf":"http://ligman.me/1HByNKS","Microsoft Excel 2016 for Mac Quick Start Guide .pdf":"http://ligman.me/29a22WR","Microsoft Excel 2016 Quick Start Guide.pdf":"http://ligman.me/29bcJtd","Microsoft Excel Mobile Quick Start Guide .pdf":"http://ligman.me/29rwoHw","Microsoft Excel VLOOKUP Troubleshooting Tips.pdf":"http://ligman.me/2sF7s6H","Microsoft OneNote 2013 Quick Start Guide.pdf":"http://ligman.me/1CSMobd","Microsoft OneNote 2016 for Mac Quick Start Guide .pdf":"http://ligman.me/29d5XTw","Microsoft OneNote 2016 Quick Start Guide.pdf":"http://ligman.me/29rwoY0","Microsoft OneNote 2016 Tips and Tricks.pdf":"http://ligman.me/29d1wc3","Microsoft OneNote Mobile Quick Start Guide .pdf":"http://ligman.me/29fudHc","Microsoft Outlook 2013 Quick Start Guide.pdf":"http://ligman.me/1FYtDD8","Microsoft Outlook 2016 for Mac Quick Start Guide.pdf":"http://ligman.me/29hVdVa","Microsoft Outlook 2016 Quick Start Guide.pdf":"http://ligman.me/29fDult","Microsoft Outlook 2016 Tips and Tricks.pdf":"http://ligman.me/29cfePX","Microsoft Powerpoint 2013 Quick Start Guide.pdf":"http://ligman.me/1NCfcKC","Microsoft PowerPoint 2016 for Mac Quick Start Guide.pdf":"http://ligman.me/29fDylj","Microsoft PowerPoint 2016 for Mac Quick Start Guide .pdf":"http://ligman.me/29fDylj","Microsoft PowerPoint Mobile Quick Start Guide .pdf":"http://ligman.me/29d5AbX","Microsoft Project 2013 Quick Start Guide.pdf":"http://ligman.me/1JI6V77","Microsoft Publisher 2013 Quick Start Guide.pdf":"http://ligman.me/1H4Q0e5","Microsoft Visio 2013 Quick Start Guide.pdf":"http://ligman.me/1LMpRns","Microsoft Word 2013 Quick Start Guide.pdf":"http://ligman.me/1HCCCRP","Microsoft Word 2016 for Mac Quick Start Guide .pdf":"http://ligman.me/29FzGG5","Microsoft Word 2016 Quick Start Guide.pdf":"http://ligman.me/29e6cTO","Microsoft Word Mobile Quick Start Guide .pdf":"http://ligman.me/29gfrkN","Microsoft Office 365: Connect and Collaborate Virtually Anywhere, Anytime.pdf":"http://ligman.me/1Ra5c1c","Monitoring and protecting sensitive data in Office 365.doc":"http://ligman.me/29vGIvY","Office 365 Dedicated Platform vNext Service Release.pdf":"http://ligman.me/2sVGUSX","Office 365 Licensing Brief.pdf":"http://ligman.me/2u1KmL9","OneNote 2013 Keyboard Shortcuts .pdf":"http://ligman.me/1n49kzj","OneNote Online Keyboard Shortcuts .pdf":"http://ligman.me/1qZlFVR","Outlook 2013 Keyboard Shortcuts .pdf":"http://ligman.me/TWa2Dg","Outlook Web App Keyboard Shortcuts .pdf":"http://ligman.me/1xzdEtT","Own Your Future: Update Your Skills with Resources and Career Ideas from Microsoft.xps":"http://ligman.me/1HCQyeA","Own Your Future: Update Your Skills with Resources and Career Ideas from Microsoft.pdf":"http://ligman.me/1Cg5iOv","Own Your Future: Update Your Skills with Resources and Career Ideas from Microsoft.mobi":"http://ligman.me/2sUC4FK","Own Your Future: Update Your Skills with Resources and Career Ideas from Microsoft.epub":"http://ligman.me/2u12ggX","PowerPoint Online Keyboard Shortcuts .pdf":"http://ligman.me/1onU8Ld","Project 2013 Keyboard Shortcuts .pdf":"http://ligman.me/1vM9mwt","Publisher 2013 Keyboard Shortcuts .pdf":"http://ligman.me/1rB8nl1","Security and Privacy For Microsoft Office 2010 Users.pdf":"http://ligman.me/1JDjqUt","Security and Privacy For Microsoft Office 2010 Users.mobi":"http://ligman.me/1eqdXCI","Security and Privacy For Microsoft Office 2010 Users.epub":"http://ligman.me/1Uj0hu2","Security Incident Management in Microsoft Office 365.pdf":"http://ligman.me/2tYk9gX","SharePoint Online Dedicated &amp; OneDrive for Business Dedicated vNext Service Release.pdf":"http://ligman.me/2sVrsGy","Skype for Business User Tips &amp; Tricks for Anyone .pdf":"http://ligman.me/1M7Xr5v","Switching from Google Apps to Office 365 for business.pdf":"http://ligman.me/2t3nqXV","Tenant Isolation in Microsoft Office 365.pdf":"http://ligman.me/2u2K9aI","Visio 2013 Keyboard Shortcuts .pdf":"http://ligman.me/1vM9H2d","Windows 10 Tips and Tricks.pdf":"http://ligman.me/2sFsnXy","Word 2013 Keyboard Shortcuts .pdf":"http://ligman.me/1m6xucg","Word Online Keyboard Shortcuts .pdf":"http://ligman.me/1qzRntH","Working with SmartArt Graphics Keyboard Shortcuts .pdf":"http://ligman.me/1lJmKeW","Ask, find, and actharnessing the power of Cortana and Power BI.doc":"http://ligman.me/29ZNaMN","Bidirectional cross-filtering in SQL Server Analysis Services 2016 and Power BI Desktop.doc":"http://ligman.me/2tEERQt","Configuring Power BI mobile apps with Microsoft Intune.doc":"http://ligman.me/29sp3nZ","Getting started with the Power BI for Android app.doc":"http://ligman.me/29LXmMt","Getting Started with the Power BI for iOS app.doc":"http://ligman.me/29EmfZc","How to plan capacity for embedded analytics with Power BI Premium.pdf":"http://ligman.me/2t3HOIt","Introducing Microsoft Power BI.pdf":"http://ligman.me/2tE789y","Introducing Microsoft Power BI  Mobile.pdf":"http://ligman.me/2sUDY9j","Microsoft Power BI Premium Whitepaper.pdf":"http://ligman.me/2tEI5U4","Power BI mobile appsenabling data analytics on the go.doc":"http://ligman.me/29yWFFf","Propelling digital transformation in manufacturing operations with Power BI.doc":"http://ligman.me/2tEtGXW","Using Power BI to visualize data insights from Microsoft Dynamics CRM Online.doc":"http://ligman.me/2txJKMz","Microsoft Dynamics GP 2015 R2 PowerShell Users Guide.pdf":"http://ligman.me/2uH1kN1","PowerShell Integrated Scripting Environment 3.0.pdf":"http://ligman.me/2tY8L4x","Simplify Group Policy administration with Windows PowerShell.pdf":"http://ligman.me/2tyf2TJ","Windows PowerShell 3.0 Examples.pdf":"http://ligman.me/2v0vXMn","Windows PowerShell 3.0 Language Quick Reference.pdf":"http://ligman.me/2u8l13d","WINDOWS POWERSHELL 4.0 LANGUAGE QUICK REFERENCE.pdf":"http://ligman.me/2u8jZEr","Windows PowerShell 4.0 Language Reference Examples.pdf":"http://ligman.me/1omCrM6","Windows PowerShell Command Builder Users Guide.pdf":"http://ligman.me/2sFvbUs","Windows PowerShell Desired State Configuration Quick Reference.pdf":"http://ligman.me/2tYmSHb","WINDOWS POWERSHELL INTEGRATED SCRIPTING ENVIRONMENT 4.0.pdf":"http://ligman.me/1n3mkVY","Windows PowerShell Web Access.pdf":"http://ligman.me/2tEXUKw","WMI in PowerShell 3.0.pdf":"http://ligman.me/2tEAt3Z","WMI in Windows PowerShell 4.0.pdf":"http://ligman.me/2t3uPGw","Configuring Microsoft SharePoint Hybrid Capabilities.pdf":"http://ligman.me/2uFTByu","Configuring Microsoft SharePoint Hybrid Capabilities  Mobile.pdf":"http://ligman.me/2tXvePt","Deployment guide for Microsoft SharePoint 2013.pdf":"http://ligman.me/12FIZ1I","Microsoft SharePoint Server 2016 Architectural Models.pdf":"http://ligman.me/2v0Dhb1","Planning and Preparing for Microsoft SharePoint Hybrid  8.5 X 11.pdf":"http://ligman.me/2u0QCD2","Planning and Preparing for Microsoft SharePoint Hybrid  Mobile.pdf":"http://ligman.me/2sEzMGA","RAP as a Service for SharePoint Server.pdf":"http://ligman.me/2u8h5PG","SharePoint Online Dedicated Service Description.pdf":"http://ligman.me/2uGN9ao","SharePoint Products Keyboard Shortcuts .pdf":"http://ligman.me/TL3pn1","SharePoint Server 2016 Databases  Quick Reference Guide.pdf":"http://ligman.me/2txHeGo","SharePoint Server 2016 Quick Start Guide.pdf":"http://ligman.me/29FkNr3","5 Tips For A Smooth SSIS Upgrade to SQL Server 2012.pdf":"http://ligman.me/1anyEJj","Backup and Restore of SQL Server Databases.pdf":"http://ligman.me/N1HEpM","Data Science with Microsoft SQL Server 2016.pdf":"http://ligman.me/2sVpUwk","Deeper insights across data with SQL Server 2016  Technical White Paper.pdf":"http://ligman.me/2u8ao0i","Deploying SQL Server 2016 PowerPivot and Power View in a Multi-Tier SharePoint 2016 Farm.doc":"http://ligman.me/2u7MT7t","Deploying SQL Server 2016 PowerPivot and Power View in SharePoint 2016.doc":"http://ligman.me/2u89lNQ","Guide to Migrating from Oracle to SQL Server 2014 and Azure SQL Database.pdf":"http://ligman.me/1ReR3Qq","Introducing Microsoft Azure HDInsight.pdf":"http://ligman.me/1RWzIGZ","Introducing Microsoft Azure HDInsight.mobi":"http://ligman.me/1CQXzkt","Introducing Microsoft Azure HDInsight.epub":"http://ligman.me/1HBRMVs","Introducing Microsoft Data Warehouse Fast Track for SQL Server 2016.pdf":"http://ligman.me/2u2j5sf","Introducing Microsoft SQL Server 2012.pdf":"http://ligman.me/1gfab07","Introducing Microsoft SQL Server 2012.mobi":"http://ligman.me/1JIDq58","Introducing Microsoft SQL Server 2012.epub":"http://ligman.me/1KBMoTl","Introducing Microsoft SQL Server 2014.pdf":"http://ligman.me/1C7dU9J","Introducing Microsoft SQL Server 2014.mobi":"http://ligman.me/1GVycPq","Introducing Microsoft SQL Server 2014.epub":"http://ligman.me/1LIJflp","Introducing Microsoft SQL Server 2016: Mission-Critical Applications, Deeper Insights, Hyperscale Cloud, Preview 2.pdf":"http://ligman.me/2u7ml6r","Introducing Microsoft SQL Server 2016: Mission-Critical Applications, Deeper Insights, Hyperscale Cloud, Preview 2.mobi":"http://ligman.me/2tXqzgh","Introducing Microsoft SQL Server 2016: Mission-Critical Applications, Deeper Insights, Hyperscale Cloud, Preview 2.epub":"http://ligman.me/2u0ZCYU","Introducing Microsoft SQL Server 2016: Mission-Critical Applications, Deeper Insights, Hyperscale Cloud, Preview 2  Mobile.pdf":"http://ligman.me/2t2o340","Introducing Microsoft Technologies for Data Storage, Movement and Transformation.doc":"http://ligman.me/2txRCxI","Introducing Microsoft SQL Server 2008 R2.xps":"http://ligman.me/1CQXzko","Introducing Microsoft SQL Server 2008 R2.pdf":"http://ligman.me/1KyNJvs","Introducing Microsoft SQL Server 2008 R2.mobi":"http://ligman.me/1C7dEYi","Introducing Microsoft SQL Server 2008 R2.epub":"http://ligman.me/1IzBL34","Microsoft SharePoint Server 2016 Reviewers Guide.pdf":"http://ligman.me/29pcQFA","Microsoft SQL Server 2012 Tutorials: Analysis Services  Data Mining Step-by-Step.pdf":"http://ligman.me/N1J8A8","Microsoft SQL Server 2012 Tutorials: Analysis Services  Multidimensional Modeling Step-by-Step.pdf":"http://ligman.me/N1JfvI","Microsoft SQL Server 2012 Tutorials: Reporting Services Quick Step-by-Step.pdf":"http://ligman.me/16E6G9L","Microsoft SQL Server 2012 Tutorials: Writing Transact-SQL-Statements.pdf":"http://ligman.me/16dHXZ9","Microsoft SQL Server 2014 Licensing Guide.pdf":"http://ligman.me/1S1f34H","Microsoft SQL Server 2016 Licensing Datasheet.pdf":"http://ligman.me/2sFqolM","Microsoft SQL Server 2016 Licensing Guide.pdf":"http://ligman.me/2tEHwtq","Microsoft SQL Server 2016 Mission-Critical Performance Technical White Paper.pdf":"http://ligman.me/2uGQTc7","Microsoft SQL Server 2016 New Innovations.pdf":"http://ligman.me/2u7TbUy","Microsoft SQL Server 2016 SP1 Editions.pdf":"http://ligman.me/2tYmEzR","Microsoft SQL Server In-Memory OLTP and Columnstore Feature Comparison.pdf":"http://ligman.me/2tYaW8d","RAP as a Service for SQL Server.pdf":"http://ligman.me/2u2HKg6","SQLCATs Guide to: Relational Engine.pdf":"http://ligman.me/2tEHLVm","Xquery Language Reference.pdf":"http://ligman.me/11IMDlh","Surface Book User Guide.pdf":"http://ligman.me/29i2CEe","Surface Pro 4 User Guide.pdf":"http://ligman.me/29hofVk","Guide to Microsoft System Center Management Pack for SQL Server 2016 Reporting Services (Native Mode).doc":"http://ligman.me/2sVrwWU","Guide to System Center Management Pack for Windows Print Server 2016.doc":"http://ligman.me/2u2uvvZ","Introducing Microsoft System Center 2012 R2.pdf":"http://ligman.me/1dD6S0J","Introducing Microsoft System Center 2012 R2.mobi":"http://ligman.me/1NEgrJQ","Introducing Microsoft System Center 2012 R2.epub":"http://ligman.me/1IzC1z4","Microsoft System Center Building a Virtualized Network Solution, Second Edition.pdf":"http://ligman.me/2sUch05","Microsoft System Center Building a Virtualized Network Solution, Second Edition.mobi":"http://ligman.me/2twxADW","Microsoft System Center Building a Virtualized Network Solution, Second Edition.epub":"http://ligman.me/2sEqaM0","Microsoft System Center Data Protection for the Hybrid Cloud.pdf":"http://ligman.me/1JDrhBp","Microsoft System Center Data Protection for the Hybrid Cloud.mobi":"http://ligman.me/1RWFCrK","Microsoft System Center Data Protection for the Hybrid Cloud.epub":"http://ligman.me/1M05t0d","Microsoft System Center Deploying Hyper-V with Software-Defined Storage &amp; Networking.pdf":"http://ligman.me/1C7okGv","Microsoft System Center Deploying Hyper-V with Software-Defined Storage &amp; Networking.mobi":"http://ligman.me/1UjcLBK","Microsoft System Center Deploying Hyper-V with Software-Defined Storage &amp; Networking.epub":"http://ligman.me/1HBYNpg","Microsoft System Center Extending Operations Manager Reporting.pdf":"http://ligman.me/1KBVfnS","Microsoft System Center Extending Operations Manager Reporting.mobi":"http://ligman.me/1IzIbPR","Microsoft System Center Extending Operations Manager Reporting.epub":"http://ligman.me/1HBYYRF","Microsoft System Center Introduction to Microsoft Automation Solutions.pdf":"http://ligman.me/1IzHZA1","Microsoft System Center Introduction to Microsoft Automation Solutions.mobi":"http://ligman.me/1RWFd8K","Microsoft System Center Introduction to Microsoft Automation Solutions.epub":"http://ligman.me/1HCW4Or","Microsoft System Center Operations Manager Field Experience.pdf":"http://ligman.me/1GUUqSD","Microsoft System Center Operations Manager Field Experience.mobi":"http://ligman.me/1Cg8UQs","Microsoft System Center Operations Manager Field Experience.epub":"http://ligman.me/1KyVGkv","Microsoft System Center Software Update Management Field Experience.pdf":"http://ligman.me/1CQXNbj","Microsoft System Center Software Update Management Field Experience.mobi":"http://ligman.me/1M05ktI","Microsoft System Center Software Update Management Field Experience.epub":"http://ligman.me/1Ujd8fL","Microsoft System Center: Building a Virtualized Network Solution.pdf":"http://ligman.me/1GUOZ6b","Microsoft System Center: Building a Virtualized Network Solution.mobi":"http://ligman.me/1HCR2l0","Microsoft System Center: Building a Virtualized Network Solution.epub":"http://ligman.me/1FYOjLl","Microsoft System Center: Cloud Management with App Controller.pdf":"http://ligman.me/1GUP0qL","Microsoft System Center: Cloud Management with App Controller.mobi":"http://ligman.me/1GVyNAv","Microsoft System Center: Cloud Management with App Controller.epub":"http://ligman.me/1HBSfqC","Microsoft System Center: Configuration Manager Field Experience.pdf":"http://ligman.me/1KBMN8a","Microsoft System Center: Configuration Manager Field Experience.mobi":"http://ligman.me/1HCQQCb","Microsoft System Center: Configuration Manager Field Experience.epub":"http://ligman.me/1Uj1dyo","Microsoft System Center: Designing Orchestrator Runbooks.pdf":"http://ligman.me/1f9cKQZ","Microsoft System Center: Designing Orchestrator Runbooks.mobi":"http://ligman.me/1RWzUWP","Microsoft System Center: Designing Orchestrator Runbooks.epub":"http://ligman.me/1LIJxJ0","Microsoft System Center: Integrated Cloud Platform.pdf":"http://ligman.me/1gfaIzh","Microsoft System Center: Integrated Cloud Platform.mobi":"http://ligman.me/1LIJHA5","Microsoft System Center: Integrated Cloud Platform.epub":"http://ligman.me/1HCQXxv","Microsoft System Center: Network Virtualization and Cloud Computing.pdf":"http://ligman.me/1JIF6vB","Microsoft System Center: Network Virtualization and Cloud Computing.mobi":"http://ligman.me/1TaxTZD","Microsoft System Center: Network Virtualization and Cloud Computing.epub":"http://ligman.me/1TaxTJ5","Microsoft System Center: Optimizing Service Manager.pdf":"http://ligman.me/1M00Lzu","Microsoft System Center: Optimizing Service Manager.mobi":"http://ligman.me/1Cg5xc8","Microsoft System Center: Optimizing Service Manager.epub":"http://ligman.me/1IWkjlf","Microsoft System Center: Troubleshooting Configuration Manager.pdf":"http://ligman.me/1M00v3u","Microsoft System Center: Troubleshooting Configuration Manager.mobi":"http://ligman.me/1GUOMzL","Microsoft System Center: Troubleshooting Configuration Manager.epub":"http://ligman.me/1TaxqXr","Whats new in System Center 2016 White Paper.pdf":"http://ligman.me/2t3NaDl","Understanding Microsoft Virtualizaton R2 Solutions.xps":"http://ligman.me/1M05yAY","Understanding Microsoft Virtualizaton R2 Solutions.pdf":"http://ligman.me/1eql6Ts","Deploying Windows 10: Automating deployment by using System Center Configuration Manager.pdf":"http://ligman.me/2sE9XX1","Deploying Windows 10: Automating deployment by using System Center Configuration Manager.mobi":"http://ligman.me/2uZgfBj","Deploying Windows 10: Automating deployment by using System Center Configuration Manager.epub":"http://ligman.me/2tDZAUn","Deploying Windows 10: Automating deployment by using System Center Configuration Manager  Mobile.pdf":"http://ligman.me/2twLeqF","Getting the most out of Microsoft Edge.doc":"http://ligman.me/2sF5tQ8","Introducing Windows 10 for IT Professionals.pdf":"http://ligman.me/2t2WmYx","Introducing Windows 10 for IT Professionals.mobi":"http://ligman.me/2uZiHI3","Introducing Windows 10 for IT Professionals.epub":"http://ligman.me/2t2qX8T","Introducing Windows 10 for IT Professionals, Preview Edition.pdf":"http://ligman.me/1Uiyx8Q","Introducing Windows 10 for IT Professionals, Preview Edition.mobi":"http://ligman.me/1C6Tg9G","Introducing Windows 10 for IT Professionals, Preview Edition.epub":"http://ligman.me/1HCIlqM","Introducing Windows 8.1 for IT Professionals.pdf":"http://ligman.me/1JDrMeG","Introducing Windows 8.1 for IT Professionals.mobi":"http://ligman.me/1GVGV3U","Introducing Windows 8.1 for IT Professionals.epub":"http://ligman.me/1JDrIvt","Introducing Windows 8: An Overview for IT Professionals.pdf":"http://ligman.me/1GVGQgI","Introducing Windows 8: An Overview for IT Professionals.mobi":"http://ligman.me/1RWFVCS","Introducing Windows 8: An Overview for IT Professionals.epub":"http://ligman.me/1RWFUig","Licensing Windows desktop operating system for use with virtual machines.pdf":"http://ligman.me/2txIfxW","Protecting your data with Windows 10 BitLocker.doc":"http://ligman.me/2sVHDUg","RAP as a Service for Windows Desktop.pdf":"http://ligman.me/2u2R83b","Shortcut Keys for Windows 10.doc":"http://ligman.me/29ErxWs","Use Reset to restore your Windows 10 PC.doc":"http://ligman.me/29yWAAO","Volume Licensing Reference Guide Windows 10 Desktop Operating System.pdf":"http://ligman.me/2sFzkaR","Windows 10 IT Pro Essentials Support Secrets.pdf":"http://ligman.me/2uFUOG1","Windows 10 IT Pro Essentials Support Secrets.mobi":"http://ligman.me/2twRrCJ","Windows 10 IT Pro Essentials Support Secrets.epub":"http://ligman.me/2t2mx1M","Windows 10 IT Pro Essentials Top 10 Tools.pdf":"http://ligman.me/2t2cYjp","Windows 10 IT Pro Essentials Top 10 Tools.mobi":"http://ligman.me/2twtAmW","Windows 10 IT Pro Essentials Top 10 Tools.epub":"http://ligman.me/2u0YnZu","Windows 10 IT Pro Essentials Top 10 Tools  Mobile.pdf":"http://ligman.me/2u15CAR","Work Smart: Windows 8 Shortcut Keys.pdf":"http://ligman.me/1sfkqBW","Automating Windows Server 2016 configuration with PowerShell and DSC.doc":"http://ligman.me/2txOv8Z","Introducing Windows Server 2008 R2.xps":"http://ligman.me/1M06aXa","Introducing Windows Server 2008 R2.pdf":"http://ligman.me/1FYVYcy","Introducing Windows Server 2008 R2.mobi":"http://ligman.me/1dDcZ5h","Introducing Windows Server 2008 R2.epub":"http://ligman.me/1H5ajbj","Introducing Windows Server 2012.pdf":"http://ligman.me/1M0681D","Introducing Windows Server 2012.mobi":"http://ligman.me/1JIV1Kk","Introducing Windows Server 2012.epub":"http://ligman.me/1eqlNMp","Introducing Windows Server 2012 R2.pdf":"http://ligman.me/1NCxHi5","Introducing Windows Server 2012 R2.mobi":"http://ligman.me/1KBX7Nw","Introducing Windows Server 2012 R2.epub":"http://ligman.me/1IzJ6Qp","Introducing Windows Server 2016.pdf":"http://ligman.me/2uFKRZd","Introducing Windows Server 2016  Mobile.pdf":"http://ligman.me/2tDMJl0","Introducing Windows Server 2016 Technical Preview.pdf":"http://ligman.me/2uFDelL","Introducing Windows Server 2016 Technical Preview  Mobile.pdf":"http://ligman.me/2twmtKY","Introducing Windows Server 2012 R2 Preview Release.pdf":"http://ligman.me/1f9k8fe","Introducing Windows Server 2012 R2 Preview Release.mobi":"http://ligman.me/1eqm4za","Introducing Windows Server 2012 R2 Preview Release.epub":"http://ligman.me/2tXBiHF","Offline Assessment for Active Directory.pdf":"http://ligman.me/2v1cDyG","RAP as a Service for Active Directory.pdf":"http://ligman.me/2txRQFd","RAP as a Service for Failover Cluster.pdf":"http://ligman.me/2v1zdYa","RAP as a Service for Internet Information Services.pdf":"http://ligman.me/2sW0A9v","RAP as a Service for Windows Server Hyper-V.pdf":"http://ligman.me/2txQLgl","Windows Server 2016 Licensing.pdf":"http://ligman.me/2sFbVq3"}

def getThatBook(stuff):
	print "Getting %s" % stuff[0]
	try:
		response = urllib2.urlopen(stuff[1])
		urllib.URLopener().retrieve(response.geturl(), stuff[0])
	except Exception as e:
		print "Failed to get %s" % stuff[0]
		print e

parsedStuff = []
for link in allLinks:
	parsedStuff.append([link, allLinks[link]])

pool = ThreadPool(multiprocessing.cpu_count())

pool.map(getThatBook, parsedStuff)

pool.close()
pool.join()

