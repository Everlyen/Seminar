Please feel free to make changes that you feel are useful to the [[README]] and to anything else that has been written. 

### Vault structure 
- Perhaps we can remove some of the other papers or add them to a References/additional reading? Not sure if sharing everything is useful? 
AB: Good idea. 
- I wonder if it's useful to put the concepts in categories, like protein folding related, pLM related and metrics? 
	- Argument for: unfamiliar concepts are contextualized even before we reach them. 
	- Argument against: concepts are beneath another layer which increases friction to access/modification and also it defeats a little bit the purpose of a flat structure where concepts can belong to multiple categories simultaneously. 
	- Alternative which I started was to use the landing page to give the concepts the context I thought might be useful. Do you think this works? YES
 AB: I would be against it. I like how the landing page is organised. We can access the concepts through this landing page which has a neat organisation. We can change this organisation structure later on based on what is convenient. If we start to create subfolders inside the concepts we would have to move the notes everytime we change. A flat folder is convenient to add new concepts. But I'm curious if there is a way to include all new notes under concepts in the landing page under the heading "uncategorised" automatically. Like as soon as a new concept is created it goes directly into that heading and we can later put it in a category we think it belongs to. 
 
 CP: I know how to do this but only using dataview. It would be another community plugin to install but may be worth it for this. Using that we can query all concepts and add them to the landing page - we wouldn't even need to organize them, we could use tags to show what they belong to: 
 eg. 
 ```dataview
 TABLE without ID 
	 file.name AS "Concept", 
	 tags AS "Connections"
Where file.folder = "Insights/2_Concepts"
 ```
 It would generate a table that looks something like this: 
 ![[Pasted image 20260930180500.png|418]]
### Sync issue
Minor issue: Is it possible that the json files that are being synced are also those from Insights/4_Protein web/.obsidian? I don't see that folder in obsidian but I do still have the changes for the json files showing up before staging. 
AB: Yes, we have to git remove this entirely. Checking if that works. 
CP: I still see the .json files showing up. It's not a huge problem, I just ignore those when staging. 