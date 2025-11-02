
def greet():
    print("Hi")
    print('This is an AI Agent Workshop')

def takeInput():
    userInput = input("Enter your symptom: ")
    print(userInput)
    return userInput

class ChatGpt_LLM:
    def _init_(self, model_name):
        self.model_name = model_name

    def generateResponse(self, prompt):
        # call openai LLM API to get response based on the prompt
        # openai url
        # openai key
        # make http call
        return "This is a dummy respone from " + self.model_name 
    
class Gemini_LLM:
    def _init_(self, model_name):
        self.model_name = model_name

    def generateResponse(self, prompt):
        # call gemini LLM API to get response based on the prompt
        # gemini url
        # gemini key
        # make http call
        return "This is a dummy respone from " + self.model_name 
    
class Practo_Tool:
    def _init_(self, name):
        self.name = name
    def useTool(self, input):
        # api url 
        # api Key 
        # http call
     print("Using Tool " + self.name + "with input " + input)

class Messanger_Tool:
    def _init_(self, name):
        self.name = name

    def useTool(self, input):
        # api url 
        # api Key 
        # http call
        print("Using Tool " + self.name + "with input " + input)

class agent:
    def _init_(self, name, llm, tool):
        self.name = name
        self.llm = llm 
        self.tool = tool

    def giveAdvice(self, symptom):
        # llm = ChatGpt_LLM("gpt-4")
        response = llm.generateResponse("Provide advice for the symptom: " + symptom)
        print("Advice for " + symptom + ": " + response)

    def takeAction(self, input):
        tool.useTool(input)

    def giveAdviceAndTakeAction(self, symptom):
        self.giveAdvice(symptom)
        self.takeAction(symptom)

class AutoAgent:
    def _init_(self, name, llm, tool, prompt):
        self.name = name
        self.llm = llm
        self.tool = tool
        self.prompt = prompt

    def decideToUseTool(self, response):
        # logic to decide whether to use tool based on response
        if "visit doctor" in response:
            return True
        return False 

    def execute(self, prompt):
        response = llm.generateResponse(self.prompt)
        print("Advice for " + symptom + ": " + response)
        if(self.decideToUseTool(response)):
            tool.useTool(input)
        else:
            print("No Action Needed")

chatMessages = []



advisorAgent = AutoAgent("AutoHealthBot", ChatGpt_LLM("gpt-4"), Practo_Tool("PractoAPI"), "Provide Advice for problem: " + chatMessages) 
advisorAgent.execute()

class Manager():
    def _init_(self, name, agents):
        self.name = name
        self.agents = agents

    def coordinate(self, symptom):
        for agent in self.agents:
            agent.execute()
    

greet()
 
name = "Ashu"
age = 25

symptomlist = [{
    "name": "cough",
    "severity": "mild",
    "duration": "2 days",
    "priority": 1,
},{
    "name": "fever",
    "severity": "high",
    "duration": "5 days",
    "priority": 2,
}, {
    "name": "headache",
    "severity": "low",
    "duration": "1 day",
    "priority": 2,
}]

# print("Hi")
# print(name)

# # print(symptomlist)
# # print(symptomlist[0])

# for symptom in symptomlist:
#     if (symptom["priority"] == 2):
#          print(symptom["name"])
#          print(symptom["priority"])

symptom = takeInput()

llm = ChatGpt_LLM("gpt-4")
tool = Practo_Tool("PractoAPI")
agent = agent("HealthBot1.0", llm, tool)
agent.giveAdvice(symptom)

print("Thank you for using our bot")
