# how to handle input profionally 


class inputHandler:
    def getNonEmptyString(self, prompt: str, minLength=1, maxLength=20) -> str:
        while True:
            value = input(prompt).strip()
            if len(value) < minLength:
                print(f"Input must be at least {minLength} characters")
            elif len(value) > maxLength:
                print(f"Input value must not exceed {maxLength} characters")
            else:
                return value

def addtopic(topicName):
    topics = ["samod"]
    if topicName in topics:
        print("Topic already exists")
    else:
        topics.append(topicName)
        print(f"Topic name `{topicName}` added.")

def main():
    handler = inputHandler()
    topicName = handler.getNonEmptyString("Enter your name: ", minLength=3, maxLength=10)
    addtopic(topicName)
if __name__ == "__main__":
    main()
    pass
    
    
                

