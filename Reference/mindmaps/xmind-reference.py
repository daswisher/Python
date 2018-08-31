from xmind.core.topic import TopicElement
from xmind.core import workbook,saver

import xmind

myWorkbook = xmind.load("please-always-overwrite-the-output.xmind") # load an existing file or create a new workbook if nothing is found

mainSheet=myWorkbook.getPrimarySheet()
mainSheet.setTitle("first sheet")
rootTopic=mainSheet.getRootTopic()
rootTopic.setTitle("root node")

topics = ["first", "second", "third", "fourth", "fifth"]

for topic in topics:
    newTopic = TopicElement() # Initialize topic object
    newTopic.setTitle(topic) # Set node text
    rootTopic.addSubTopic(newTopic) # Attach the topic to the root topic

myWorkbook.addSheet(mainSheet) # the second sheet is now added to the workbook

xmind.save(myWorkbook,"test.xmind") # and we save

